# PolyMark Feature Reference

> **v.3.0.2** — Updated 2026-08-05

> Every construct below is live — open this file in Sublime Text with the
> PolyMark syntax and color scheme active, and each sample renders in its
> assigned color.

## How to read this file

- This is both a cheat-sheet (what to type) and the verification document for
  `polymark.sublime-syntax` and `polymark.sublime-color-scheme`.
- Rule labels (A#, E#) are the same labels used to mark each rule in the
  syntax and color scheme files.
- Section titles are headings (`###`), so they double as E2 demos; the `///`
  dividers are E9 comment demos.
- A few rules are styled by unassigned placeholder entries and fall back to
  the scheme's default foreground until you give them a color — see
  `Instructions.md` → Customizing colors.

## Rule Index

| Rule | Feature | Type this |
| ---- | ------- | --------- |
| A2a  | Arrow ligature | `->` |
| A7   | List markers | `- item`, `+ item` |
| A8   | Date header | `2026-08-05` |
| A9   | Duration range | `16-18-07 -> 16-18-12` |
| E1   | Area/project hierarchy | `@Inbox/@Work` |
| E2   | Markdown-style headings | `# H1` … `###### H6` |
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

/// A Series

## Section A — Core rules

### A2a. Arrow ligature (->)

`->` becomes a highlighted arrow. Styled by an unassigned placeholder, so it
currently keeps the default foreground until you assign a color.

Next: ship the build -> deploy to prod

### A7. List markers (+, -)

Lines starting with `-` or `+`. The marker is a bold coral, the text follows.

- plain bullet item
+ plain bullet item

### A8. Date header (YYYY-MM-DD)

Four-digit-year dates are school-bus yellow.

Meeting on 2026-08-05 in the office.

### A9. Duration range (HH-MM-SS -> HH-MM-SS)

A start and end time joined by an arrow, highlighted electric cyan.

Standup runs 16-18-07 -> 16-18-12.

/// E Series

## Section E — Extension rules

### E1. Area/Project hierarchy (@Area/@Project)

An `@Area/@Project` path is electric blue on rich black. Sub-paths and names
with parentheses are supported.

@Inbox/@Home
@Inbox/@Work/@Projects
@Inbox/@(Someday-Maybe)

### E2. Markdown-style headings (H1 – H6)

The `#` symbols are colored and the heading line is vivid sky blue. The heading
text is scoped per depth (that per-depth rule is unassigned, so it inherits the
line color).

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

### E3. Incomplete to-do items (- [ ] Task)

The `[ ]` box is school-bus yellow and the bullet aquamarine.

- [ ] Write the release notes

### E4. Completed to-do items (- [x] Task)

The `[x]` box is aquamarine.

- [x] Ship the release

### E5. Metadata definition ([Key]: value)

A key in square brackets followed by `:`. The key and its punctuation are
aquamarine.

[Thoughts]: Refactor the parser
[Next]: Call the reviewer

### E6. Horizontal rule / document separator (---)

A line of exactly three dashes, tropical indigo.

---

### E7. Blockquote (> text)

A line starting with `>`, aquamarine on a gunmetal background.

> This is a quoted thought.

### E8. Quoted strings ("text")

Text between double quotes. The opening/closing quotes, the string content and
escape sequences each have a rule (currently unassigned placeholders).

"Hello, world"
"An escaped \" quote"

### E9. Comments (/// text)

Any line starting with three forward slashes is an ash-gray, italic comment.
The A Series and E Series dividers in this file are live examples.

/// this is a comment

### E10. Bold (**text**)

Text wrapped in double asterisks is bold, pale green. The `**` delimiters are
unassigned placeholders.

**This is bold text**

### E11. Italic (*text*)

Text wrapped in single asterisks is italic, pale green. The `*` delimiters are
unassigned placeholders.

*This is italic text*

### E12. Custom tagging (<tag> content </tag>)

A lowercase tag name (`<note>` … `</note>`) is soft purple on rich black. Other
rules keep working inside the content.

<note>
Any text can live here, including dates like 2026-08-05.
</note>

### E13. Date-time-stamp (YYYY-MM-DD-HH-MM-SS)

A full six-part timestamp, aquamarine.

2025-12-18-16-08-32

### E14. Email address (name@provider.com)

The user name, `@` and domain are bold ash gray.

hasan@gmail.com

### E15. Inline status markers ([?], [!])

`[?]` is bright blue (question) and `[!]` is vivid pink (alert). They work
anywhere in a line, including mid-sentence.

[?] Is this the right approach?
Review the report [!] before sending it.

### E16. Single-line code markers ($ command)

A `$` at the start of a line followed by a command, rendered as an electric
cyan chip on rich black.

$ ls -la
$ echo "hello world"

### E17. Task statuses (- [/], - [!], - [?], - [-])

Line-start status markers: `/` in progress (light gray), `!` critical (racing
red), `?` question (yellow), `-` abandoned (dark gray, including its content).

- [/] Refactoring the module
- [!] Fix the critical bug
- [?] Clarify the requirements
- [-] Dropped the old approach

### E18. Filename with extension (filename.ext)

Words ending in a 2–5 letter extension are ash gray (name + extension). On
lines that start with a `-`/`+` marker the marker rule wins, so filenames read
best in running text.

[File]: 2025_report.pdf
The file titled draft_2.docx was moved.

### A6a. Keywords — extension point (off by default)

The `keywords` context in `polymark.sublime-syntax` is intentionally empty. It
is a reserved slot for your own keyword rules, with a ready-to-uncomment
example (`TODO`, `FIXME`, `NOTE`). Until enabled, words like TODO render as
plain text.

To enable, uncomment the `keywords` context in the syntax file, then style
`keyword.other.polymark` via the "Keyword Extension Point (A6a)" rule in the
color scheme:

//   keywords:
//     - match: '\b(TODO|FIXME|NOTE)\b'
//       scope: keyword.other.polymark
