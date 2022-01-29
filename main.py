import json
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


kvstring = '''<HelloScreen>:
    Image:
        source:'pic.png'
        size_hint_x: 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRaisedButton:
        text: "Continue to APP"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        on_press: app.continue_to_app()
<HomePage>:
    MDLabel:
        text: "WELCOME TO TRIPOTO"
        font_size: 35
        pos_hint: {"center_x": 0.5, "center_y": 0.95}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: "Enter details of Teammates"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.89}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDCard:
        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
    MDTextField:
        id: phn1
        hint_text: "Person 1 Phone"
        size_hint_x: 0.4
        font_size: 25
        max_text_length: 10
        pos_hint: {"center_x": 0.75, "center_y": 0.65}
        helper_text_mode: "on_error"
        helper_text: "Enter phone number"
    MDTextField:
        id: p1
        hint_text: "Person 1"
        size_hint_x: 0.4
        helper_text_mode: "on_error"
        helper_text: "Enter a name"
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.65}
    MDTextField:
        id: p2
        hint_text: "Person 2"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.55}
        helper_text_mode: "on_error"
        helper_text: "Enter a name"
    MDTextField:
        id: phn2
        hint_text: "Person2 phone"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.55}
        max_text_length: 10
        helper_text_mode: "on_error"
        helper_text: "enter 10 digit phone number"
    MDTextField:
        id: p3
        hint_text: "Person 3"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.45}
        helper_text_mode: "on_error"
        helper_text: "enter a name"
    MDTextField:
        id: phn3
        hint_text: "Person 3 phone"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.45}
        max_text_length: 10
        helper_text_mode: "on_error"
        helper_text: "enter 10 digit phone number"
    MDTextField:
        id: p4
        hint_text: "Person 4"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.35}
        helper_text_mode: "on_error"
        helper_text: "Enter a name"
    MDTextField:
        id: phn4
        hint_text: "Person 4 phone"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.35}
        max_text_length: 10
        helper_text_mode: "on_error"
        helper_text: "enter 10 digit phone number"
    MDTextField:
        id: p5
        hint_text: "Person 5"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.25}
        helper_text_mode: "on_error"
        helper_text: "enter a name"
    MDTextField:
        id: phn5
        hint_text: "Person 5 phone"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.25}
        helper_text_mode: "on_error"
        helper_text: "Enter 10-digit phone number"
    MDTextField:
        id: destination
        hint_text: "Destination"
        size_hint_x: 0.9
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter any place"
    MDRoundFlatButton:
        text: "Submit"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7
        on_press: app.submit(p1.text,p2.text,p3.text,p4.text,p5.text,phn1.text,phn2.text,phn3.text,phn4.text,phn5.text,destination.text)
<PostLogin>:
    MDLabel:
        text: "Planning for a Trip this week?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDRoundFlatButton:
        text: "Check Weather condition at your destination"        
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        on_press: app.weather()



    MDLabel:
        text: "Trip Started?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDRoundFlatButton:
        text: "Track expenses"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        on_press: app.track()


<Weather>:
    MDLabel:
        text: "The weather details at "+app.destination+" is: "
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.90}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Current Temperature:'+str(app.current_temperature)
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.80}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Humidity:'+str(app.humidity)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.70}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Minimum Temperature:'+str(app.tempmin)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Maximum Temperature:'+str(app.tempmax)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.60}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDLabel:
        text: "The location details of "+app.destination+" is :"
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.50}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDLabel:
        text: 'Latitude:'+str(app.latitude)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.40}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    
    MDLabel:
        text: 'Longitude:'+str(app.longitude)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        text: "Go to Home Page"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        on_press: app.goback()
<Overview>:
    MDRaisedButton:
        text: "Overview"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.25, "center_y": 0.85}
        size_hint: 0.5,0.075
        on_press: app.overview()
        border: 'yellow'
    MDFlatButton:
        text: "Transactions"
        font_size: 18
        pos_hint: {"center_x": 0.75, "center_y": 0.85}
        on_press: app.transactions()
        size_hint: 0.5,0.075
    MDCard:
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.27, "center_y": 0.65}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: app.persons[0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.persons[1]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.persons[2]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.persons[3]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.persons[4]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.73, "center_y": 0.65}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: str(app.spends[app.persons[0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.spends[app.persons[1]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.spends[app.persons[2]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.spends[app.persons[3]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.spends[app.persons[4]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        size_hint: 0.48, 0.4
        pos_hint: {"center_x": 0.27, "center_y": 0.25}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: 'Food'
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Utilities"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Travelling"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Parties"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Others"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        size_hint: 0.48, 0.4
        pos_hint: {"center_x": 0.73, "center_y": 0.25}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: str(app.cwisespends["Food"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Utilities"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Travelling"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Parties"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Others"])
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.plus
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDToolbar:
                    title: "Track Expenses"
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]
<Transactions>:
    MDRaisedButton:
        text: "Transactions"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.75, "center_y": 0.85}
        size_hint: 0.5,0.075
        on_press: app.transactions()
        border: 'yellow'
    MDFlatButton:
        text: "Overview"
        font_size: 18
        pos_hint: {"center_x": 0.25, "center_y": 0.85}
        on_press: app.track()
        size_hint: 0.5,0.075
    ScrollView:
        id: scroll
        do_scroll_x: False
        do_scroll_y: True
        size_hint: 1,0.80
        pos_hint: {"center_x": 0.5275, "y": 0}
        MDList:
            id: box
            spacing: 20
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.plus
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDToolbar:
                    title: "Track Expenses"
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]
<AddTransaction>
    MDCard:
        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
    MDTextField:
        id: amount
        hint_text: "Amount"
        size_hint_x: 0.7
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter Amount"
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.75}
    MDTextField:
        id: purpose
        hint_text: "Purpose"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.65}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter purpose"
    MDLabel:
        text: "Food"
        font_size: 20
        pos_hint: {"center_x": 0.70, "center_y": 0.5}
        size_hint_x: 0.30
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .5}
        on_active: app.on_checkbox_active('Food')
    MDLabel:
        text: "Utilities"
        font_size: 20
        pos_hint: {"center_x": 0.70, "center_y": 0.42}
        size_hint_x: 0.30
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .42}
        on_active: app.on_checkbox_active('Utilities')
    MDLabel:
        text: "Travelling"
        font_size: 20
        pos_hint: {"center_x": 0.7, "center_y": 0.35}
        size_hint_x: 0.3
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .35}
        on_active: app.on_checkbox_active('Travelling')
    MDLabel:
        text: "Parties"
        font_size: 20
        pos_hint: {"center_x": 0.7, "center_y": 0.27}
        size_hint_x: 0.3
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .27}
        on_active: app.on_checkbox_active('Parties')
    MDLabel:
        text: "Others"
        font_size: 20
        pos_hint: {"center_x": 0.7, "center_y": 0.20}
        size_hint_x: 0.3
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .20}
        on_active: app.on_checkbox_active('Others')
    MDLabel:
        text: app.persons[0]
        font_size: 20
        pos_hint: {"center_x": 0.30, "center_y": 0.5}
        size_hint_x: 0.30
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .45, 'center_y': .5}
        on_active: app.on_person_select(app.persons[0])
    MDLabel:
        text: app.persons[1]
        font_size: 20
        pos_hint: {"center_x": 0.30, "center_y": 0.42}
        size_hint_x: 0.30
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .45, 'center_y': .42}
        on_active: app.on_person_select(app.persons[1])
    MDLabel:
        text: app.persons[2]
        font_size: 20
        pos_hint: {"center_x": 0.30, "center_y": 0.35}
        size_hint_x: 0.3
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .45, 'center_y': .35}
        on_active: app.on_person_select(app.persons[2])
    MDLabel:
        text: app.persons[3]
        font_size: 20
        pos_hint: {"center_x": 0.30, "center_y": 0.27}
        size_hint_x: 0.3
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .45, 'center_y': .27}
        on_active: app.on_person_select(app.persons[3])
    MDLabel:
        text: app.persons[4]
        font_size: 20
        pos_hint: {"center_x": 0.30, "center_y": 0.20}
        size_hint_x: 0.3
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .45, 'center_y': .20}
        on_active: app.on_person_select(app.persons[4])
    MDRaisedButton:
        text: "Add"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7
        on_press: app.addSubmit(amount.text,purpose.text)
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDToolbar:
                    title: "Add Transaction"
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]
<TCard>:
    id: tcard
    orientation: "vertical"
    size_hint: 1, None
    height: box_top.height + box_bottom.height
    focus_behavior: True
    ripple_behavior: True
    pos_hint: {"center_x": .5, "center_y": .5}
    MDBoxLayout:
        id: box_top
        spacing: "20dp"
        adaptive_height: True
        MDBoxLayout:
            id: text_box
            orientation: "vertical"
            adaptive_height: True
            spacing: "10dp"
            padding: 0, "10dp", "10dp", "10dp"
            MDLabel:
                text: app.money
                theme_text_color: "Primary"
                font_style: "H5"
                bold: True
                adaptive_height: True
            MDLabel:
                text: app.paidby+"    "+app.paymenttime
                adaptive_height: True
                theme_text_color: "Primary"
    MDSeparator:
    MDBoxLayout:
        id: box_bottom
        adaptive_height: True
        padding: "10dp", 0, 0, 0
        MDLabel:
            text: app.purpose
            adaptive_height: True
            pos_hint: {"center_y": .5}
            theme_text_color: "Primary"
'''

