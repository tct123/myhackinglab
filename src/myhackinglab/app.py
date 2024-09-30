import toga
import toga.platform
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.platform import current_platform
import os
from mylocale.TR import tr
import locale

# imported
from PIL import Image
import phonenumbers as pn
from phonenumbers import geocoder

platform = toga.platform.current_platform


class MyHackingLab(toga.App):
    def startup(self):
        file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()
            self.lang, _ = self.lang
            self.lang = self.lang.split("_")[0]
        print(self.lang)
        about = toga.Box(children=[toga.Label("Page 2")])
        home = toga.Box(
            children=[
                toga.Label(
                    tr(csv_file=file, target_key="WELCOMEMESSAGE", langcode=self.lang)
                )
            ]
        )
        container = toga.OptionContainer(
            content=[
                (
                    tr(csv_file=file, target_key="HOME", langcode=self.lang),
                    home,
                    toga.Icon("pasta"),
                ),
                (
                    tr(csv_file=file, target_key="ABOUT", langcode=self.lang),
                    about,
                    toga.Icon("information"),
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
