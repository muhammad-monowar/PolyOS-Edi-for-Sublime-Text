"""Behaviour tests for activate_profile.py.

The contract these guard:
  * the prompt appears on first start and only once, whichever way answered
  * declining writes nothing at all to Preferences
  * upgrading never replaces a setting the user already changed
  * the explicit Activate command does override, since that is its purpose
"""

import sublime

from tests.helpers import (
    Checker,
    fresh_editor,
    plugin_starts,
    preferences,
    state,
)

import activate_profile

THEME_SUFFIX = "PolyOS Editor Dark.sublime-theme"
SCHEME_SUFFIX = "polymark.sublime-color-scheme"
SYNTAX_SUFFIX = "polymark.sublime-syntax"


def test_first_start_accept(c):
    print("first start, user accepts")
    fresh_editor()
    sublime.dialog_answers.append(sublime.OK)

    plugin_starts()

    prefs = preferences()
    c.check("prompt shown exactly once", len(sublime.dialogs_shown) == 1)
    c.check("theme applied", prefs.get("theme", "").endswith(THEME_SUFFIX))
    c.check("color scheme applied", prefs.get("color_scheme", "").endswith(SCHEME_SUFFIX))
    c.check("default syntax applied", prefs.get("default_syntax", "").endswith(SYNTAX_SUFFIX))
    c.check("font size set to 16", prefs.get("font_size") == 16)
    c.check("answer recorded", state().get("polyos_activate") is True)
    c.check("settings saved", prefs.saved)


def test_restart_after_accept_is_silent(c):
    print("restart after accepting")
    fresh_editor()
    sublime.dialog_answers.append(sublime.OK)
    plugin_starts()

    shown_before = len(sublime.dialogs_shown)
    plugin_starts()

    c.check("no second prompt", len(sublime.dialogs_shown) == shown_before)
    c.check("theme still applied", preferences().get("theme", "").endswith(THEME_SUFFIX))


def test_first_start_decline(c):
    print("first start, user declines")
    fresh_editor()
    before = dict(preferences().data)
    sublime.dialog_answers.append(sublime.CANCEL)

    plugin_starts()

    prefs = preferences()
    c.check("prompt shown exactly once", len(sublime.dialogs_shown) == 1)
    c.check("Preferences untouched", prefs.data == before)
    c.check("nothing saved", not prefs.saved)
    c.check("decline recorded", state().get("polyos_activate") is False)
    c.check("points at the menu command", any("Activate profile" in m
                                              for m in sublime._window.status_messages))


def test_restart_after_decline_is_silent(c):
    print("restart after declining")
    fresh_editor()
    sublime.dialog_answers.append(sublime.CANCEL)
    plugin_starts()

    shown_before = len(sublime.dialogs_shown)
    plugin_starts()

    c.check("does not nag again", len(sublime.dialogs_shown) == shown_before)


def test_upgrade_preserves_user_choices(c):
    print("upgrade over an existing configuration")
    fresh_editor({
        "theme": "Packages/Theme - Adaptive/sublime-theme",
        "font_size": 20,
    })
    sublime.dialog_answers.append(sublime.OK)

    plugin_starts()

    prefs = preferences()
    c.check("chosen theme kept", prefs.get("theme") == "Packages/Theme - Adaptive/sublime-theme")
    c.check("chosen font size kept", prefs.get("font_size") == 20)
    c.check("stock keys still filled", prefs.get("default_syntax", "").endswith(SYNTAX_SUFFIX))


def test_prompt_again_rearms(c):
    print("Prompt again re-arms the prompt")
    fresh_editor()
    sublime.dialog_answers.append(sublime.OK)
    plugin_starts()

    activate_profile.PolyosEditorPromptAgainCommand().run()

    c.check("answer cleared", not state().has("polyos_activate"))

    sublime.dialog_answers.append(sublime.CANCEL)
    plugin_starts()
    c.check("prompt appears again", len(sublime.dialogs_shown) == 2)


def test_activate_command_overrides(c):
    print("explicit Activate overrides an existing theme")
    fresh_editor({"theme": "Packages/Theme - Adaptive/sublime-theme"})

    activate_profile.PolyosEditorActivateProfileCommand().run()

    c.check("theme replaced", preferences().get("theme", "").endswith(THEME_SUFFIX))


def test_apply_profile_is_idempotent(c):
    print("applying twice changes nothing the second time")
    fresh_editor()
    sublime.dialog_answers.append(sublime.OK)
    plugin_starts()

    changed = activate_profile.apply_profile()

    c.check("reports nothing to change", changed == [])


def main():
    c = Checker()
    for test in (
        test_first_start_accept,
        test_restart_after_accept_is_silent,
        test_first_start_decline,
        test_restart_after_decline_is_silent,
        test_upgrade_preserves_user_choices,
        test_prompt_again_rearms,
        test_activate_command_overrides,
        test_apply_profile_is_idempotent,
    ):
        test(c)
    return 0 if c.report("activate_profile behaviour") else 1