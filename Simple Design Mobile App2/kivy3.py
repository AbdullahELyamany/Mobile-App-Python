
from kivy.lang import Builder
from kivymd.app import MDApp
v7x = '''
FloatLayout:
    MDFillRoundFlatButton
        text:'Enter'
        pos_hint:{'center_x':.5,'center_y':.5}
        text_color:0,0,1,1
        md_bg_color:0,1,0,1
    MDIconButton:
        icon:"android"
        pos:925,450
        
'''
class MyApp(MDApp):
    def build(self):
        self.root = Builder.load_string(v7x)

MyApp().run()