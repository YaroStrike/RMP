from random import randint
from kivymd.app import MDApp
from kivy.lang import Builder
from secrets import token_hex
from datetime import datetime
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialogIcon, MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.widget import MDWidget
from kivymd.uix.transition import MDSharedAxisTransition
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle


swipe = 'up' #up down right left

game = {
    'size': 8,
    'move': 'up',
    'snek': [],
    'apple': [],
    'engine': None,
    'timer': None
}

class MainApp(MDApp):
    dialog = None

    def build_config(self, config):
        config.setdefaults('THEMING', {
            'theme_style': 'Light',
            'primary_palette': 'Green'
        })

        config.setdefaults('SESSION', {
            'login': None,
            'token': None,
            'last_login': None
        })
        pass

    def build(self):
        self.theme_cls.theme_style = self.config.get('THEMING', 'theme_style')
        self.theme_cls.primary_palette = self.config.get('THEMING', 'primary_palette')
        self.root = Builder.load_file("ui.kv")

        self.root.transition = MDSharedAxisTransition(
            transition_axis='x',
            duration=.5
        )

        if self.config.get('SESSION', 'token') != 'None' and self.check_session():
            self.root.current = 'main'
            return self.root

    def engine_timer(self, interval):
        timer = self.root.ids.game_timer.text.split()[1]
        minutes = int(timer.split(':')[0])
        seconds = int(timer.split(':')[1])
        seconds = seconds + 1 if seconds + 1 < 60 else 0
        minutes = minutes if seconds else minutes + 1

        self.root.ids.game_timer.text = f'Таймер: {str(minutes).zfill(2)}:{str(seconds).zfill(2)}'


    def engine_game(self, interval):
        global game, swipe
        field: MDWidget = self.root.ids.game_field
        field.canvas.clear()
        spacing = 5
        width = (field.width - (game['size'] - 1) * spacing) / game['size']


        game['move'] = swipe if ((swipe in ['up', 'down'] and game['move'] not in ['up', 'down']
                          ) or (
                swipe in ['left', 'right'] and game['move'] not in ['left', 'right'])) else game['move']

        swipe = None

        match game['move']:
            case 'up':
                game['snek'].append([game['snek'][-1][0], game['snek'][-1][1] + 1])

            case 'down':
                game['snek'].append([game['snek'][-1][0], game['snek'][-1][1] - 1])

            case 'left':
                game['snek'].append([game['snek'][-1][0] - 1, game['snek'][-1][1]])

            case 'right':
                game['snek'].append([game['snek'][-1][0] + 1, game['snek'][-1][1]])
        game['snek'].pop(0)



        with field.canvas:
            for y in range(game['size']):
                for x in range(game['size']): #0, 1, 2, 3, 4, 5, 6, 7
                    if [x,y] in game['snek']:
                        Color(.12, .92, .63)
                        Rectangle(
                            pos=[field.x + x * (spacing + width), field.y + y * (spacing + width)],
                            size=[width, width]
                        )
                    else:
                        Color(.92, .92, .92)
                        Rectangle(
                            pos=[field.x + x * (spacing + width), field.y + y * (spacing + width)],
                            size=[width, width]
                        )


    def start_game(self):
        global game
        self.root.current = 'game'
        self.root.ids.game_timer.text = 'Таймер: 00:00'
        game['snek'] = [[0, 0],[0, 1],[0, 2]]
        game['apple'] = []
        game['timer'] = Clock.schedule_interval(self.engine_timer, 1)
        game['engine'] = Clock.schedule_interval(self.engine_game, .4)

    def stop_game(self):
        global game
        game['timer'].cancel()
        game['timer'] = None

        game['engine'].cancel()
        game['engine'] = None

    def add_dialog(self, type_d: str = 'error', title: str = None, text: str = None, icon: str = None):
        match type_d:
            case "error":
                self.dialog = MDDialog(
                    MDDialogIcon(
                        icon=icon if icon else 'alert',
                        theme_font_size='Custom',
                        font_size='32sp'
                    ),
                    MDDialogHeadlineText(
                        text=title if title else ''
                    ),
                    MDDialogSupportingText(
                        text=text if text else ''
                    ),
                    MDDialogButtonContainer(
                        MDWidget(),
                        MDButton(MDWidget(),
                                 MDButtonText(
                                     text="ОК"
                                 ),
                                 on_press=lambda *args: self.dialog.dismiss()
                                 )
                    )
                )
            case "msg":
                self.dialog = MDDialog(
                    MDDialogIcon(
                        icon=icon if icon else 'information-outline',
                        theme_font_size='Custom',
                        font_size='32sp'
                    ),
                    MDDialogHeadlineText(
                        text=title if title else ''
                    ),
                    MDDialogSupportingText(
                        text=text if text else ''
                    ),
                    MDDialogButtonContainer(
                        MDWidget(),
                        MDButton(MDWidget(),
                                 MDButtonText(
                                     text="ОК"
                                 ),
                                 on_press=lambda *args: self.dialog.dismiss()
                                 )
                    )
                )
        self.dialog.open()

    def radio_change_color(self, checkbox, active):
        if active:
            self.theme_cls.primary_palette = checkbox.value
            self.config.set('THEMING', 'primary_palette', checkbox.value)
            self.config.write()

    def app_login(self, login, password):
        print('Кнопка нажата!')
        if login == 'a' and password == 'a':
            self.config.set('SESSION', 'login', login)
            self.config.set('SESSION', 'token', token_hex())
            self.config.set('SESSION', 'last_login', str(datetime.now()))
            self.config.write()
            self.root.current = 'main'
            self.add_dialog(type_d='msg', title=f'Добро пожаловать, {login}!', text=f'Powered by:\ngruger\nnukxkubi\nГерман\nYaroStrike')
        else:
            self.add_dialog(title='Авторизация!', text='Неправильный логи или пароль!')
            self.root.ids.login_login = ''
            self.root.ids.login_password = ''
            self.dialog.open()

    def close_session(self):
        self.config.set('SESSION', 'login', None)
        self.config.set('SESSION', 'password', None)
        self.config.set('SESSION', 'last_login', None)
        self.config.write()
        self.root.current = 'Login'

    def check_session(self):
        if randint(0, 2):
            self.config.set('SESSION', 'last_login', None)
            self.config.write()
            return True
        else:
            self.config.set('SESSION', 'login', None)
            self.config.set('SESSION', 'password', None)
            self.config.set('SESSION', 'last_login', None)
            self.config.write()

    def app_logout(self, login, password, password2):
        if login in ['a', 'b', 'c', '']:
            self.add_dialog(title='Ошибка регистрации', text='Пользователь существует или поле пустое!')
            return
        # if mt('[0-9A-Za-z@_!]{8,36}'):
        #     self.add_dialog(title='Регистрация', text='Пользователь существует!')
        #     return
        if password2 != password:
            self.add_dialog(title='Регистрация', text='Пароль не совпадает!')
            return

        self.root.ids.register_login.text = ''
        self.root.ids.register_password.text = ''
        self.root.ids.register_rpassword.text = ''
        self.root.current = 'Login'
        self.add_dialog(type_d='msg', title='УСПЕШНО', text='Вы перенаправлены на окно авторизации.')

    def app_register(self, register, password):
        pass

    def touch_down(self, element, touch):
        if element.collide_point(touch.x, touch.y):
            touch.ud['down'] = [touch.x, touch.y]

    def touch_up(self, element, touch):
        global swipe
        if 'down' in touch.ud and element.collide_point(touch.x, touch.y):
            width = touch.x - touch.ud['down'][0]
            height = touch.y - touch.ud['down'][1]
            if abs(height) > abs(width):
                swipe = 'up' if height > 0 else 'down'
            elif abs(width) > abs(height):
                swipe = 'right' if width > 0 else 'left'
            else:
                swipe = None

MainApp().run()