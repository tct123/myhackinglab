import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.platform import current_platform
import phonenumbers as pn
from phonenumbers import geocoder
from PIL import Image
import os
from mylocale.TR import tr
import locale

platform = toga.platform.current_platform


class MyHackingLab(toga.App):
    def startup(self):
        file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            )
        else:
            lang = locale.getlocale()
            lang, _ = lang
        about = toga.Box(children=[toga.Label("Page 2")])
        home = toga.Box(children=[])
        container = toga.OptionContainer(
            content=[
                (
                    tr(csv_file=file, target_key="HOME", langcode=lang),
                    home,
                    toga.Icon("pasta"),
                ),
                (
                    tr(csv_file=file, target_key="ABOUT", langcode=lang),
                    about,
                    toga.Icon("pasta"),
                ),
            ]
        )
        about.style.direction = "column"
        container.current_tab = 0
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container
        self.main_window.show()


def main():
    return MyHackingLab()
