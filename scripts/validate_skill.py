from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "kahua-yixia"
SKILL_FILE = SKILL_DIR / "SKILL.md"
PRESETS_FILE = SKILL_DIR / "references" / "style-presets.md"


def fail(message: str) -> None:
    raise SystemExit(f"Validation failed: {message}")


def read_utf8(path: Path) -> str:
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


skill_text = read_utf8(SKILL_FILE)
match = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
if not match:
    fail("SKILL.md must start with YAML frontmatter")

frontmatter = yaml.safe_load(match.group(1))
if not isinstance(frontmatter, dict) or set(frontmatter) != {"name", "description"}:
    fail("SKILL.md frontmatter must contain only name and description")
if frontmatter["name"] != SKILL_DIR.name:
    fail("skill name must match its directory")
if not re.fullmatch(r"[a-z0-9-]{1,63}", frontmatter["name"]):
    fail("skill name must use lowercase letters, digits, and hyphens")
if not isinstance(frontmatter["description"], str) or not frontmatter["description"].strip():
    fail("description must be a non-empty string")

presets_text = read_utf8(PRESETS_FILE)
for label in ("现代平面插画", "可爱轻卡通"):
    if label not in skill_text or label not in presets_text:
        fail(f"missing consistent style name: {label}")

if "references/style-presets.md" not in skill_text:
    fail("SKILL.md must link to the bundled style presets")

for platform_term in ("Codex", "OpenAI", "image_gen", "view_image"):
    if platform_term in skill_text or platform_term in presets_text:
        fail(f"platform-specific term is not allowed in the release skill: {platform_term}")

files = sorted(
    path.relative_to(SKILL_DIR).as_posix()
    for path in SKILL_DIR.rglob("*")
    if path.is_file()
)
expected_files = ["SKILL.md", "references/style-presets.md"]
if files != expected_files:
    fail(f"release package must contain only {expected_files}; found {files}")

print("Skill validation passed.")
