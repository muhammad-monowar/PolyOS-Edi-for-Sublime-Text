---
Author: Muhammad Mustafa Monowar
Updated: 2026-08-06
Target: Sublime-Text
Version: v.3.1.0
---

# PolyMark — Setup & Customization Guide

PolyMark is a color scheme and syntax highlighting rule set for Sublime Text,
part of the PolyOS ecosystem. The syntax file (`polymark.sublime-syntax`)
classifies text into scopes; the color scheme (`polymark.sublime-color-scheme`)
paints those scopes. Together they highlight Markdown-flavored notes that mix
plain prose with dates, to-dos, tags, statuses, filenames and more.

For a visual tour of every feature, open `Examples.md` with PolyMark active.
This guide covers setup, activation and customization.

## What's in the box

| File                          | Purpose                                        |
| ----------------------------- | ---------------------------------------------- |
| `polymark.sublime-syntax`     | Syntax rules — which patterns get scopes       |
| `polymark.sublime-color-scheme` | Colors — one rule per feature, labelled A#/E# |
| `Examples.md`                 | Interactive feature reference / verification   |
| `Instructions.md`             | This guide                                     |
| `README.md`                   | Landing page and quick install                 |
| `LICENSE`                     | MIT License                                    |

## Requirements

- Sublime Text 4.
- Files opened with the `.md`, `.txt` or `.pm` extension. PolyMark selects
  itself for all three (see *Customizing the syntax* → *File extensions*).
- Optional, for the full look: the `JetBrains Mono` font. Its `dlig` ligatures
  turn `->` into a true arrow.

## Install

1. Open `Preferences > Browse Packages...` to find your packages directory:
   - Windows: `%APPDATA%\Sublime Text\Packages\`
   - macOS: `~/Library/Application Support/Sublime Text/Packages/`
2. Copy the whole `PolyMark` folder into that directory, so the layout is:
   `Packages/PolyMark/polymark.sublime-syntax`
3. Restart Sublime Text (or let it pick the files up automatically).

No other configuration is required for the syntax and color scheme to work.

## Activate

1. **Syntax** — `Set Syntax: PolyMark` from the command palette
   (`Ctrl+Shift+P` / `Cmd+Shift+P`), or simply open a `.md` / `.txt` / `.pm`
   file.
2. **Color scheme** — `UI: Select Color Scheme > PolyMark`.

### Recommended preferences

To reproduce the reference setup, set the following in your user preferences:

```json
{
  "font_size": 14,
  "font_face": "JetBrains Mono",
  "font_options": ["dlig", "calt", "directwrite", "subpixel_antialias"],
  "color_scheme": "Packages/PolyMark/polymark.sublime-color-scheme",
  "default_syntax": "Packages/PolyMark/polymark.sublime-syntax"
}
```

`dlig` is what renders the `->` arrow ligature.

## Feature tour

Every rule below is demonstrated live in `Examples.md`. The A#/E# labels are
the same ones used in the comments of both resource files.

| Rule | Feature | Type this | You'll see |
| ---- | ------- | --------- | ---------- |
| A2a | Arrow ligature | `->` | default foreground (unassigned) |
| A7 | List markers | `- item`, `+ item` | bold coral `-` marker, bold cyanish `+` marker |
| A8 | Date header | `2026-08-05` | school-bus yellow |
| A9 | Duration range | `16-18-07 -> 16-18-12` | electric cyan |
| E1 | Area/project | `@Inbox/@Work` | electric blue on rich black |
| E2 | Headings | `# H1` … `###### H6` | sky-blue heading lines |
| E3 | To-do (open) | `- [ ] task` | yellow `[ ]` box |
| E4 | To-do (done) | `- [x] task` | aquamarine `[x]` box |
| E5 | Metadata key | `[Thoughts]: value` | aquamarine key |
| E6 | Horizontal rule | `---` | tropical indigo |
| E7 | Blockquote | `> text` | aquamarine on gunmetal |
| E8 | Quoted string | `"text"` | default foreground (unassigned) |
| E9 | Comment | `/// text` | ash gray, italic |
| E10 | Bold | `**text**` | bold pale green |
| E11 | Italic | `*text*` | italic pale green |
| E12 | Custom tag | `<note>…</note>` | soft purple on rich black |
| E13 | Timestamp | `2025-12-18-16-08-32` | aquamarine |
| E14 | Email | `name@provider.com` | bold ash gray |
| E15 | Inline status | `[?]`, `[!]` | bright blue / vivid pink |
| E16 | Code marker | `$ command` | electric cyan chip |
| E17 | Task status | `- [/]`, `- [!]`, `- [?]`, `- [-]` | gray / red / yellow / dark gray |
| E18 | Filename | `draft_2.docx` | ash gray |
| A6a | Keywords (extension point) | — | off by default |

