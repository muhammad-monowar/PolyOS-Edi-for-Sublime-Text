# PolyMark-Language-Pack-JavaScript

Standalone companion package for [PolyMark](https://thepolymodframework.carrd.co/).
Adds language-specific highlighting to PolyMark fenced code blocks tagged
`js`, `javascript` or `node` by embedding Sublime Text's built-in `source.js`
highlighting.

```js
const greeting = (name) => `Hello, ${name}!`;
console.log(greeting("world"));
```

## Install

Copy the `PolyMark-Language-Pack-JavaScript` folder into your `Packages`
directory next to `PolyMark`, then restart Sublime Text. No PolyMark edits are
needed — PolyMark detects this package automatically.

## License

MIT. See `LICENSE`.
