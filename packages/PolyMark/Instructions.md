---
Author: Muhammad Mustafa Monowar
Updated: 2026-08-05
Target: Sublime-Text
Version: v.3.0.2
---

# PolyMark (A Syntax and Color Scheme Compatible with PolyOS)

## About PolyMark

PolyMark is a Color Scheme and Syntax Highlight Rule, a part of the PolyOS ecosystem.

For more information visit: https://thepolymodframework.carrd.co/

License:

PolyMark v.3.0.2 by Muhammad Mustafa Monowar
Copyright (c) 2026 Muhammad Mustafa Monowar
Licensed under the MIT License.

For more information see `LICENSE`.

## Setting Up
PolyMark builds on Markdown. The files using PolyMark should have a '.md' extension. The files mentioned in this document work with .md files opened with Sublime Text on both Windows and Mac. 

To use PolyMark: 
    1. Necessary files have to be downloaded from the source repository.
    2. Files have to be placed within the appropriate location.
    3. Preferences may need to be updated for full experience.

### Step 1: Preconfiguration
Make these changes to Sublime Text to avoid glitches after installation:
    
    - [ ] Install Package Control by pressing `Ctrl + P` and selecting `Package Control: Install Package Control`

    - [ ] Install the Theme: `Materialize`

    - [ ] Set the Theme to: `Material Vim Blackboard` (for compatibility)

A `Preferences.sublime-settings` is included in the package. Feel free to:

- [ ] Download the 'Preferences.sublime-settings' file from Sublime Text from the **source**. 

As of this version, the **source** is: `https://github.com/INTxK/PolyMark`

You can:
    
- [ ] mirror and incorporate preferences from the downloaded file to your own preferences file (recommended), or
    
- [ ] overwrite the existing preferences file with the file downloaded from GitHub. You need to install and set the theme before overwriting the preferences file. Use caution if you choose this method as it can lead to glitches or overwrite your existing preferences.


###	Step 2: Downloading the files
Download the `PolyMark` package folder from the **source**:

- [ ] PolyMark/polymark.sublime-syntax
- [ ] PolyMark/polymark.sublime-color-scheme

* The `polymark.sublime-syntax` is the syntax rule file that determines which patterns to highlight in the editor text.

* The `polymark.sublime-color-scheme` is the color-scheme file that highlights texts in sublime text editor as per the syntax file.
     
###	Step 3: Place the files
Place the `PolyMark` folder into the packages directory. You can access the root of the path by clicking the 'Browse Packages' menu item in Sublime Text.

The default path is: `~\Sublime Text\Packages\` (or `~/Library/Application Support/Sublime Text/Packages/` on macOS)

Place/Paste the `PolyMark` folder so the layout is:

- [ ] `Packages/PolyMark/polymark.sublime-syntax`
- [ ] `Packages/PolyMark/polymark.sublime-color-scheme`


### Step 4. Configure Sublime Text
Now that you're done placing the files:
    
- [ ] Type Ctrl+Shift+P (win)/Cmd+Shift+P to open the quickmenu and then:
    
    - [ ] Choose `Set Syntax: polymark`. This will set the Syntax to PolyMark.
    
    - [ ] Choose `UI Select Color Scheme: polymark`. This will set the color scheme to PolyMark.


## Additional Notes:
If you find a bug or want to provide feedback, share them [here](https://github.com/INTxK/PolyMark/issues)

---


