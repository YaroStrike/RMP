# MyApp with Configurable Login
import configparser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDButton, MDButtonText
from secrets import token_hex
from kivymd.uix.dialog import MDDialog, MDDialogIcon, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer

session = {
    'login': None,
    'token': None
}

class MyApp(MDApp):

    def build_config(self, config):
        config.setdefaults('THEMING', {
            'theme_style': 'Light',
            'primary_palette': 'Fuchsia'
        })
        config.setdefaults('SESSION', {
            'login': None,
            'token': None
        })

    def build(self):
        self.theme_cls.primary_palette = self.config.get('THEMING', 'primary_palette')
        self.theme_cls.theme_style = self.config.get('THEMING', 'theme_style')
        self.root = Builder.load_file('ui.kv')
        return self.root

    def radio_change_color(self, checkbox, active):
        if active:
            self.theme_cls.primary_palette = checkbox.change.value

    def app_login(self, login, password):
        global session
        session['login'] = self.config.get('SESSION', 'login')
        session['token'] = self.config.get('SESSION', 'token')
        if login == 'adm' and password == 'adm':
            session['login'] = login
            session['token'] = token_hex(16)
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='skull',
                    theme_font_size='Custom',
                    font_size='48sp'
                ),
                MDDialogHeadlineText(
                    text='Бордо жалаповать'
                ),
                MDDialogSupportingText(
                    text='Спасибо и пожалуйста'
                ),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(
                            text='Ok'
                        ),
                        on_press=lambda *args: self.dialog.dismiss()
                    )
                )
            )
            self.dialog.open()
            self.root.current = 'main'
        else:
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='alert',
                    theme_font_size='Custom',
                    font_size='48sp'
                ),
                MDDialogHeadlineText(
                    text='ОШИБКА'
                ),
                MDDialogSupportingText(
                    text='Неправильный логин или пароль'
                ),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(
                            text='Ok'
                        ),
                        on_press=lambda *args: self.dialog.dismiss()
                    )
                )
            )
            self.dialog.open()

    def app_register(self, login, password, password_confirm):
        global session
        if password != password_confirm:
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='alert',
                    theme_font_size='Custom',
                    font_size='48sp'
                ),
                MDDialogHeadlineText(
                    text='ОШИБКА'
                ),
                MDDialogSupportingText(
                    text='Пароли не совпадают'
                ),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(
                            text='Ok'
                        ),
                        on_press=lambda *args: self.dialog.dismiss()
                    )
                )
            )
            self.dialog.open()
            return

        if login == 'admin' and password == 'admin':
            session['login'] = login
            session['token'] = token_hex(16)
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='account-child',
                    theme_font_size='Custom',
                    font_size='48sp'
                ),
                MDDialogHeadlineText(
                    text='Бордо жалаповать'
                ),
                MDDialogSupportingText(
                    text='Спасибо и пожалуйста'
                ),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(
                            text='Ok'
                        ),
                        on_press=lambda *args: self.dialog.dismiss()
                    )
                )
            )
            self.dialog.open()
            self.root.current = 'main'
        else:
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='alert',
                    theme_font_size='Custom',
                    font_size='48sp'
                ),
                MDDialogHeadlineText(
                    text='ОШИБКА'
                ),
                MDDialogSupportingText(
                    text='Неправильный логин или пароль'
                ),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(
                            text='Ok'
                        ),
                        on_press=lambda *args: self.dialog.dismiss()
                    )
                )
            )
            self.dialog.open()

    def switch_to_login(self):
        self.root.current = 'login'

MyApp().run()