Builder.load_string(kvstring)
sm = ScreenManager()
Window.size = (700, 600)


class TripotoApp(MDApp):
    def build(self):
        self.data = {
            'Add Transaction': 'Addtrs'
        }

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        sm.add_widget(HelloScreen(name='helloscreen'))
        sm.add_widget(HomePage(name='homepage'))

        sm.current = 'helloscreen'
        self.transactionsar = []
        return sm

    def continue_to_app(self):
        sm.current = 'homepage'

    def submit(self, p1, p2, p3, p4, p5, phn1, phn2, phn3, phn4, phn5, des):
        # if p1 and p2 and p3 and p4 and p5 and phn1 and phn2 and phn3 and phn4 and phn5 and des:
        self.persons = [p1, p2, p3, p4, p5]
        self.phones = [phn1, phn2, phn3, phn4, phn5]
        self.destination = des
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current = 'postlogin'
        sm.remove_widget(sm.get_screen('homepage'))
        '''else:
            Snackbar(
                text="Fields cannot be blank",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()'''

    def goback(self):
        sm.current = 'postlogin'

    def weather(self):
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                   + self.destination + "&units=metric&appid=" + 'bb9c06a29f2282c6d4b8606cc12d874c')

        api = json.loads(api_request.content)

        # Temperatures
        y = api['main']
        self.current_temperature = y['temp']
        self.humidity = y['humidity']
        self.tempmin = y['temp_min']
        self.tempmax = y['temp_max']

        # Coordinates
        x = api['coord']
        self.longitude = x['lon']
        self.latitude = x['lat']

        # Country
        z = api['sys']
        self.country = z['country']
        self.citi = api['name']
        '''search = f"weather in {self.destination}"
        url=f"https://www.google.com/search?&q={search}"
        url2=f"https://in.search.yahoo.com/search?p=weather%20in%20hyderabad"
        r=requests.get(url)
        s=BeautifulSoup(r.text,"html.parser")
        update=s.find("div",class_="BNeawe").text
        self.temp=update

        '''
        sm.add_widget(Weather(name='weather'))
        sm.current = 'weather'

    def addSubmit(self, amount, purpose):
        row = [self.personname, amount, purpose, self.category, datetime.now().strftime("%D %H:%M")]
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

        c = ['Food', 'Utilities', 'Travelling', 'Parties', 'Others']
        self.cwisespends = {"Food": 0, "Utilities": 0, "Travelling": 0, "Parties": 0, "Others": 0}
        self.spends = {self.persons[0]: 0, self.persons[1]: 0, self.persons[2]: 0, self.persons[3]: 0,
                       self.persons[4]: 0}
        for i in range(len(self.transactionsar)):
            for j in range(5):
                if self.transactionsar[i][0] == self.persons[j]:
                    self.spends[self.transactionsar[i][0]] = self.spends[self.transactionsar[i][0]] + int(
                        self.transactionsar[i][1])
            for k in c:
                if self.transactionsar[i][3] == k:
                    self.cwisespends[k] = self.cwisespends[k] + int(self.transactionsar[i][1])

        sm.add_widget(Overview(name='overview'))
        sm.current = "overview"

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
            l = TCard()
            sm.get_screen('transactions').ids.box.add_widget(l)

    def on_checkbox_active(self, category):
        self.category = category

    def on_person_select(self, personname):
        self.personname = personname

    def plus(self, addtrs):
        sm.add_widget(AddTransaction(name='addtransaction'))
        sm.current = 'addtransaction'


TripotoApp().run()