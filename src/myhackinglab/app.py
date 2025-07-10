import toga
import toga.platform
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.platform import current_platform
import os
from mylocale.TR import TR
import locale
from toga.validators import Number

# imported
from PIL import Image
import phonenumbers as pn
from phonenumbers import geocoder

platform = toga.platform.current_platform


class MyHackingLab(toga.App):
    def startup(self):
        file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        print(file)
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()
            self.lang, _ = self.lang
            self.lang = str(self.lang.split("_")[0])
        print(self.lang)
        self.tr = TR(csv_file=file, langcode=self.lang)
        pn_input = toga.TextInput(
            placeholder=self.tr.tr(target_key="PNINPUT", langcode=self.lang)
        )
        about = toga.Box(children=[pn_input])
        home = toga.Box(
            children=[
                toga.Label(
                    text=self.tr.tr(target_key="WELCOMEMESSAGE", langcode=self.lang)
                )
            ]
        )
        container = toga.OptionContainer(
            content=[
                (
                    self.tr.tr(target_key="HOME", langcode=self.lang),
                    home,
                    toga.Icon("pasta"),
                ),
                (
                    self.tr.tr(target_key="PHONENUMBERPAGE", langcode=self.lang),
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
