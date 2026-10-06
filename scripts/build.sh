#!/usr/bin/env bash
# Builds dist/ artefacts from skills/sandfield-design:
#   sandfield-design.zip  - upload to Claude.ai / Desktop (Settings → Capabilities → Skills)
#   sandfield-design.md   - single file to paste or attach in any other AI tool
#   reader.html           - the whole skill on one readable page (if pandoc is installed)
set -euo pipefail
cd "$(dirname "$0")/.."
SKILL=skills/sandfield-design
mkdir -p dist
rm -f dist/sandfield-design.zip
(cd skills && zip -qr ../dist/sandfield-design.zip sandfield-design -x '*.DS_Store')
{
  # SKILL.md without its YAML frontmatter
  awk 'NR==1 && /^---$/ {fm=1; next} fm && /^---$/ {fm=0; next} !fm' "$SKILL/SKILL.md"
  for f in philosophy rules checklist examples; do
    printf '\n\n---\n\n'; cat "$SKILL/references/$f.md"
  done
  printf '\n\n---\n\n'; cat "$SKILL/themes/README.md"
} > dist/sandfield-design.md
echo "Built dist/sandfield-design.zip and dist/sandfield-design.md"

# Optional: one-page reader of the skill (needs pandoc)
if command -v pandoc >/dev/null; then python3 scripts/reader.py; else echo "Skipped dist/reader.html (pandoc not installed)"; fi
