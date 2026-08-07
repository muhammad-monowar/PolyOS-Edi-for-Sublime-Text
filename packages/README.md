# packages/ — sync source of truth

This tree mirrors the Sublime Text `Packages/` directory. `scripts/sync.sh`
(macOS) and `scripts/sync.ps1` (Windows) copy it onto each platform.

## Layout and failure isolation

| Folder | Purpose | Platform |
| ------ | ------- | -------- |
| `User/` | Personal profile: settings, keymaps, `*.py` plugins | Shared + platform-suffixed files |
| `PolyMark/` | PolyMark syntax + color scheme (v3.0.2) | Shared |
| `ProseMode/` | ProseMode color scheme (no syntax — see below) | Shared |
| `PolyOSEditorDark/` | PolyOS Editor Dark UI theme + `assets/` | Shared |
| `PolyOSPlatform/` | Per-platform preferences | Split per platform |

Rules that keep one platform's bug from breaking the other:

- **Shared files stay cross-platform.** `User/Preferences.sublime-settings`
  only contains settings valid on both macOS and Windows.
- **Platform-only settings live in `PolyOSPlatform/`**, one file per platform:
  `Preferences (Windows).sublime-settings` and
  `Preferences (OSX).sublime-settings`. Sublime loads only the file matching
  the host platform. Any key defined here must be absent from the shared
  `User/Preferences.sublime-settings` (User settings are consulted last and
  would win).
- **Keymaps self-segregate** via Sublime's native suffix mechanism:
  `User/Default (OSX).sublime-keymap` vs
  `User/Default (Windows).sublime-keymap`. A broken Windows keymap is never
  parsed on macOS.
- **`.txt` is owned by PolyMark** (`md`, `txt`, `pm`). ProseMode is a color
  scheme only and ships no syntax file, so the two packages never fight over
  the extension.
- **One canonical copy per resource.** There is exactly one
  `polymark.sublime-syntax` / `polymark.sublime-color-scheme`, in
  `PolyMark/`. Never copy these (or any resource) into `User/` — a stale
  copy there shadows the package copy and "breaks" the install.

## Per-platform settings hierarchy (Sublime)

`Packages/Default/Preferences.sublime-settings`
→ `Packages/Default/Preferences (<platform>).sublime-settings`
→ `Packages/PolyOSPlatform/Preferences (<platform>).sublime-settings`
→ `Packages/User/Preferences.sublime-settings`

So `PolyOSPlatform` platform files are consumed before `User` — the shared
`User` file must not re-declare their keys.
