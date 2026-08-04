# Sublime Sync

Syncs the Sublime Text `Packages` folder across all devices (Windows and macOS).

## Layout

```
├── packages/   <- mirrors the Packages/ ROOT (this is what gets synced)
│   ├── User/       <- personal settings + keymaps (must stay FLAT)
│   ├── PolyMark/   <- custom package: PolyMark syntax + color scheme
│   └── ProseMode/  <- custom package: prose writing color scheme
├── scripts/    <- sync.ps1 (Windows), sync.sh (macOS)
├── docs/       <- feature tests and other docs
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

## Per-device setup (one time)

1. Install Sublime Text + Package Control.
2. Clone this repo.
3. Run the sync script (see below). It creates `Packages/User`,
   `Packages/PolyMark` and `Packages/ProseMode` and fills them with the config.
4. Restart Sublime Text. Package Control auto-installs the packages listed in
   `packages/User/Package Control.sublime-settings` (Materialize, LSP, Git,
   Transparency).
5. Set the theme to `Material Vim Blackboard` and the color scheme to `polymark`
   if they don't apply automatically.

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
`*.sublime-syntax` and `*.sublime-color-scheme`. They are non-destructive:
existing packages (and local-only files in `Packages/User`) are left alone.

Target paths: `%APPDATA%\Sublime Text\Packages\` on Windows,
`~/Library/Application Support/Sublime Text/Packages/` on macOS.

## Platform-specific files

- `Default (Windows).sublime-keymap` loads on Windows only.
- `Default (OSX).sublime-keymap` loads on macOS only.
- `Preferences.sublime-settings` is shared. Keep it to settings that work on
  both platforms.

## Notes

- After installing/removing packages on any device, commit the updated
  `packages/User/Package Control.sublime-settings` so other devices pick up the
  change.
- If you add a new custom theme/syntax, give it its own folder under
  `packages/` and point settings at `Packages/<Folder>/<file>`.
- Local-only files (session, workspaces, caches) are excluded via `.gitignore`
  and are never synced.
