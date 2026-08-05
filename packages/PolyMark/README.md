# PolyMark

> **v.3.0.2** — Updated 2026-08-05

A custom syntax and color scheme for Sublime Text, compatible with PolyOS.

## Install (standalone)

Drop this `PolyMark` folder into your Sublime Text packages directory:

- Windows: `%APPDATA%\Sublime Text\Packages\`
- macOS: `~/Library/Application Support/Sublime Text/Packages/`

Access it via `Preferences > Browse Packages...`.

No other configuration is required for the resources to work.

## Activate

- Syntax: `Set Syntax: PolyMark` (command palette), or open a `.pm` / `.md` file.
- Color scheme: `UI: Select Color Scheme > PolyMark`.

For the full experience, install the `Materialize` theme and set the theme to
`Material Vim Blackboard` (see `Instructions.md`).

## Features & customization

PolyMark recognizes the following rule families (identifiers match
`Feature Test.md`):

- **Section A (core):** date-time-stamp, area/project, bold, italic, custom
  tags, general includes (keywords/strings), markers, date header, duration
  range.
- **Section E (extensions):** headings, to-do items, metadata, horizontal
  rules, blockquotes, comments, bold/italic content, custom tagging, timestamps,
  email addresses, status markers, code markers, task statuses, filenames.

Customization knobs (file extensions, tag charset, timestamp/date/duration
formats, email TLD length, filename extension length, marker characters) are
documented at the top of `polymark.sublime-syntax` under **PARAMETERS**. The
scope → color-scheme mapping lives in that same header; the color scheme lists
every styled scope rule-by-rule.

## Files

```
├── polymark.sublime-syntax            Syntax rules
├── polymark.sublime-color-scheme      Color scheme
├── Feature Test.md                    Feature-by-feature test document
├── Instructions.md                    Detailed setup guide
└── license.txt                        Commercial EULA
```

## License

Commercial EULA. See `license.txt` for redistribution terms.
