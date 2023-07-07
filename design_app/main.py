from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size=(1000, 900)

NavHelper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'ELYMANE-[KivyApp]'
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                Image:
                    source: 'image.jpeg'
                MDLabel:
                    text: 'ELyamne App'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'AbdoELymane@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Profile'
                            
                        OneLineIconListItem:
                            text: 'WebSiteUs'
                            IconLeftWidget:
                                icon: 'gift-outline'
                        OneLineListItem:
                            text: 'Settings'
                        OneLineIconListItem:
                            text: 'Security'
                            IconLeftWidget:
                                icon: 'language-python'
                        OneLineListItem:
                            text: 'About'
                        OneLineIconListItem:
                            text: 'LogOut'
                            IconLeftWidget:
                                icon: 'logout'

"""


class App(MDApp):

    def build(self):

        screen = Builder.load_string(NavHelper)

        return screen







if __name__ == '__main__' :

    App().run()