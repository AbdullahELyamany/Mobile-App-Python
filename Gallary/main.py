
import kivy
from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.core.window import Window


Window.size=(1920,1180)


class Picture(Scatter):

    source = StringProperty(None)


class Pictures(App):

    def build(self):

        root = self.root # connect to External file

                       #   sdcard == storage/emulated/0
        curdir = dirname('/sdcard/python/project/min-app/kivy_app/kivy/Rakwan/Gallary/') #Access to all file in images folder

        for file in glob(join(curdir,'img', '*')) :

            try:
                picture = Picture(source=file, rotation=randint(0, 30))
                root.add_widget(picture)
            except Exception as e :
                Logger.exception('Pictures: Unable to load <%s>' % file)
                



if __name__ == "__main__" :

    Pictures().run()


