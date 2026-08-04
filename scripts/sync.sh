#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/user"
TARGET="$HOME/Library/Application Support/Sublime Text/Packages/User"

if [[ ! -d "$SRC" ]]; then
    echo "Source folder not found: $SRC" >&2
    exit 1
fi

mkdir -p "$TARGET"

mapfile -t FILES < <(find "$SRC" -maxdepth 1 -type f \( \
    -name '*.sublime-settings' -o \
    -name '*.sublime-keymap' -o \
    -name '*.sublime-syntax' -o \
    -name '*.sublime-color-scheme' \
\) -print)

echo "Syncing ${#FILES[@]} file(s) to: $TARGET"
if $DRY_RUN; then
    echo "  [DRY RUN]"
fi

for file in "${FILES[@]}"; do
    echo "  $(basename "$file")"
    if ! $DRY_RUN; then
        cp -f "$file" "$TARGET/"
    fi
done

if $DRY_RUN; then
    echo "Dry run complete. Re-run without --dry-run to copy."
fi
