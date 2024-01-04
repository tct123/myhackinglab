"""
Hacking Application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.platform import current_platform
import phonenumbers as pn
from phonenumbers import geocoder
from PIL import Image


class MyHackingLab(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        main_box.style.direction = "column"

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        btn1 = toga.Button(
            text="Phonenumber Location", on_press=self.btn_phonenumber_location
        )
        btn2 = toga.Button(text="Image metadata", on_press=self.loadimagescreen)
        main_box.add(btn1)
        main_box.add(btn2)

    def leave(self, widget):
        self.exit()

    def btn_phonenumber_location(self, widget):
        box = toga.Box()
        box.style.direction = "column"
        window = toga.Window(title="Phonenumber Location")
        window.content = box
        window.show()
        self.number = toga.TextInput(placeholder="Phonenumber (international)")
        checkbutton = toga.Button(text="Check", on_press=self.phonenumber_screen)

        box.add(self.number)
        box.add(checkbutton)

    def phonenumber_data(self):
        try:
            data = pn.parse(self.number.value, None)
            countrycode = data.country_code
            print(countrycode)
            city = geocoder.description_for_number(f"+{countrycode}{data}", "en")
            return data, city
        except:
            data = "Failed!!!"
            city = data
            return data, city

    def phonenumber_screen(self, widget):
        box = toga.Box()
        box.style.direction = "column"
        window = toga.Window("Phonenumber")
        window.content = box
        window.show()
        data, city = self.phonenumber_data()
        info = toga.Label(f"Info: {data}")
        info2 = toga.Label(f"City: {city}")
        box.add(info)
        box.add(info2)

    def loadimagescreen(self, widget):
        self.box = toga.Box()
        self.box.style.direction = "column"
        self.window = toga.Window(title="Image metadata")
        self.window.content = self.box
        self.window.show()
        loadbtn = toga.Button(text="Load image", on_press=self.loadimage)
        self.box.add(loadbtn)

    def loadimage(self, widget):
        file_types = ["jpg", "png"]
        self.file = self.window.open_file_dialog(
            title="Load image", file_types=file_types
        )
        self.file.on_result = self.exifscreen

    def exifscreen(self, widget):
        self.box = toga.Box()
        self.box.style.direction = "column"
        self.window = toga.Window(title="Image metadata")
        self.window.content = self.box
        self.window.show()


def main():
    return MyHackingLab()
