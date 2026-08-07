import sublime
import sublime_plugin

class TypewriterCenterListener(sublime_plugin.EventListener):
    """Vertically centers line 1 using invisible top padding phantoms."""

    def __init__(self):
        self.last_half_height = 0

    def on_selection_modified(self, view):
        self.center_line(view)

    def on_activated(self, view):
        self.center_line(view)

    def center_line(self, view):
        # Trigger when typewriter or distraction-free settings are active
        is_typewriter = view.settings().get("typewriter_mode_scrolling", False) or not view.settings().get("draw_centered", True)
        
        if not is_typewriter:
            view.erase_phantoms("top_typewriter_padding")
            self.last_half_height = 0
            return

        if len(view.sel()) == 0:
            return

        viewport_height = view.viewport_extent()[1]
        half_height = int(viewport_height / 2)

        # Create/update top phantom when viewport dimensions change
        if half_height > 0 and abs(self.last_half_height - half_height) > 5:
            self.last_half_height = half_height
            
            phantom_html = f'''
            <body id="typewriter-padding">
                <style>
                    html, body {{
                        margin: 0;
                        padding: 0;
                        background-color: transparent;
                    }}
                    .spacer {{
                        font-size: 1px;
                        line-height: {half_height}px;
                    }}
                </style>
                <div class="spacer">&nbsp;</div>
            </body>
            '''
            
            view.erase_phantoms("top_typewriter_padding")
            view.add_phantom(
                "top_typewriter_padding",
                sublime.Region(0, 0),
                phantom_html,
                sublime.LAYOUT_ABOVE
            )
            
            sublime.set_timeout(lambda: self.scroll_to_cursor(view), 20)
        else:
            self.scroll_to_cursor(view)

    def scroll_to_cursor(self, view):
        if len(view.sel()) > 0:
            view.show_at_center(view.sel()[0])
