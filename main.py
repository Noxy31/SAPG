from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ColorProperty, StringProperty, OptionProperty
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.text import LabelBase


# Definition of screens and screenmanager
class HomeScreen(Screen):
    pass


class ClasseScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        # THEMING CODE
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.primary_hue = "700"
# TOOLBAR RIGHT BUTTON, LANGUAGE SELECTION FUNCTION
        list = ['English', 'Français(Coming Soon)', 'русский(Coming Soon)']
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "height": dp(56),
                "on_release": lambda x=f"Language set to {i}": self.menu_callback(x),
             } for i in list
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        return Builder.load_file('ColorTheme.kv')

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()


# Registering of police fonts
LabelBase.register(name='SFPro',
                   fn_regular='SF-Pro-Display-Regular.otf')
LabelBase.register(name='SFProSB',
                   fn_regular='SF-Pro-Display-Semibold.otf')
LabelBase.register(name='SFProB',
                   fn_regular='SF-Pro-Text-Bold.otf')

if __name__ == '__main__':
    MainApp().run()
