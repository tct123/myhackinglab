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
        container = toga.OptionContainer(
            content=[
                (tr(csv_file=file, target_key="ABOUT", langcode=lang), about),
            ]
        )
        about.style.direction = "column"
        container.current_tab = 0
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container
        self.main_window.show()

        # btn1 = toga.Button(
        #    text=tr(csv_file=self.translationfile, target_key="PHONENUMBERLOCATION"),
        #    on_press=self.btn_phonenumber_location,
        # )
        # btn2 = toga.Button(
        #    text=tr(csv_file=self.translationfile, target_key="IMAGEMETADATA"),
        #    on_press=self.loadimagescreen,
        # )
        # main_box.add(btn1)
        # main_box.add(btn2)


#    def leave(self, widget):
#        self.exit()
#
#    def btn_phonenumber_location(self, widget):
#        box = toga.Box()
#        box.style.direction = "column"
#        window = toga.Window(
#            title=tr(csv_file=self.translationfile, target_key="PHONENUMBERLOCATION")
#        )
#        window.content = box
#        window.show()
#        self.number = toga.TextInput(placeholder="Phonenumber (international)")
#        checkbutton = toga.Button(text="Check", on_press=self.phonenumber_screen)
#
#        box.add(self.number)
#        box.add(checkbutton)
#
#    def phonenumber_data(self):
#        try:
#            data = pn.parse(self.number.value, None)
#            countrycode = data.country_code
#            print(countrycode)
#            city = geocoder.description_for_number(f"+{countrycode}{data}", "en")
#            return data, city
#        except:
#            data = "Failed!!!"
#            city = data
#            return data, city
#
#    def phonenumber_screen(self, widget):
#        box = toga.Box()
#        box.style.direction = "column"
#        window = toga.Window("Phonenumber")
#        window.content = box
#        window.show()
#        data, city = self.phonenumber_data()
#        info = toga.Label(f"Info: {data}")
#        info2 = toga.Label(f"City: {city}")
#        box.add(info)
#        box.add(info2)
#
#    def loadimagescreen(self, widget):
#        self.box = toga.Box()
#        self.box.style.direction = "column"
#        self.window = toga.Window(title="Image metadata")
#        self.window.content = self.box
#        self.window.show()
#        loadbtn = toga.Button(text="Load image", on_press=self.loadimage)
#        self.box.add(loadbtn)
#
#    def loadimage(self, widget):
#        file_types = ["jpg", "png"]
#        self.file = self.window.open_file_dialog(
#            title="Load image", file_types=file_types
#        )
#        self.file.on_result = self.exifscreen
#
#    def exifscreen(self, widget):
#        self.box = toga.Box()
#        self.box.style.direction = "column"
#        self.window = toga.Window(title="Image metadata")
#        self.window.content = self.box
#        self.window.show()
#


def main():
    return MyHackingLab()
