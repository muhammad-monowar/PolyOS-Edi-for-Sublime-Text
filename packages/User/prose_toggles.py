import sublime
import sublime_plugin

class ToggleProseUiCommand(sublime_plugin.TextCommand):
    """Toggles spell check, the status bar (word/character count), and the menu bar together."""
    def run(self, edit):
        # Toggle spell check
        spell_state = self.view.settings().get("spell_check", False)
        self.view.settings().set("spell_check", not spell_state)

        # Toggle status bar interface
        self.view.window().run_command("toggle_status_bar")

        # Toggle the menu bar
        window = self.view.window()
        window.set_menu_visible(not window.is_menu_visible())


class ToggleDistractionFreePolymarkCommand(sublime_plugin.WindowCommand):
    """Toggles distraction-free mode, hiding the menu bar on entry and
    restoring its previous visibility on exit."""
    _saved_menu = {}

    def run(self):
        window = self.window
        wid = window.id()

        if self._is_distraction_free(window):
            window.run_command("toggle_distraction_free")
            if wid in self._saved_menu:
                window.set_menu_visible(self._saved_menu.pop(wid))
        else:
            self._saved_menu[wid] = window.is_menu_visible()
            window.set_menu_visible(False)
            window.run_command("toggle_distraction_free")

    def _is_distraction_free(self, window):
        view = window.active_view()
        return view is not None and view.settings().get("draw_centered", False)


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
