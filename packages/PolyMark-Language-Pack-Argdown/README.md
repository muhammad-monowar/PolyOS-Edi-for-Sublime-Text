# PolyMark-Language-Pack-Argdown

Standalone companion package for [PolyMark](https://thepolymodframework.carrd.co/).
Adds language-specific highlighting to PolyMark fenced code blocks tagged
`argdown`, `argdown-map` or `ad` by embedding the bundled minimal Argdown
grammar (`argdown.sublime-syntax`, scope `source.argdown`). The grammar is also
selectable for `.argdown` and `.ad` files.

```argdown
[Argdown is great]: it maps arguments as you type
  + <Supports it>: clear syntax, plain text
  - <Too niche>: small community
```

## Install

Copy the `PolyMark-Language-Pack-Argdown` folder into your `Packages`
directory next to `PolyMark`, then restart Sublime Text. No PolyMark edits are
needed — PolyMark detects this package automatically.

## Coverage

Headings, statement (`[title]:`) and argument (`<title>:`) definitions,
mentions (`@[...]` / `@<...>`), relation lists (`+`, `-`, `<+`, `+>`, `<-`,
`->`, `<_`, `_>`, `><`), premise-conclusion indices and inference separators,
frontmatter (`===`), hashtags, comments, strings, emphasis and inline code.

## License

MIT. See `LICENSE`.
