# PolyMark

> **v.3.0.2** — Updated 2026-08-05

A custom syntax and color scheme for Sublime Text, compatible with PolyOS.
Highlight dates, to-dos, tags, statuses, filenames and more in plain `.md`
files.

## Quick install

Drop this `PolyMark` folder into your Sublime Text packages directory:

- Windows: `%APPDATA%\Sublime Text\Packages\`
- macOS: `~/Library/Application Support/Sublime Text/Packages/`

Access it via `Preferences > Browse Packages...`.

## Quick start

1. Open a `.md` or `.pm` file — PolyMark selects itself as the syntax.
2. `Ctrl+Shift+P` / `Cmd+Shift+P` → `UI: Select Color Scheme > PolyMark`.
3. Optional: copy the `PolyOSEditorDark` theme into Packages and set
   `"theme": "PolyOS Editor Dark.sublime-theme"` for the matching look.

No other configuration is required for the resources to work.

## What you can write

| Rule | Feature | Type this |
| ---- | ------- | --------- |
| A2a  | Arrow ligature | `->` |
| A7   | List markers | `- item`, `+ item` |
| A8   | Date header | `2026-08-05` |
| A9   | Duration range | `16-18-07 -> 16-18-12` |
| E1   | Area/project hierarchy | `@Inbox/@Work` |
| E2   | Headings | `# H1` … `###### H6` |
| E3   | To-do item (open) | `- [ ] task` |
| E4   | To-do item (done) | `- [x] task` |
| E5   | Metadata definition | `[Thoughts]: value` |
| E6   | Horizontal rule | `---` |
| E7   | Blockquote | `> text` |
| E8   | Quoted string | `"text"` |
| E9   | Comment | `/// text` |
| E10  | Bold | `**text**` |
| E11  | Italic | `*text*` |
| E12  | Custom tag | `<note>…</note>` |
| E13  | Date-time-stamp | `2025-12-18-16-08-32` |
| E14  | Email address | `name@provider.com` |
| E15  | Inline status markers | `[?]`, `[!]` |
| E16  | Single-line code marker | `$ command` |
| E17  | Task statuses | `- [/] text`, `- [-] text` |
| E18  | Filename with extension | `draft_2.docx` |
| A6a  | Keywords (extension point) | off by default |

Every rule is rendered live in `Examples.md` — open it in Sublime Text with
PolyMark active to see the full reference.

## Documentation

| Document | What it's for |
| -------- | ------------- |
| [`Examples.md`](Examples.md) | Interactive feature reference / cheat-sheet |
| [`Instructions.md`](Instructions.md) | Setup, activation, customization, troubleshooting |

## Customization

Colors and syntax knobs — file extensions, tag charset, timestamp/date/duration
formats, email and filename constraints, marker characters, and the keyword
extension point — are documented in the **PARAMETERS** sections at the top of
`polymark.sublime-syntax` and `polymark.sublime-color-scheme`. See
`Instructions.md` for a guided walkthrough.

## Files

```
├── polymark.sublime-syntax            Syntax rules (scopes every feature)
├── polymark.sublime-color-scheme      Color scheme (paints those scopes)
├── Examples.md                        Interactive feature reference
├── Instructions.md                    Setup & customization guide
└── LICENSE                            MIT License
```

## License

MIT License. See `LICENSE` for the full text.
