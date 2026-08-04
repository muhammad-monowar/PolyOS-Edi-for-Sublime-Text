# Sublime Sync

Syncs the Sublime Text `Packages/User` folder across all devices (Windows and macOS).

## Layout

```
├── user/      <- FLAT mirror of Packages/User (this is what gets synced)
├── scripts/   <- sync.ps1 (Windows), sync.sh (macOS)
├── docs/      <- PolyMark docs, feature test, license
└── archive/   <- old exports, not synced
```

The `user/` folder must stay flat: Sublime Text only loads `.sublime-settings`
files from the root of `Packages/User`, not from subfolders.

## Per-device setup (one time)

1. Install Sublime Text + Package Control.
2. Clone this repo:
   - Windows: `git clone git@github.com:mmmonowar/sublime-sync.git`
   - macOS: `git clone git@github.com:mmmonowar/sublime-sync.git`
3. Run the sync script (see below). This copies the config files into
   `Packages/User`.
4. Restart Sublime Text. Package Control auto-installs the packages listed in
   `user/Package Control.sublime-settings` (Materialize, LSP, Git, Transparency).
5. Set the theme to `Material Vim Blackboard` and the color scheme to `polymark`
   if they don't apply automatically.

## Syncing after changes

Run the script after every `git pull`, or after editing files in `user/`:

- Windows (PowerShell):
  `.\scripts\sync.ps1`
  Dry run: `.\scripts\sync.ps1 -DryRun`
- macOS (Terminal):
  `./scripts/sync.sh`
  Dry run: `./scripts/sync.sh --dry-run`

Scripts copy only `*.sublime-settings`, `*.sublime-keymap`, `*.sublime-syntax`
and `*.sublime-color-scheme` from `user/` into the platform's `Packages/User`:
`%APPDATA%\Sublime Text\Packages\User\` on Windows,
`~/Library/Application Support/Sublime Text/Packages/User/` on macOS.

## Platform-specific files

- `Default (Windows).sublime-keymap` loads on Windows only.
- `Default (OSX).sublime-keymap` loads on macOS only.
- `Preferences.sublime-settings` is shared. Keep it to settings that work on
  both platforms.

## Notes

- After installing/removing packages on any device, commit the updated
  `user/Package Control.sublime-settings` so other devices pick up the change.
- Local-only files (session, workspaces, caches) are excluded via `.gitignore`
  and are never synced.
