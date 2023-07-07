
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivy.core.window import Window

Window.size=(1500, 1000)

img = '''
Image:
    source: 'img/python0.png'
    pos_hint={'center_x':0.5 , 'center_y':0.8}
    size_hint=(0.5, 0.5)
'''

class App(MDApp):

    def build(self):

        self.title = 'Learn Coding'                        # Title of App in PC
        self.theme_cls.primary_palette = 'Blue'            # Theme of Button
        self.theme_cls.primary_hue = '400'                 # Transparency شفافية
        self.theme_cls.theme_style="Dark" # Dark - Light   # Main Theme

        screen = Screen()

        label = MDLabel(
            text='Learn Python',
            halign="center",
            theme_text_color="Primary",
            font_style="H5",
            pos_hint={'center_x':0.5 , 'center_y':0.6}
        )

        btn1 = MDRectangleFlatButton(
            text="Python Kivy",
            pos_hint={'center_x':0.5 , 'center_y':0.1},
            size_hint= (0.6, 0.1)
        )

        btn2 = MDRectangleFlatButton(
            text="Python Tkinter",
            pos_hint={'center_x':0.5 , 'center_y':0.2},
            size_hint= (0.6,0.1)
        )

        btn3 = MDRectangleFlatButton(
            text="Python Flask",
            pos_hint={'center_x':0.5 , 'center_y':0.3},
            size_hint=(0.6, 0.1)
        )

        btn4 = MDRectangleFlatButton(
            text="Python Django",
            pos_hint={'center_x':0.5 , 'center_y':0.4},
            size_hint=(0.6, 0.1)
        )


           #↓ You can Access the Information from 
           #↓     1- /sdcard/
           #↓     2- internet==>  website-->  'Material Design Icons' » To know the Icon Names
        icon1 = MDIconButton(
            icon='language-python',
            pos_hint={'center_x':0.3 , 'center_y':0.1}
        )
        icon2 = MDIconButton(
            icon='language-python',
            pos_hint={'center_x':0.3 , 'center_y':0.2}
        )
        icon3 = MDIconButton(
            icon='language-python',
            pos_hint={'center_x':0.3 , 'center_y':0.3}
        )
        icon4 = MDIconButton(
            icon='language-python',
            pos_hint={'center_x':0.3 , 'center_y':0.4}
        )



        images = Builder.load_string(img)

        screen.add_widget(btn1)
        screen.add_widget(btn2)
        screen.add_widget(btn3)
        screen.add_widget(btn4)
        
        screen.add_widget(images)
        screen.add_widget(label)
        
        screen.add_widget(icon1)
        screen.add_widget(icon2)
        screen.add_widget(icon3)
        screen.add_widget(icon4)


        return screen





if __name__ == "__main__" :

    App().run()