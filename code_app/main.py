
from kivy.app import App  # To Call the App
from kivy.lang  import Builder  # To Call an external file or write the codes directly inside the main file
from kivy.core.window import Window  # To Call the Window App to control App Size + color
from kivy.uix.screenmanager import ScreenManager, Screen  # ScreenManager => Main Screen    # Screen => Sub Screen In Main Screen

Window.clearcolor=(120/255.0, 0, 1, 1) # red | grean | blue | a
Window.size=(1500, 1000) # width | height


class MainWin(Screen):

    pass


class Sec_Win(Screen):

    pass

class Error(Screen):
    
    pass


class Python(Screen):
    pass
class SQL(Screen):
    pass
class Html(Screen):
    pass
class Js(Screen):
    pass
class Css(Screen):   
    pass
class Ruby(Screen):
    pass


class Win_Manager(ScreenManager):

    pass


bd = Builder.load_file('app.kv')

class M_App(App):

    def build(self):

        self.title = 'Coding App'       # App Title In PC

        return bd




if __name__ == '__main__' :

    M_App().run()

