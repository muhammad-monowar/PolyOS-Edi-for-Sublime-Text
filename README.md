# Sublime Sync

Syncs the Sublime Text `Packages` folder across all devices (Windows and macOS).

## Layout

```
├── packages/   <- mirrors the Packages/ ROOT (this is what gets synced)
│   ├── User/               <- personal settings + keymaps (must stay FLAT)
│   ├── PolyMark/           <- custom package: PolyMark syntax + color scheme
│   ├── ProseMode/          <- custom package: prose writing color scheme
│   └── PolyOSEditorDark/   <- custom package: PolyOS Editor Dark UI theme
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
   `Packages/PolyMark`, `Packages/ProseMode` and `Packages/PolyOSEditorDark` and
   fills them with the config.
4. Restart Sublime Text. Package Control auto-installs the packages listed in
   `packages/User/Package Control.sublime-settings` (Materialize, LSP, Git,
   Transparency).
5. Set the theme to `PolyOS Editor Dark` and the color scheme to `polymark` if
   they don't apply automatically.

## Syncing after changes

Run the script after every `git pull`, or after editing files in `packages/`:

- Windows (PowerShell):
  `.\scripts\sync.ps1`
  Dry run: `.\scripts\sync.ps1 -DryRun`
- macOS (Terminal):
  `./scripts/sync.sh`
  Dry run: `./scripts/sync.sh --dry-run`

The scripts mirror each folder under `packages/` into the platform's
`Packages/` directory, copying only `*.sublime-settings`, `*.sublime-keymap`,
`*.sublime-syntax`, `*.sublime-color-scheme`, `*.sublime-theme` and `*.py`.
Theme asset folders (`assets/`) are copied recursively. The scripts are
non-destructive: existing packages (and local-only files in `Packages/User`)
are left alone.

Target paths: `%APPDATA%\Sublime Text\Packages\` on Windows,
`~/Library/Application Support/Sublime Text/Packages/` on macOS.

## Platform-specific files

- `Default (Windows).sublime-keymap` loads on Windows only.
- `Default (OSX).sublime-keymap` loads on macOS only.
- `Preferences.sublime-settings` is shared. Keep it to settings that work on
  both platforms.

## Key bindings

Both platform keymaps define the same prose-mode controls:

- `F5` — toggle distraction-free full-screen mode
- `F6` — toggle spell check, word/character count, and the status bar
- `F7` — cycle between the PolyMark and ProseMode color schemes

## Notes

- After installing/removing packages on any device, commit the updated
  `packages/User/Package Control.sublime-settings` so other devices pick up the
  change.
- If you add a new custom theme/syntax, give it its own folder under
  `packages/`, add its assets under that folder's `assets/` subdirectory, and
  point settings at `Packages/<Folder>/<file>`.
- Local-only files (session, workspaces, caches) are excluded via `.gitignore`
  and are never synced.
