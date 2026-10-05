"""Minimal stand-in for the `sublime` module.

Only what activate_profile.py touches. Real Sublime settings objects also
remember unsaved edits and write through to Packages/User; this keeps it to
a dict so tests can assert on the result.
"""

OK = 1
CANCEL = 0
OK_CANCEL = 2

_settings = {}


class Settings:
    def __init__(self, initial=None):
        self.data = dict(initial or {})
        self.saved = False

    def get(self, key, default=None):
        return self.data.get(key, default)

    def has(self, key):
        return key in self.data

    def set(self, key, value):
        self.data[key] = value

    def erase(self, key):
        self.data.pop(key, None)


class Window:
    def __init__(self):
        self.status_messages = []

    def status_message(self, message):
        self.status_messages.append(message)


# Queued answers for message_dialog; empty means the user cancelled.
dialog_answers = []
# Every dialog text shown, in order.
dialogs_shown = []
# Callbacks queued by set_timeout, which tests fire manually.
timers = []

_window = Window()


def load_settings(name):
    return _settings.setdefault(name, Settings())


def save_settings(name):
    load_settings(name).saved = True


def message_dialog(message, flags=0):
    dialogs_shown.append(message)
    return dialog_answers.pop(0) if dialog_answers else CANCEL


def active_window():
    return _window


def set_timeout(callback, delay=0):
    timers.append(callback)