## Customizing colors

All colors live in `polymark.sublime-color-scheme`. The file is a literate
document: the **PARAMETERS** section at the top explains every knob, and each
rule carries its A#/E# label.

- **Restyle one feature** — find its label (e.g. `E13`) and edit that rule's
  `foreground`, `background` or `font_style`.
- **Unassigned placeholders** — every scope emitted by the syntax has a rule
  entry. Entries marked `UNASSIGNED` have empty color values on purpose; fill
  in a hex color to style them. Currently unassigned: the A2a arrow, heading
  text and separators, to-do whitespace, blockquote internals, all string
  parts, comment/email/code/filename meta scopes, and the bold/italic
  delimiters.
- **Reserved heading variables** — `heading_punc` and `h1`–`h6` in the
  `variables` block are reserved for future per-depth heading coloring. Heading
  colors currently come from the "General Markdown Heading Line" rule.
- **Theme hooks** — the `globals` block defines `accent` plus eight kind colors
  (`redish`, `orangish`, `yellowish`, …). Themes that read these keys follow
  the syntax palette, so the UI chrome matches your highlight colors.

## Customizing the syntax

The **PARAMETERS** section at the top of `polymark.sublime-syntax` documents
every regex that is likely to need tweaking. Each change is local to that file.

| Knob | Rule(s) | What to change |
| ---- | ------- | -------------- |
| File extensions | `file_extensions:` | Extensions that auto-select PolyMark (`.md`, `.txt`, `.pm`) |
| Custom tag names | E12 (both rules) | The `[A-Za-z][A-Za-z0-9_\-]*` charset — letters, digits, `-`, `_` |
| Timestamp format | E13 | The `\d{4}-\d{2}-…` pattern |
| Date header format | A8 | The `\d{4}-\d{2}-\d{2}` pattern |
| Duration range | A9 | The `\d{2}-\d{2}-\d{2} -> …` pattern |
| Email address | E14 | TLD length `\w{2,}` and the local/domain charset |
| Filename extensions | E18 | Extension length `[a-zA-Z]{2,5}` |
| Inline code | E19 | The backtick delimiter `` ` ``; inline code must close on the same line |
| Fenced code blocks | E20 | The ``` fence + language-token charset `[A-Za-z0-9_\-]*` in the `fenced-raw` rule |
| List markers | A7 | Leading characters `[\-+]` |

### Extension point (A6a)

The `keywords` context is intentionally empty so you can add your own keyword
rules without touching the main pipeline. Uncomment the shipped example:

```
keywords:
  - match: '\b(TODO|FIXME|NOTE)\b'
    scope: keyword.other.polymark
```

Then style `keyword.other.polymark` via the "Keyword Extension Point (A6a)"
rule in the color scheme.

### Extension point (E20): language companions

Fenced code blocks (E20) are language-agnostic in PolyMark. Language-specific
colors inside a block come from **companion packages** that ship a hidden
syntax whose scope is `source.embedded.polymark.<lang>` and that embeds
Sublime Text highlighting for the language (built-in, community, or bundled).

Shipped companions:

