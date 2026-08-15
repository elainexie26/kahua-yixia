from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "kahua-yixia"
SKILL_FILE = SKILL_DIR / "SKILL.md"
AGENT_FILE = SKILL_DIR / "agents" / "openai.yaml"
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
if set(frontmatter) != {"name", "description"}:
    fail("SKILL.md frontmatter must contain only name and description")
if frontmatter["name"] != SKILL_DIR.name:
    fail("skill name must match its directory")
if not re.fullmatch(r"[a-z0-9-]{1,63}", frontmatter["name"]):
    fail("skill name must use lowercase letters, digits, and hyphens")

agent = yaml.safe_load(read_utf8(AGENT_FILE))
interface = agent.get("interface", {})
required_interface = {"display_name", "short_description", "default_prompt"}
if not required_interface.issubset(interface):
    fail("agents/openai.yaml is missing required interface fields")
if "$kahua-yixia" not in interface["default_prompt"]:
    fail("default_prompt must explicitly mention $kahua-yixia")
if not 25 <= len(interface["short_description"]) <= 64:
    fail("short_description must be 25-64 characters")

presets_text = read_utf8(PRESETS_FILE)
for label in ("现代平面插画风", "可爱动画风"):
    if label not in skill_text or label not in presets_text:
        fail(f"missing official style name: {label}")

if "references/style-presets.md" not in skill_text:
    fail("SKILL.md must link to the style presets")

print("Repository validation passed.")
