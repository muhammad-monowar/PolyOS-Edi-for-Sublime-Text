#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
fi

if [ -n "${BASH_SOURCE:-}" ]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
else
    SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
fi
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC="$REPO_ROOT/packages"
case "$(uname -s)" in
    Linux*)   TARGET="$HOME/.config/sublime-text/Packages" ;;
    Darwin*)  TARGET="$HOME/Library/Application Support/Sublime Text/Packages" ;;
    *)        TARGET="$HOME/Library/Application Support/Sublime Text/Packages" ;;
esac

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

    FILES=()
    while IFS= read -r file; do
        FILES+=("$file")
    done < <(find "$pkg_dir" -maxdepth 1 -type f \( \
        -name '*.sublime-settings' -o \
        -name '*.sublime-keymap' -o \
        -name '*.sublime-syntax' -o \
        -name '*.sublime-color-scheme' -o \
        -name '*.sublime-theme' -o \
        -name '*.sublime-commands' -o \
        -name '*.py' \
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

    if [[ -d "$pkg_dir/assets" ]]; then
        echo "    assets/"
        if ! $DRY_RUN; then
            mkdir -p "$pkg_target/assets"
            cp -Rf "$pkg_dir/assets/." "$pkg_target/assets/"
        fi
    fi

    if [[ -d "$pkg_dir/themes" ]]; then
        echo "    themes/"
        if ! $DRY_RUN; then
            mkdir -p "$pkg_target/themes"
            cp -Rf "$pkg_dir/themes/." "$pkg_target/themes/"
        fi
    fi
done

if $DRY_RUN; then
    echo "Dry run complete. Re-run without --dry-run to copy."
fi
