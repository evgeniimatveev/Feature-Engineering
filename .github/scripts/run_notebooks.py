"""Execute every course notebook top to bottom and report pass/fail.

Each notebook runs with its own folder as working directory (like Jupyter does),
so the relative path ../data/... resolves. Plots go to a non-interactive backend.
"""
import glob
import os
import sys
import time
import warnings

import nbformat
from nbclient import NotebookClient

warnings.filterwarnings("ignore")
os.environ["MPLBACKEND"] = "Agg"

TIMEOUT = 600
notebooks = sorted(glob.glob("0*/*.ipynb"))
rows = []

for path in notebooks:
    started = time.time()
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=TIMEOUT, kernel_name="python3",
                            resources={"metadata": {"path": os.path.dirname(path)}})
    error = ""
    try:
        client.execute()
        status = "passed"
    except Exception as exc:  # noqa: BLE001 - report any failure
        status = "FAILED"
        lines = [l for l in str(exc).splitlines() if l.strip()]
        error = lines[-1][:300] if lines else type(exc).__name__
    secs = time.time() - started
    print(f"{status.upper():7s} {path} ({secs:.0f}s)" + (f"\n        {error}" if error else ""), flush=True)
    rows.append((path, status, secs, error))

failed = sum(1 for r in rows if r[1] != "passed")
print(f"\nSummary: {len(rows) - failed} passed, {failed} failed, {len(rows)} total")

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    icon = {"passed": "✅", "FAILED": "❌"}
    md = ["## Notebook run", "", f"**{len(rows) - failed} passed · {failed} failed** (of {len(rows)} notebooks)", "",
          "| Notebook | Result | Seconds |", "|---|:-:|--:|"]
    md += [f"| `{p}` | {icon[s]} {s} | {t:.0f} |" for p, s, t, _ in rows]
    errs = [(p, e) for p, s, _, e in rows if e]
    if errs:
        md += ["", "### Errors", ""] + [f"- `{p}`: {e}" for p, e in errs]
    with open(summary, "w", encoding="utf-8") as fh:
        fh.write("\n".join(md) + "\n")

sys.exit(1 if failed else 0)
