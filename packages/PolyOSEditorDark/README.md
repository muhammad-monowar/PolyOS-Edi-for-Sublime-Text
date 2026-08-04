# PolyOS Editor Dark

A decoupled, self-contained UI theme for the PolyOS workspace. Terminal / CRT
"Matrix" aesthetic: deep charcoal-green chrome with a phosphor mint accent.

Derived from [Material Theme](https://github.com/equinusocio/material-theme)
(MIT). The theme is fully self-contained — it vendors its own assets and does
not require Materialize to be installed.

## Palette

| Role      | Hex       | Description                 |
| --------- | --------- | --------------------------- |
| Background| `#0E1410` | Deep charcoal green         |
| Raised    | `#16201A` | Hover / raised surfaces     |
| Foreground| `#E8EAE6` | Primary UI text             |
| Secondary | `#6A7B70` | Muted green-gray            |
| Accent    | `#72EFA6` | Phosphor mint highlight     |

## Install (standalone)

Drop this `PolyOSEditorDark` folder into your Sublime Text packages directory:

- Windows: `%APPDATA%\Sublime Text\Packages\`
- macOS: `~/Library/Application Support/Sublime Text/Packages/`

Access it via `Preferences > Browse Packages...`.

## Activate

Set the theme in `Preferences.sublime-settings`:

```json
"theme": "PolyOS Editor Dark.sublime-theme"
```

## Customization

**Theme palette** — every surface color is a variable in the top-level
`"variables"` block of `PolyOS Editor Dark.sublime-theme`. Edit one value to
re-tint that surface everywhere it is used:

```json
"variables": {
    "--polyos-background":        "#0E1410",
    "--polyos-background-raised": "#16201A",
    "--polyos-foreground":        "#E8EAE6",
    "--polyos-secondary":         "#6A7B70",
    "--polyos-accent":            "#72EFA6",
    "--polyos-border":            "#16201A"
}
```

**Accent follows the color scheme** — rules use `var(--accent)`, which resolves
to the active color scheme's `globals.accent`. Both `PolyMark` and `ProseMode`
define `"accent": "#72EFA6"` (plus the eight kind colors), so toggling between
them keeps the UI chrome in sync. If a scheme does not define an accent, the
theme's own `--accent` variable is used.

**UI toggles** — the original Material settings still work and control the same
things:

- `material_theme_contrast_mode` — deeper, higher-contrast surfaces
- `material_theme_small_tab` / `material_theme_bold_tab` — tab sizing / weight
- `material_theme_title_bar` — OS-style title bar
- `overlay_scroll_bars` — slim overlay scrollbars
- `bold_folder_labels`, `show_tab_close_buttons`, and other `material_theme_*`
  switches from Material

## Files

```
├── PolyOS Editor Dark.sublime-theme    Theme definition (rules + variables)
├── assets/
│   ├── vim blackboard/                 Base chrome textures (29 PNGs)
│   └── commons/                        Shared UI textures (45 PNGs)
└── README.md
```

## License

The theme is a derivative of Material Theme (MIT License). See
https://github.com/equinusocio/material-theme for the original license.
