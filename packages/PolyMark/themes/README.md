# Polymark theme variations

Every Polymark color scheme variation lives in this folder as a
`.sublime-color-scheme` file. The canonical base scheme stays one level up
(`packages/PolyMark/polymark.sublime-color-scheme`); it is never duplicated
here.

## Adding your own variation

1. Create `<name>.sublime-color-scheme` in this folder.
2. Recommended: `extends` the base and override only what you want to change:

   ```json
   {
     "extends": "Packages/PolyMark/polymark.sublime-color-scheme",
     "name": "My Polymark",
     "globals": {
       // Re-tints the whole system (PolyOS Editor Dark reads these):
       "background": "#000101",
       "foreground": "#edecee",
       "caret": "rgba(255, 255, 255, 0.2)",
       "accent": "#72EFA6",
       "redish": "#F08080",
       "orangish": "#FFB86C",
       "yellowish": "#FBDA35",
       "greenish": "#47FFC2",
       "cyanish": "#75FAF8",
       "bluish": "#47D4FF",
       "purplish": "#9D70FF",
       "pinkish": "#FF79C6"
     },
     "rules": [
       // Optional per-feature restyles ("name": <A#/E# label>).
     ]
   }
   ```

   A standalone (non-extending) scheme with its own full `rules` array also
   works — it just won't inherit future base-scheme updates. Prefer `extends`:
   any scope you don't override keeps the base styling, keyed off the base
   scheme's A#/E# rule index, and base additions propagate to your theme.

   Reference example: `polymark-neon.sublime-color-scheme` in this folder.

Conventions: lowercase hex throughout, and match the base scheme's rule
labels (`"name": "Feature (A#/E#)"`) so a theme stays greppable against the
base's RULE INDEX.
3. Run the sync script so the file reaches your live `Packages/PolyMark/`.
4. Pick it from the command palette (`PolyMark: Select Color Scheme...`) or
   cycle through all Polymark themes with `F7`.