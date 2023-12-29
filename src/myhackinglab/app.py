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
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        if current_platform == "android" or current_platform == "iOS":
            self.main_window.error_dialog(title="Error", message="Platform is not supported.", on_result=self.leave)
        else:
            btn = toga.Button(text="exit", on_press=self.leave)
            main_box.add(btn)
    def leave(self):
        quit()


def main():
    return MyHackingLab()
