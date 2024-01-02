"""
Hacking Application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.platform import current_platform
import phonenumbers as pn


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

        btn1 = toga.Button(text="Phonenumber Location", on_press=self.btn_phonenumber_location)
        main_box.add(btn1)
    def leave(self, widget):
        self.exit()
    def btn_phonenumber_location(self,widget):
        box = toga.Box()
        box.style.direction = "column"
        self.window = toga.Window(title="Phonenumber Location")
        self.window.content = box
        self.window.show()
        number = toga.TextInput(placeholder="Phonenumber (international)")
        checkbutton = toga.Button(text="Check")

        box.add(number)


def main():
    return MyHackingLab()
