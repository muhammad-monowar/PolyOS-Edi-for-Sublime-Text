
/// A Series
# A1. Date-time-stamp [Rule]
Example: 2025-12-18-16-08-32

# A2. Area/Project [Rule]
Example: @Area/@Project

# A3. Bold [Rule] (**content**)
Example: **Hello** ** Hello **

# A4. Itilic [Rule] (*content*)
Example: *Hello* * Hello *

# A5. Custom Tag [Rule] (<tag> Content </tag>)
Example:
<tag>
Hello
Hello
Hello
</tag>

# A6. General Includes [Rule] (KEYWORDS, STRINGS, etc.)
Example: N/A

# A7. Markers [Rule] (+, -)
Example:

- Hello
+ Hello

# A8. Date Header [Rule] (####-##-##)
Example: 2025-12-18

# A9. Duration Range [Rule] (##-##-## -> ##-##-##)
Example: 16-18-07 -> 16-18-12

/// E Series
# E1. Area/Project [Rule] (@Area/Project)
Example: @Area/@Project

# E2. Markdown-style headings [Rule] (H1 through H6)
Example:
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

# E3. Incomplete to-do list items [Rule] (e.g., "- [ ] Task")
Example:
- [ ] Task Todo

# E4. Completed to-do list items [Rule] (e.g., "- [x] Task")
Example:
- [x] Task Done

# E5. Metadata Definition [Rule] ([InnerString]: OuterString)
Example:
[Thoughts]: Thought content
[Next]: Next action

# E6. Horizontal rule/document separator [Rule] (---)
Example:
---

# E7. Blockquote [Rule] (> String)
Example:
> "Quotes are nice to have." - Unknown

# E8. Strings [Rule]
Example:
Lorem Ipsum Doloret.

# E9. Comments [Rule] (/// Comment)
Example: /// this is a comment

# E10. Bold [Rule] (**Bold Item**)
Example:
** Bold **
**Bold**

# E11. Italics [Rule] (*Italicized Item*)
Example:
*hello*
* hello *

# E12. Custom Tagging [Rule] (<tag> Content </tag>)
Example:

<tag>

Hello

</tag>

# E13. Date-time-stamp [Rule] (YYYY-MM-DD-HH-MM-SS)
Example:
2025-12-18-16-22-57

# E14. Email Address Pattern [Rule] (name@provider.com)
Example: hasan@gmail.com

# E15. Status Markers [Rule] ([?], [!])
Example:
[?] What is the question?
[!] This is important!

# E16. Single-Line Code Marker [Rule] ($)
Example:
$ ls -a
$ touch hello.md

# E17. Project Management Patterns [Rule] (- [/], -[!], -[?])
Example:
- [/] means in progress
- [!] means important/critical
- [?] means ambiguous or needs clarification
- [-] means abandoned

# E18. Filename with Extension [Rule] (filename.ext)
Example:

the pattern need to cover these use cases:

[File]: 2025_report.pdf
The file titled draft_2.docx
+ file.txt
- file.txt


- [!] means important/critical
- [?] means ambiguous or needs clarification
- [-] means abandoned