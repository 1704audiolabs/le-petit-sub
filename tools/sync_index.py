"""docs/index.md = README.md with the links rewritten for the website, plus the home page's cover.

    python tools/sync_index.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/1704audiolabs/le-petit-sub"
SITE = "https://1704audiolabs.github.io/le-petit-sub/"
HUB = "https://1704audiolabs.github.io/"

FRONT = """---
template: home.html
cover_image: assets/3d/with-le-petit.png
cover_alt: 3D model of the sub between a Le Petit pair
cover_kicker: 02 · Le Petit Sub
cover_title: "Le Petit's bigger twin: two opposed 10″ drivers, built from <i>one sheet of OSB.</i>"
cover_links:
  - [3D model, 3d-model/]
  - [Build guide, 01-build/]
  - [Building plan, building-plan/]
description: Le Petit's bigger twin — a sealed subwoofer with two opposed 10″ drivers from one sheet of OSB.
---

"""
TEASER = """<div class="oab-onesheet" markdown>
[![The one-sheet: Le Petit Sub on one A4 page](assets/one-sheet.png)](one-sheet.md)
<div markdown>
<span class="oab-label">One-sheet · A4</span>

**The whole project on one page** — what was calculated, what was chosen and how to build it.
[Open the one-sheet →](one-sheet.md)
</div>
</div>"""

s = (ROOT / "README.md").read_text()
head, sep, rest = s.partition("<a href=")
assert sep and "one-sheet.png" in rest.split("\n", 1)[0], "README: one-sheet teaser line not found"
s = head.replace(f"Also readable as a website, with the interactive 3D model: **{SITE}** · the whole project on one\n"
                 f"page: **[one-sheet]({SITE}one-sheet/)** · part of **[1704 Audio Labs]({HUB})** — Measure & Taste",
                 f"All files, drawings and scripts: **{REPO}** ·\npart of **[1704 Audio Labs]({HUB})** — Measure & Taste") + TEASER + "\n" + rest.split("\n", 1)[1]
# the cover shows the 3D still already
s = s.replace(f"[![The sub between a Le Petit pair: same front, same OSB, the drivers in the sides]"
              f"(docs/assets/3d/with-le-petit.png)]({SITE}3d-model/)\n\n", "")
s = s.replace(f"({SITE}3d-model/)", "(3d-model.md)")
s = s.replace("](docs/", "](")
s = s.replace("](tools/", f"]({REPO}/blob/main/tools/")
(ROOT / "docs" / "index.md").write_text(FRONT + s)
print("wrote docs/index.md")
