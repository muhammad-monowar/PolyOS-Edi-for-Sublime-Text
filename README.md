# Sublime Sync

Syncs the Sublime Text `Packages` folder across all devices (Windows and macOS).

## Layout

```
├── packages/   <- mirrors the Packages/ ROOT (this is what gets synced)
│   ├── User/               <- personal settings + keymaps (must stay FLAT)
│   ├── PolyMark/           <- custom package: PolyMark syntax + color scheme
│   ├── ProseMode/          <- custom package: prose writing color scheme
│   ├── PolyOSEditorDark/   <- custom package: PolyOS Editor Dark UI theme
│   └── PolyOSPlatform/     <- per-platform preferences (Preferences (OSX|Windows).sublime-settings)
├── scripts/    <- sync.ps1 (Windows), sync.sh (macOS)
└── archive/    <- old exports, not synced
```

Why this shape:

- `Packages/User` only loads `.sublime-settings` files from its **root**, so that
  folder stays flat. Keymaps and per-syntax settings also live there.
- Syntaxes, color schemes, and themes belong in their own **custom package
  folders** under `Packages/` (e.g. `Packages/PolyMark/`). This groups them by
  product and keeps the shared `User` folder clean.
- Settings reference packages by resource path, e.g.
  `Packages/PolyMark/polymark.sublime-color-scheme`.

## Standalone packages

`PolyMark`, `ProseMode`, and `PolyOSEditorDark` are standalone Sublime Text
packages:

- Each folder is a valid unmanaged package — drop it into any `Packages/`
  directory and its resources work with zero other configuration.
- They never reference `Packages/User`, the profile, or each other. The
  coupling is one-directional: `Packages/User` (the profile) activates them,
  but the packages are profile-agnostic. You can swap or replace the profile
  without touching them.
- Activation lives only in `packages/User/`; the packages do not ship
  auto-applying preferences.

## Per-device setup (one time)

1. Install Sublime Text + Package Control.
2. Clone this repo.
3. Run the sync script (see below). It creates `Packages/User`,
   `Packages/PolyMark`, `Packages/ProseMode`, `Packages/PolyOSEditorDark` and
   `Packages/PolyOSPlatform` and fills them with the config.
4. Restart Sublime Text. Package Control auto-installs the packages listed in
   `packages/User/Package Control.sublime-settings` (LSP, Git, Transparency).
5. Set the theme to `PolyOS Editor Dark` and the color scheme to `polymark` if
   they don't apply automatically.

### macOS notes

- The color scheme uses `JetBrains Mono` as its font (`font_face` in
  `Preferences.sublime-settings`). Install JetBrains Mono on the Mac too, or
  Sublime Text silently falls back to the platform font and the look differs.
- The F5/F6/F7 shortcuts require holding the `fn` key unless you enable
  "Use F1, F2, etc. keys as standard function keys" in System Settings →
  Keyboard → Keyboard shortcuts → Function Keys.

## Syncing after changes

Run the script after every `git pull`, or after editing files in `packages/`:

- Windows (PowerShell):
  `.\scripts\sync.ps1`
  Dry run: `.\scripts\sync.ps1 -DryRun`
- macOS (Terminal):
  `./scripts/sync.sh`
  Dry run: `./scripts/sync.sh --dry-run`

  The script runs under both `bash` and `zsh`. If you get `zsh: permission
  denied`, run `chmod +x scripts/sync.sh` once (or use `bash scripts/sync.sh`).

The scripts mirror each folder under `packages/` into the platform's
`Packages/` directory, copying only `*.sublime-settings`, `*.sublime-keymap`,
`*.sublime-syntax`, `*.sublime-color-scheme`, `*.sublime-theme`,
`*.sublime-commands` and `*.py`.
Subfolders `assets/` and `themes/` are copied recursively. The scripts are
non-destructive: existing packages (and local-only files in `Packages/User`)
are left alone.

Target paths: `%APPDATA%\Sublime Text\Packages\` on Windows,
`~/Library/Application Support/Sublime Text/Packages/` on macOS, and
`~/.config/sublime-text/Packages/` on Linux.

## Platform-specific files

- `Default (Windows).sublime-keymap` loads on Windows only.
- `Default (OSX).sublime-keymap` loads on macOS only.
- `Preferences.sublime-settings` is shared. Keep it to settings that work on
  both platforms.
- Platform-only preferences live in `packages/PolyOSPlatform/`:
  `Preferences (OSX).sublime-settings` and
  `Preferences (Windows).sublime-settings`. Sublime loads only the file for
  the host platform. A key defined in one of these must NOT also be defined in
  the shared `User/Preferences.sublime-settings` (User is consulted last and
  would win). Currently Windows adds `directwrite`/`subpixel_antialias` font
  flags and `hardware_acceleration: "opengl"`; macOS needs no overrides.

This split isolates failure points: a malformed Windows-only file is never
parsed on macOS (and vice versa), and the shared files stay cross-platform.

### `.txt` ownership

`.txt` is claimed by PolyMark (`md`, `txt`, `pm`), matching the PolyMark
README ("because PolyMark auto-selects for `.txt`..."). ProseMode is a color
scheme only and ships no syntax file, so the two packages never fight over the
extension. If you want PolyMark to leave plain-text files alone, delete the
`txt` line from `packages/PolyMark/polymark.sublime-syntax`.

## Key bindings

Both platform keymaps define the same prose-mode controls:

- `F5` — toggle distraction-free mode (hides the menu bar; restores its previous visibility on exit)
- `F6` — toggle spell check, word/character count, the status bar, and the menu bar
- `F7` — cycle through the PolyMark color scheme variations and ProseMode

## PolyMark color scheme variations

All PolyMark theme variations live in `packages/PolyMark/themes/`. The
canonical base scheme (`polymark.sublime-color-scheme`) is never duplicated.

- **Add your own:** drop a `<name>.sublime-color-scheme` into
  `packages/PolyMark/themes/`, then run the sync script. Recommended pattern:
  `"extends": "Packages/PolyMark/polymark.sublime-color-scheme"` plus a
  `globals` block overriding `accent`, the kind hooks, `background`,
  `foreground`, etc. — the base rules inherit automatically and the UI re-tints.
- **Select a variation:** command palette → `PolyMark: Select Color Scheme...`
  (applies to the active view) or `F7` to cycle through base → variations →
  ProseMode.
- See `packages/PolyMark/themes/README.md` for details.

## Notes

- After installing/removing packages on any device, commit the updated
  `packages/User/Package Control.sublime-settings` so other devices pick up the
  change.
- If you add a new custom theme/syntax, give it its own folder under
  `packages/`, add its assets under that folder's `assets/` subdirectory, and
  point settings at `Packages/<Folder>/<file>`.
- Local-only files (session, workspaces, caches) are excluded via `.gitignore`
  and are never synced.
