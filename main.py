from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
import requests
from bs4 import BeautifulSoup

class HelloScreen(MDScreen):
    pass

class HomePage(MDScreen):
    pass
class PostLogin(MDScreen):
    pass
class Weather(MDScreen):
    pass
Builder.load_file("file.kv")
sm = ScreenManager()
Window.size = (700, 600)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        sm.add_widget(HelloScreen(name='helloscreen'))
        sm.add_widget(HomePage(name='homepage'))

        sm.current = 'helloscreen'

        return sm


    def continue_to_app(self):
        sm.current='homepage'
    def submit(self,p1,p2,p3,p4,p5,phn1,phn2,phn3,phn4,phn5,des):
        self.persons=[p1,p2,p3,p4,p5]
        self.phones=[phn1,phn2,phn3,phn4,phn5]
        self.destination=des
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current='postlogin'
        sm.remove_widget(sm.get_screen('homepage'))
    def goback(self):
        sm.current='postlogin'

    def weather(self):
        search = f"weather in {self.destination}"
        url=f"https://www.google.com/search?&q={search}"
        url2=f"https://in.search.yahoo.com/search?p=weather%20in%20hyderabad"
        r=requests.get(url)
        s=BeautifulSoup(r.text,"html.parser")
        update=s.find("div",class_="BNeawe").text
        self.temp=update
        sm.add_widget(Weather(name='weather'))
        sm.current='weather'

MainApp().run()