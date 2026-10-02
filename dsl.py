"""Tiny authoring DSL for PyPath lessons.

Every sub-level is written with S(...). The builder turns it into the generic
Lesson → pages → blocks + Quiz structure the app renders, so the UI never needs
to know about specific topics.
"""
import textwrap

def _d(s):
    return textwrap.dedent(s).strip("\n") if s is not None else None

def _t(s):
    return " ".join(s.split())

class Sub:
    def __init__(self, title, summary, what, *, points=None, key=None, syntax=None, syn=None,
                 ex=(), rules=(), mistake=None, q=()):
        self.title, self.summary = title, summary
        self.what, self.points, self.key = what, points, key
        self.syntax, self.syn = syntax, syn or []
        self.ex = list(ex)
        self.rules, self.mistake = list(rules), mistake
        self.q = list(q)

def S(*a, **k):
    return Sub(*a, **k)

def L(title, description, subs):
    return {"title": title, "description": description, "subs": subs}

# ───────────── builders ─────────────

def build_examples(sub):
    """Yields (code, output, opts) for validation."""
    for e in sub.ex:
        code, out = _d(e[0]), _d(e[1]) if e[1] is not None else None
        opts = e[3] if len(e) > 3 else {}
        yield code, out, opts

def build_sub(sub, sid, code):
    pages = []
    first = [{"type": "text", "text": _t(sub.what)}]
    if sub.points:
        first.append({"type": "bullets", "items": [_t(p) for p in sub.points]})
    if sub.key:
        first.append({"type": "keypoint", "text": _t(sub.key)})
    pages.append({"title": sub.title, "blocks": first})

    if sub.syntax:
        b = {"type": "code", "code": _d(sub.syntax), "caption": "Syntax"}
        if sub.syn:
            b["explanation"] = [_t(x) for x in sub.syn]
        pages.append({"title": "Syntax", "blocks": [b]})

    for i, e in enumerate(sub.ex):
        b = {"type": "code", "code": _d(e[0])}
        if e[1] is not None:
            b["output"] = _d(e[1])
        if len(e) > 2 and e[2]:
            b["explanation"] = [_t(x) for x in e[2]]
        title = "Example" if len(sub.ex) == 1 else f"Example {i + 1}"
        pages.append({"title": title, "blocks": [b]})

    last = []
    if sub.rules:
        last.append({"type": "bullets", "items": [_t(r) for r in sub.rules]})
    if sub.mistake:
        mcode, mtext = sub.mistake
        if mcode:
            last.append({"type": "code", "code": _d(mcode), "caption": "Common mistake"})
        last.append({"type": "tip", "title": "Common mistake", "text": _t(mtext)})
    if last:
        pages.append({"title": "Rules & common mistakes", "blocks": last})

    questions = []
    for j, qq in enumerate(sub.q):
        prompt, opts, correct, expl = qq[0], qq[1], qq[2], qq[3]
        assert len(opts) == 4, f"{sid}: question {j + 1} needs 4 options"
        assert 0 <= correct < 4
        d = {"id": f"{sid}q{j + 1}", "prompt": prompt, "options": opts, "correctIndex": correct, "explanation": _t(expl)}
        if len(qq) > 4 and qq[4]:
            d["code"] = _d(qq[4])
        questions.append(d)
    assert len(questions) >= 3, f"{sid} needs at least 3 MCQs"

    minutes = max(3, round(len(pages) * 1.2 + len(questions) * 0.5))
    return {
        "id": sid, "code": code, "title": sub.title, "summary": sub.summary,
        "estimatedMinutes": minutes, "steps": ["learn", "quiz"],
        "lesson": {"pages": pages},
        "quiz": {"questions": questions, "passPercent": 60},
    }
