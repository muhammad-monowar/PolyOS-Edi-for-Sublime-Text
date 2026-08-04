import sublime
import sublime_plugin

class ToggleProseUiCommand(sublime_plugin.TextCommand):
    """Toggles spell check and the status bar (word/character count) together."""
    def run(self, edit):
        # Toggle spell check
        spell_state = self.view.settings().get("spell_check", False)
        self.view.settings().set("spell_check", not spell_state)
        
        # Toggle status bar interface
        self.view.window().run_command("toggle_status_bar")


class CycleColorSchemeCommand(sublime_plugin.TextCommand):
    """Cycles between ProseMode and PolyMark color schemes."""
    def run(self, edit):
        prose_scheme = "Packages/ProseMode/ProseMode.sublime-color-scheme"
        polymark_scheme = "Packages/PolyMark/polymark.sublime-color-scheme"
        
        current_scheme = self.view.settings().get("color_scheme")
        
        if current_scheme == prose_scheme:
            self.view.settings().set("color_scheme", polymark_scheme)
        else:
            self.view.settings().set("color_scheme", prose_scheme)
