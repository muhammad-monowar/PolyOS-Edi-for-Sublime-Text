# PolyOS Editor

A writing environment for Sublime Text: the PolyMark syntax and color scheme,
PolyMark theme variations, a ProseMode color scheme, and the PolyOS Editor Dark
UI theme — installed as one Package Control package.

## Install

1. Run `Preferences → Package Control → Add Repository` and paste:

   ```
   https://raw.githubusercontent.com/muhammad-monowar/PolyOS-Edi-for-Sublime-Text/main/repository.json
   ```

2. Run `Preferences → Package Control → Install Package` and choose
   **PolyOS Editor**.

Package Control installs the theme, every color scheme, the syntax, the
keybindings and the dependencies (Git, LSP, Transparency), then offers upgrades
on its own.

On first start a dialog asks whether to apply the PolyOS profile. Answer yes to
set the theme, color scheme, default syntax and font size; answer no and nothing
changes. The prompt does not come back on its own — re-enable it from
`Preferences → Package Settings → PolyOS Editor → Prompt on next start`, or
apply the profile later with `Activate profile`.

## Your settings are never overwritten

Sublime merges same-named `.sublime-settings` and `.sublime-keymap` files across
all packages and reads `Packages/User` last. The settings shipped here are
therefore defaults: if you have already set `font_face`, `font_options`,
`caret_style` or any other key in your own preferences, your value wins and this
package is ignored for that key.

The four settings that visibly change the editor — `theme`, `color_scheme`,
`default_syntax`, `font_size` — are deliberately left out of the shipped
preferences. `activate_profile.py` applies them, and only for keys still holding
Sublime's stock value. A setting you have already changed is skipped even if you
click "Apply".

Upgrading never touches your settings. The only file this package writes to
`Packages/User` is `PolyOSEditor.sublime-settings`, which holds the single key
`polyos_activate` used to remember your answer.

There is no sync script and no background re-writer: the packaged preferences
*are* the default layer, which is why nothing needs to copy them into
`Packages/User` on every launch.

## What's in the package

| File | Purpose |
| ---- | ------- |
| `polymark.sublime-syntax` | PolyMark syntax, claims `.md`, `.txt`, `.pm` |
| `polymark.sublime-color-scheme` | PolyMark colors, the base scheme |
| `themes/*.sublime-color-scheme` | PolyMark variations, see `themes/README.md` |
| `color_schemes.py` | F7 cycling and the `PolyMark: Select Color Scheme...` command |
| `PolyMark.sublime-commands` | palette entry for the scheme picker |
| `ProseMode.sublime-color-scheme` | monochrome ProseMode colors |
| `PolyOS Editor Dark.sublime-theme` | UI theme, `assets/` holds its textures |
| `Preferences.sublime-settings` | cross-platform defaults |
| `Preferences (OSX).sublime-settings` | macOS-only keys (currently none) |
| `Preferences (Windows).sublime-settings` | Windows font rendering + OpenGL |
| `Default (OSX).sublime-keymap` | F5/F6/F7 on macOS |
| `Default (Windows).sublime-keymap` | F5/F6/F7 on Windows |
| `Distraction Free.sublime-settings` | F5 typography and layout |
| `prose_toggles.py` | the F5/F6/F7 commands |
| `activate_profile.py` | first-run prompt and the profile commands |
| `syntax_test_polymark.txt` | syntax tests, run from the Build With syntax tests |

Platform files use Sublime's native suffix mechanism, so a `Preferences (Windows)`
file is parsed only on Windows and a malformed value never reaches macOS. A key
defined in a platform file must not also be defined in the shared
`Preferences.sublime-settings`, because `Packages/User` is consulted last.

### `.txt` ownership

`.txt` is claimed by PolyMark (`md`, `txt`, `pm`). ProseMode ships no syntax
file, only a color scheme, so the two never fight over the extension. To leave
plain-text files alone, delete the `txt` line from `file_extensions` in
`polymark.sublime-syntax`.

## Key bindings

Defined in both platform keymaps:

- `F5` — toggle distraction-free mode (hides the menu bar, restores it on exit)
- `F6` — toggle spell check, word/character count, the status bar, and the menu
- `F7` — cycle through the PolyMark schemes and ProseMode
- `Tab` — accept an autocomplete suggestion after `@`

On macOS the F-keys may require holding `fn` unless "Use F1, F2, etc. keys as
standard function keys" is enabled in System Settings → Keyboard.

Centering in distraction-free mode uses Sublime's native `draw_centered`.

## Dependencies

`font_face` is `JetBrains Mono`. Without it installed, Sublime silently falls
back to the platform font and the look differs.

## Development

The repository root is the package, which is what Package Control's tag-based
GitHub hosting requires — the root of the package must be the root of the repo.
Releases are tags prefixed `polyos-editor-`:

```sh
git tag polyos-editor-1.0.0
git push origin polyos-editor-1.0.0
```

`repository.json` matches that prefix, so any other tag in the repo is invisible
to the release resolver.

When you add a resource, give it a `Packages/PolyOS-Edi-for-Sublime-Text/…`
resource path, matching the repo folder name exactly. Theme textures are
referenced as `PolyOS-Edi-for-Sublime-Text/assets/…` — no `Packages/` prefix,
which Sublime rejects for `layer0.texture`.

## License

MIT. See `LICENSE`. PolyOS Editor Dark is derived from Material Theme, MIT
licensed.