- `PolyMark-Language-Pack-Shell` — activates `bash`, `sh`, `shell`, `zsh`,
  `console` fences (embeds built-in `source.shell`).
- `PolyMark-Language-Pack-JavaScript` — activates `js`, `javascript`, `node`
  fences (embeds built-in `source.js`).
- `PolyMark-Language-Pack-Mermaid` — activates `mermaid`, `mmd` fences (embeds
  `source.mermaid` from the community
  [Mermaid](https://packagecontrol.io/packages/Mermaid) package — install it
  from Package Control).
- `PolyMark-Language-Pack-Argdown` — activates `argdown`, `argdown-map`, `ad`
  fences (embeds the bundled `source.argdown` grammar).

Each is a normal package folder next to `PolyMark`; install and restart.
PolyMark already references their scopes in the `fenced-language-extensions`
context, so nothing else needs editing.

**Adding your own language.** Create a folder e.g. `PolyMark-Language-Pack-Python`
containing a hidden syntax file:

```
%YAML 1.2
---
name: PolyMark Fenced Python
scope: source.embedded.polymark.python
hidden: true
contexts:
  main:
    - match: '^([ \t]*)(```)[ \t]*(python|py)[ \t]*$'
      captures:
        2: punctuation.definition.raw.code-fence.begin.polymark
        3: constant.other.language-name.polymark
      embed: scope:source.python
      embed_scope: markup.raw.block.polymark
      escape: '^([ \t]*)(```)[ \t]*$'
      escape_captures:
        2: punctuation.definition.raw.code-fence.end.polymark
```

Then register the scope in `polymark.sublime-syntax`:

```
fenced-language-extensions:
  - include: "scope:source.embedded.polymark.bash"
  - include: "scope:source.embedded.polymark.js"
  - include: "scope:source.embedded.polymark.python"   # added
```

No color work is needed: the color scheme's shared code-block palette styles
the standard scope families (`comment`, `string`, `keyword`, `constant`,
`variable`, `entity.name.function`, `entity.name.type`, ...) inside every
fenced block, for any language. If you want to customize one scope for your
language, add an optional rule to `polymark.sublime-color-scheme` scoped like
`markup.raw.block.polymark keyword.control.python`.

## Troubleshooting

| Symptom | Cause / fix |
| ------- | ----------- |
| Nothing is highlighted | The syntax isn't PolyMark: run `Set Syntax: PolyMark`, or check the file has a `.md`/`.txt`/`.pm` extension (or edit `file_extensions`). |
| Highlighted, but colors look off | The PolyMark color scheme isn't selected: `UI: Select Color Scheme > PolyMark`. |
| A construct renders in the default color | Its rule is an unassigned placeholder (see *Customizing colors*) — fill in a color. |
| A filename on a line that starts with a marker is not colored | Line-start marker rules (A7/E17) take priority over filenames — put filenames in running text or after a metadata key. |
| `->` isn't a ligature | Enable `"dlig"` in `font_options` and use a ligature font (e.g. JetBrains Mono). |
| Every `.txt` file is highlighted now | PolyMark includes `txt` in `file_extensions:`. Remove that line from `polymark.sublime-syntax` to opt out. |
| A fenced code block renders but the language isn't colored | The matching companion package isn't installed (e.g. `PolyMark-Language-Pack-Shell` for bash), or the language token isn't one it maps. A correctly typed block still renders in plain code-block styling. Colors for installed languages come automatically from the shared code-block palette. |
| A fence line with extra text after the language token isn't highlighted | Correct — a fence is three backticks plus (optionally) a language token and nothing else on the line. That is the "correctly typed only" rule (E20). |

## Support

PolyMark is free and open source (MIT). If it saves you time, you can support
future development at any of these:

- Gumroad — https://gumroad.com/YOUR_HANDLE
- Lemon Squeezy — https://lemonsqueezy.com/YOUR_HANDLE
- Payoneer — https://payoneer.com/YOUR_LINK

## License

MIT License. See `LICENSE` for the full text.
