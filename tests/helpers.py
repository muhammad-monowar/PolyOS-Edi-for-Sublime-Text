"""Shared helpers: a fresh editor state and a tiny assertion vocabulary."""

import os

import sublime

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(TESTS_DIR)

# Sublime's shipped Preferences.sublime-settings values. activate_profile.py's
# stock-value guard compares against these, so every test that touches
# Preferences needs them present or the guard sees "user changed it".
STOCK_PREFERENCES = {
    "theme": "auto",
    "color_scheme": "Packages/Color Scheme - Default.sublime-color-scheme",
    "default_syntax": "Packages/Text/Plain text.sublime-syntax",
    "font_size": 10,
}


def fresh_editor(preferences=None):
    """Reset all module state and return a clean Preferences store.

    Pass `preferences` to simulate settings the user already chose.
    """
    sublime._settings.clear()
    sublime.dialog_answers.clear()
    del sublime.dialogs_shown[:]
    del sublime.timers[:]
    del sublime._window.status_messages[:]

    prefs = dict(STOCK_PREFERENCES)
    if preferences:
        prefs.update(preferences)
    sublime._settings["Preferences.sublime-settings"] = sublime.Settings(prefs)
    return sublime.load_settings("Preferences.sublime-settings")


def preferences():
    return sublime.load_settings("Preferences.sublime-settings")


def state():
    return sublime.load_settings("PolyOSEditor.sublime-settings")


def fire_timers():
    """Run whatever the plugin deferred via set_timeout."""
    for callback in sublime.timers:
        callback()
    del sublime.timers[:]


def plugin_starts():
    """Simulate Sublime loading activate_profile.py at startup."""
    import activate_profile

    activate_profile.plugin_loaded()
    fire_timers()


class Checker:
    def __init__(self):
        self.passed = 0
        self.failures = []

    def check(self, label, condition):
        if condition:
            self.passed += 1
            print("  PASS  " + label)
        else:
            self.failures.append(label)
            print("  FAIL  " + label)
        return bool(condition)

    def report(self, title):
        print()
        if self.failures:
            print("%s: %d passed, %d FAILED" % (title, self.passed, len(self.failures)))
            for label in self.failures:
                print("    - " + label)
        else:
            print("%s: all %d checks passed" % (title, self.passed))
        return not self.failures