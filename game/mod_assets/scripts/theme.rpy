init python:

    def set_t_b(st, at):
        return  im.MatrixColor(
            "gui/textbox.png",
            im.matrix.hue(persistent.theme_value)
        ), None

    def set_n_b(st, at):
        return im.MatrixColor(
            "gui/namebox.png",
            im.matrix.hue(persistent.theme_value)
        ), None

    class ColorTheme(object):
        
            def blue(self) -> None: self._set_theme(-90.0)

            def yellow(self) -> None: self._set_theme(-75.0)

            def green(self) -> None: self._set_theme(-180.0)

            def orange(self) -> None: self._set_theme(45.0)

            def default(self) -> None: self._set_theme(0.0, True)

            def _set_theme(self, value: float, is_default: bool = False) -> None:
                persistent.theme_value = value
                persistent.is_theme_default = is_default
                renpy.save_persistent()
                return

