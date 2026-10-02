"""Builds app/src/main/assets/course/course.json from the curriculum files.

    python content/build_course.py            # build + verify every example
    python content/build_course.py --no-check # build only

Verification runs every lesson example that has an expected output (and every MCQ
marked RUN) through real Python and fails if the output doesn't match, so the
course never shows wrong results. Adding a level = add an L(...) to a curriculum
file. No Kotlin changes needed.
"""
import json, pathlib, subprocess, sys, tempfile, textwrap

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "curriculum"))
from dsl import build_sub, build_examples, _d  # noqa: E402

PARTS = ["part1", "part2", "part3", "part4"]
CONTENT_VERSION = 2

HARNESS = textwrap.dedent("""
    import builtins, json, sys
    _vals = iter(json.loads(sys.argv[2]))
    def _fake(prompt=""):
        v = next(_vals)
        print(prompt + v)
        return v
    builtins.input = _fake
    src = open(sys.argv[1]).read()
    exec(compile(src, "main.py", "exec"), {"__name__": "__main__"})
""")

def run(code, stdin=(), setup=""):
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d)
        (p / "h.py").write_text(HARNESS)
        if setup:
            subprocess.run([sys.executable, "-c", _d(setup)], cwd=d, check=True)
        (p / "main.py").write_text(code)
        r = subprocess.run([sys.executable, "h.py", "main.py", json.dumps(list(stdin))],
                           cwd=d, capture_output=True, text=True, timeout=10)
        out = r.stdout.rstrip("\n")
        if r.returncode != 0:
            last = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "?"
            out = (out + "\n" + last) if out else last
        return out

def main():
    check = "--no-check" not in sys.argv
    levels, problems, n_sub, n_q = [], [], 0, 0
    for part in PARTS:
        try:
            mod = __import__(part)
        except ModuleNotFoundError:
            continue
        for lv in mod.LEVELS:
            num = len(levels) + 1
            lid = f"l{num}"
            subs = []
            for i, sub in enumerate(lv["subs"]):
                sid, code = f"{lid}s{i + 1}", f"{num}.{i + 1}"
                subs.append(build_sub(sub, sid, code))
                n_sub += 1; n_q += len(sub.q)
                if not check:
                    continue
                for j, (c, out, opts) in enumerate(build_examples(sub)):
                    if out is None or opts.get("nocheck"):
                        continue
                    got = run(c, opts.get("stdin", ()), opts.get("setup", ""))
                    if got != out:
                        problems.append(f"{code} {sub.title} ex{j + 1}:\n  expected: {out!r}\n  got:      {got!r}")
                for j, qq in enumerate(sub.q):
                    if len(qq) > 5 and qq[5]:
                        got = run(_d(qq[4]))
                        if got != qq[1][qq[2]]:
                            problems.append(f"{code} {sub.title} Q{j + 1}: correct option {qq[1][qq[2]]!r} but code prints {got!r}")
            levels.append({"id": lid, "number": num, "title": lv["title"], "description": lv["description"], "subLevels": subs})

    course = {"id": "python-complete", "title": "Python: Zero to Advanced", "schemaVersion": 1,
              "contentVersion": CONTENT_VERSION, "levels": levels}
    out = ROOT.parent / "app/src/main/assets/course/course.json"
    out.write_text(json.dumps(course, indent=1, ensure_ascii=False))
    print(f"{len(levels)} levels, {n_sub} sub-levels, {n_q} MCQs -> {out}")
    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        print("\n".join(problems))
        sys.exit(1)
    print("All examples verified." if check else "(verification skipped)")

if __name__ == "__main__":
    main()
