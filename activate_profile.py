import sublime
import sublime_plugin

PACKAGE = "Packages/PolyOS-Edi-for-Sublime-Text"

# Keys that visibly change someone's editor. They are kept out of the shipped
# Preferences.sublime-settings and applied here instead, behind a prompt.
PROFILE = {
    "theme": PACKAGE + "/PolyOS Editor Dark.sublime-theme",
    "color_scheme": PACKAGE + "/polymark.sublime-color-scheme",
    "default_syntax": PACKAGE + "/polymark.sublime-syntax",
    "font_size": 16,
}

# Sublime's own stock values. A key is only written when it still matches one
# of these, so a user who has already chosen a theme is never switched.
DEFAULTS = {
    "theme": "auto",
    "color_scheme": "Packages/Color Scheme - Default.sublime-color-scheme",
    "default_syntax": "Packages/Text/Plain text.sublime-syntax",
    "font_size": 10,
}

STATE_FILE = "PolyOSEditor.sublime-settings"


def plugin_loaded():
    sublime.set_timeout(_maybe_prompt, 100)


def _state():
    return sublime.load_settings(STATE_FILE)


def _is_declined():
    return _state().get("polyos_activate") is False


def _maybe_prompt():
    if _is_declined():
        return

    window = sublime.active_window()
    if window is None:
        return

    if sublime.message_dialog(
        "PolyOS Editor\n\n"
        "Apply the PolyOS Editor profile now?\n\n"
        "This sets the theme, color scheme, default syntax and font size.\n"
        "Anything you have already changed is left alone, and every setting\n"
        "stays editable in Preferences.",
        sublime.OK_CANCEL,
    ) != sublime.OK:
        _state().set("polyos_activate", False)
        sublime.save_settings(STATE_FILE)
        _status(
            "skipped. Use Preferences > Package Settings > PolyOS Editor > "
            "Activate profile to apply it later."
        )
        return

    _status(_summary(apply_profile()))


def apply_profile(force=False):
    """Writes the profile into Packages/User/Preferences.sublime-settings.

    Only keys still holding Sublime's stock value are touched, so installing
    or upgrading never silently replaces a choice the user already made.
    force=True skips that guard and is used by the explicit command.
    """
    settings = sublime.load_settings("Preferences.sublime-settings")
    changed = []

    for key, value in PROFILE.items():
        if force or settings.get(key) == DEFAULTS.get(key):
            settings.set(key, value)
            changed.append(key)

    if changed:
        sublime.save_settings("Preferences.sublime-settings")

    _state().set("polyos_activate", True)
    sublime.save_settings(STATE_FILE)
    return changed


def _summary(changed):
    if not changed:
        return "nothing to change, profile already active"
    return "profile applied (" + ", ".join(changed) + ")"


def _status(message):
    window = sublime.active_window()
    if window is not None:
        window.status_message("PolyOS Editor: " + message)


class PolyosEditorActivateProfileCommand(sublime_plugin.ApplicationCommand):
    """Applies the PolyOS Editor theme, color scheme and syntax."""

    def run(self):
        _status(_summary(apply_profile(force=True)))


class PolyosEditorPromptAgainCommand(sublime_plugin.ApplicationCommand):
    """Forgets the activation choice so the prompt appears on the next start."""

    def run(self):
        _state().erase("polyos_activate")
        sublime.save_settings(STATE_FILE)
        _status("prompt reset, it will appear on the next start")