"""Minimal stand-in for `sublime_plugin`.

Sublime derives a command's name from its class name, so
`PolyosEditorActivateProfileCommand` answers to
`polyos_editor_activate_profile` without any string in the source. Nothing
needs registering here; the tests instantiate the classes directly.
"""


class ApplicationCommand:
    def run(self):
        pass


class WindowCommand:
    def __init__(self, window=None):
        self.window = window

    def run(self):
        pass


class TextCommand:
    def run(self, edit):
        pass


class EventListener:
    pass