#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/packages"
TARGET="$HOME/Library/Application Support/Sublime Text/Packages"

if [[ ! -d "$SRC" ]]; then
    echo "Source folder not found: $SRC" >&2
    exit 1
fi

mkdir -p "$TARGET"

echo "Syncing packages to: $TARGET"
if $DRY_RUN; then
    echo "  [DRY RUN]"
fi

for pkg_dir in "$SRC"/*/; do
    [[ -d "$pkg_dir" ]] || continue
    pkg_name="$(basename "$pkg_dir")"
    pkg_target="$TARGET/$pkg_name"

    mapfile -t FILES < <(find "$pkg_dir" -maxdepth 1 -type f \( \
        -name '*.sublime-settings' -o \
        -name '*.sublime-keymap' -o \
        -name '*.sublime-syntax' -o \
        -name '*.sublime-color-scheme' \
    \) -print)

    [[ ${#FILES[@]} -eq 0 ]] && continue

    mkdir -p "$pkg_target"
    echo "  [$pkg_name] ${#FILES[@]} file(s)"
    for file in "${FILES[@]}"; do
        echo "    $(basename "$file")"
        if ! $DRY_RUN; then
            cp -f "$file" "$pkg_target/"
        fi
    done
done

if $DRY_RUN; then
    echo "Dry run complete. Re-run without --dry-run to copy."
fi
