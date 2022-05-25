from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (300, 500)

help_str = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    ChatScreen:
<WelcomeScreen>:
    name:'welcomescreen'
    MDFloatLayout:
        md_bg_color: 0/255, 0/255, 0/255, 1


        Image:
            source: "giphy.gif"
            size_hint: 0.9, 0.9
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
        MDLabel:
            text: "Health Care Chatbot"
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            font_size: "35sp"
            #font_name: "3.ttf"
    MDRaisedButton:
        text:'Welcome'
        pos_hint : {'center_x':0.5,'center_y':0.1}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    MDFloatLayout:
        md_bg_color: 86/255, 169/255, 183/255, 1
        Image:
            source: "loginlogo.jpg"
            pos_hint: {"y": .29}

        MDLabel:
            text: "Log in"
            pos_hint: {"center_x": .5, "center_y": .5}
            halign: "center"
            font_name: 'Arial'
            font_size: "40sp"
            theme_text_color: "Custom"
            #text_color: 60/225, 43/255, 117/255, 1
        MDTextField:

            id:login_email
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Email'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            text_color: 0/255, 0/255, 0/255, 1
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:login_password
            pos_hint: {'center_y':0.3,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Password'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            text_color: 0/255, 0/255, 0/255, 1
            password : True
            icon_right: 'key'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        
        MDRaisedButton:
            text:'Login'
            icon: "login"
            md_bg_color: 0/255, 0/255, 0/255, 1

            size_hint: (0.13,0.07)
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press:
                app.login()
                app.username_changer() 
        MDLabel:
            text: "OR"
            pos_hint: {"center_x": .3, "center_y": 0.1}
            halign: "center"
            font_name: 'Arial'
            font_size: "10sp"
            theme_text_color: "Custom"
            #text_color: 60/225, 43/255, 117/255, 1
    
    
        MDTextButton:
            text: 'Sign Up'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press:
                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'up'
        
        
<SignupScreen>:
    name:'signupscreen'
    MDFloatLayout:
        md_bg_color: rgba(250, 250, 250, 0)
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release:
                app.root.current = "loginscreen"
        MDLabel:
            text: "H i !  W e l c o m e"
            font_name: "Arial"
            font_size: "26sp"
            pos_hint: {"center_x": .6, "center_y": .85}
            color: rgba(0, 0, 59, 255)
        MDLabel:
            text: "Create a new account"
            font_name: "Arial"
            font_size: "13sp"
            pos_hint: {"center_x": .6, "center_y": .79}
            color: rgba(135, 133, 193, 255)
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.70,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.55,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        password : True
        icon_right: 'key'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'


<MainScreen>:
    name: 'mainscreen'
    Image:
        source: "tab.jpg"
        size_hint: 0.9, 0.9
        pos_hint: {'center_x': 0.5, 'center_y':0.8}
    MDLabel:
        id:username_info
        text:'Hello Main'
        #font_style:'H1'
        pos_hint: {"center_X": .5, "center_y": .58}
        halign:'center'
        font_size: "30sp"
    MDLabel:
        text: "Your Digital Assistant to guide you through our Health Care Services 24/7 Available!"
        size_hint_x: .9
        font_name: "Arial"
        font_size:"18sp"
        pos_hint: {"center_X": .3, "center_y": .40}
        halign: "center"
        theme_text_color: "Custom"
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x": .5, "center_y": .19}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [22, 22, 22, 22]
        TextInput:
            hint_text: "Patient Name"
            id: patient_name
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            font_size: "18sp"
            height: self.minimum_height
            cursor_color: 1, 170/255, 23/255, 1
            multiline: False
            cursor_width: "2sp"
            foreground_color: 1, 170/255, 23/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            #font_name: "Poppins"
    MDFloatLayout:
        size_hint: .45, .08
        pos_hint: {"center_x": .5, "center_y": .1}
        canvas:
            Color:
                rgb: (1, 170/255, 23/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [22, 22, 22, 22]            
            
    Button:
        text:""
        size_hint: (0.45,0.08)
        pos_hint: {"center_x":0.5,"center_y":0.1}
        background_color: 0, 0, 0, 0
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = "chatscreen"
    MDLabel:
        text: "LET'S CHAT"
        halign: "center"
        pos_hint: {"center_y": .1}
        #font_name: "Poppins"
        font_size: "18sp"
        color: 1, 1, 1, 1
                
<ChatScreen>:
    name: "chatscreen"
    MDLabel:
        text: "LET'S CHAT"
        halign: "center"
'''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass

class ChatScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='loginscreen'))
sm.add_widget(MainScreen(name='chatscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))


class LoginApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://healthcare-1136a-default-rtdb.firebaseio.com/.json"
        return self.strng



    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'

    auth = 'HkLcxQOT9qWZ8vcGhcvWywhS8ukF6ENBV1hEnb1g'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            self.dialog = MDDialog(title='Invalid Email and Password', text='Please enter correct username and password',
                                   size_hint=(0.7, 0.2), )
            self.dialog.open()

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"welcome {self.username}"
LoginApp().run()