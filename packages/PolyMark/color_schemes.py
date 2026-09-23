import sublime
import sublime_plugin

BASE_SCHEME = "Packages/PolyMark/polymark.sublime-color-scheme"
THEMES_PREFIX = "Packages/PolyMark/themes/"
PROSE_SCHEME = "Packages/ProseMode/ProseMode.sublime-color-scheme"


def polymark_scheme_resources():
    """Returns the canonical base scheme followed by every Polymark theme
    variation found under PolyMark/themes/, sorted by name."""
    variations = [
        res
        for res in sublime.find_resources("*.sublime-color-scheme")
        if res.startswith(THEMES_PREFIX)
    ]
    variations.sort()
    return [BASE_SCHEME] + variations


def scheme_display_name(resource):
    """Human-friendly name for a color scheme resource."""
    name = resource.rsplit("/", 1)[-1]
    if name.endswith(".sublime-color-scheme"):
        name = name[:-len(".sublime-color-scheme")]
    return name


class CycleColorSchemeCommand(sublime_plugin.TextCommand):
    """Cycles through all Polymark themes and ProseMode with wrap-around."""
    def run(self, edit):
        rotation = polymark_scheme_resources() + [PROSE_SCHEME]

        current_scheme = self.view.settings().get("color_scheme")

        if current_scheme in rotation:
            index = rotation.index(current_scheme)
            next_scheme = rotation[(index + 1) % len(rotation)]
        else:
            next_scheme = BASE_SCHEME

        self.view.settings().set("color_scheme", next_scheme)


class SelectPolymarkColorSchemeCommand(sublime_plugin.WindowCommand):
    """Lists all Polymark themes in a quick panel and applies the selection
    to the active view."""
    def run(self):
        resources = polymark_scheme_resources()
        names = [scheme_display_name(res) for res in resources]

        self.window.show_quick_panel(
            names,
            lambda index: self._apply(resources, index),
            placeholder="Select a Polymark color scheme",
        )

    def _apply(self, resources, index):
        if index < 0:
            return

        view = self.window.active_view()
        if view is None:
            return

        view.settings().set("color_scheme", resources[index])