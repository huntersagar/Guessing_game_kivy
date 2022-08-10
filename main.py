import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config 
Config.set('graphics', 'resizable', True) 
from random import randint
def win():
    winning_number = randint(1,100)
    return winning_number
global count
count = 0
class Home(Screen):
    pass
class Play(Screen):
    pass
class Manager(ScreenManager):
    pass
class GameApp(App):
    def build(self):
        pass
    def check(self):
        input_number = self.ids.input.text
        int(input_number)
        winning_number = win()
        game_over = False
        while not game_over:
            pass
if __name__ == "__main__":
    GameApp().run()