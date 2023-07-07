from kivy.lang import Builder
from kivymd.app import MDApp
v7x = '''
Screen:
    MDFloatingActionButtonSpeedDial
        data: app.row
        rotation_root_button: True
'''
class MyApp(MDApp):
    row = {
        'Facebook':'facebook',
        'web':'whatsapp',
        'Google':'google'
    }

    def build(self):
        return Builder.load_string(v7x)

MyApp().run()