#!/usr/bin/env bash
# tokin-ads-advisor — one-shot installer
# Installs the skill globally. Idempotent: safe to re-run.
#
# The skill expects these two data sources to exist on the machine:
#   1. The Tokin Chews ads pipeline at a path discoverable by the skill.
#      Default path: ~/Documents/AI Work Folder/Projects/Tokin Jew/tokin ads/
#      You can override by setting TOKIN_ADS_DIR before running.
#   2. The tokin-jew-db skill (already installed via install.sh of that package)
#      for product/sales/customer queries against the Neon DB.
#
# If either is missing the skill still works (partial answers). You'll see a
# helpful warning in Claude's response.

set -euo pipefail

SKILL_NAME="tokin-ads-advisor"
SKILLS_DIR="$HOME/.claude/skills"
DEFAULT_ADS_DIR="$HOME/Documents/AI Work Folder/Projects/Tokin Jew/tokin ads"
ADS_DIR="${TOKIN_ADS_DIR:-$DEFAULT_ADS_DIR}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "==> Installing skill → $SKILLS_DIR/$SKILL_NAME"
mkdir -p "$SKILLS_DIR"
if [ "$SCRIPT_DIR" != "$SKILLS_DIR/$SKILL_NAME" ]; then
  rm -rf "$SKILLS_DIR/$SKILL_NAME"
  cp -R "$SCRIPT_DIR" "$SKILLS_DIR/$SKILL_NAME"
fi
echo "    ok."

echo ""
echo "==> Checking data sources"
if [ -d "$ADS_DIR" ] && [ -f "$ADS_DIR/data/creative_enriched.json" ]; then
  echo "    ads pipeline: OK ($ADS_DIR)"
else
  echo "    ⚠ ads pipeline not found at: $ADS_DIR"
  echo "      Either clone the tokin-ads-dashboard repo or set TOKIN_ADS_DIR to your copy."
  echo "      The skill will still work on public dashboard data but lose some context."
fi

if [ -d "$SKILLS_DIR/tokin-jew-db" ]; then
  echo "    tokin-jew-db skill: OK"
else
  echo "    ⚠ tokin-jew-db skill not installed."
  echo "      Install it separately to unlock live Shopify product/sales queries."
fi

echo ""
echo "✅ Installed."
echo ""
echo "Next steps:"
echo "  1. Restart Claude Desktop (or the CLI) so the skill is discovered."
echo "  2. Ask any ads question — e.g. 'what hook works best for a Passover ad?'"
echo ""
echo "Install companion:"
echo "  • tokin-jew-db skill   → unlocks live Shopify/Klaviyo/Meta-daily data"
echo ""
echo "To uninstall: rm -rf \"$SKILLS_DIR/$SKILL_NAME\""
