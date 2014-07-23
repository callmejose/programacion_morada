import kivy
kivy.require('1.8.0') # remplazar por tu versión actual de kivy !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hola mundo')


if __name__ == '__main__':
    MyApp().run()