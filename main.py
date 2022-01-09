import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
import requests
from bs4 import BeautifulSoup
from kivymd.uix.snackbar import Snackbar
from openpyxl import *
from datetime import datetime

class HelloScreen(MDScreen):
    pass

class HomePage(MDScreen):
    pass
class PostLogin(MDScreen):
    pass
class Weather(MDScreen):
    pass

class Overview(MDScreen):
    pass

class Transactions(MDScreen):
    pass
class AddTransaction(MDScreen):
    pass
class TCard(MDCard):
    pass
Builder.load_file("file.kv")
sm = ScreenManager()
Window.size = (700, 600)


class MainApp(MDApp):
    def build(self):
        self.data = {
            'Add Transaction': 'Addtrs',
            "hi": "hello"
        }
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        sm.add_widget(HelloScreen(name='helloscreen'))
        sm.add_widget(HomePage(name='homepage'))

        sm.current = 'helloscreen'
        self.transactionsar=[]
        return sm


    def continue_to_app(self):
        sm.current='homepage'
    def submit(self,p1,p2,p3,p4,p5,phn1,phn2,phn3,phn4,phn5,des):
        #if p1 and p2 and p3 and p4 and p5 and phn1 and phn2 and phn3 and phn4 and phn5 and des:
        self.persons=[p1,p2,p3,p4,p5]
        self.phones=[phn1,phn2,phn3,phn4,phn5]
        self.destination=des
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current='postlogin'
        sm.remove_widget(sm.get_screen('homepage'))
        '''else:
            Snackbar(
                text="Fields cannot be blank",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()'''
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
    def addSubmit(self,amount,purpose,name):

        row = [name, amount, purpose, self.category, datetime.now().strftime("%D %H:%M")]
        self.transactionsar.append(row)
        Snackbar(
            text="Transaction added successfully!!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()
        try:
            sm.remove_widget(sm.get_screen('overview'))
            sm.remove_widget(sm.get_screen('transactions'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass
        sm.add_widget(Overview(name='overview'))
        sm.add_widget(Transactions(name='transactions'))
        self.track()
        sm.remove_widget(sm.get_screen('addtransaction'))
    def track(self):
        try:
            sm.remove_widget(sm.get_screen('overview'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass



        c=['Food','Utilities','Travelling','Parties','Others']
        self.cwisespends={"Food":0,"Utilities":0,"Travelling":0,"Parties":0,"Others":0}
        self.spends={self.persons[0]:0,self.persons[1]:0,self.persons[2]:0,self.persons[3]:0}
        for i in range(len(self.transactionsar)):
            for j in range(5):
                if self.transactionsar[i][0]==self.persons[j]:
                    self.spends[self.transactionsar[i][0]]=self.spends[self.transactionsar[i][0]]+int(self.transactionsar[i][1])
            for k in c:
                if self.transactionsar[i][3]==k:
                    self.cwisespends[k]=self.cwisespends[k]+int(self.transactionsar[i][1])

        sm.add_widget(Overview(name='overview'))
        sm.current="overview"

        try:
            sm.remove_widget(sm.get_screen('transactions'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass


    def transactions(self):
        try:
            sm.remove_widget(sm.get_screen('transactions'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        self.lenn = len(self.transactionsar) * 90
        sm.add_widget(Transactions(name='transactions'))
        sm.current = 'transactions'
        try:
            sm.remove_widget(sm.get_screen('overview'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass
        for i in range(len(self.transactionsar)):
            self.money = self.transactionsar[i][1]
            self.paidby = self.transactionsar[i][0]
            self.purpose = self.transactionsar[i][2]
            self.category = self.transactionsar[i][3]

            self.paymenttime = self.transactionsar[i][4]
            l=TCard()
            sm.get_screen('transactions').ids.box.add_widget(l)
    def on_checkbox_active(self,category):
        self.category=category

    def plus(self, addtrs):
        sm.add_widget(AddTransaction(name='addtransaction'))
        sm.current = 'addtransaction'
MainApp().run()