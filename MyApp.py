from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Window.size = (360, 640)

class GerenciadorTelas(ScreenManager):
    pass

class PrimeiraTela(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Image(source='gummy_bears.jpg', size_hint=(1, 0.5), allow_stretch=True, keep_ratio=True))
        layout.add_widget(Label(text='Alpha Barbearia', font_size=32, size_hint_y=None, height=50))
        layout.add_widget(Label(text='Bora povo.', font_size=24, size_hint_y=None, height=50))
        layout.add_widget(Button(text='Clique aqui', font_size=24, size_hint_y=None, height=50, on_press=self.continuar))
        self.add_widget(layout)
    
    def continuar(self, *args):
        self.manager.current = 'segunda'

class SegundaTela(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Segunda Tela', font_size=32, size_hint_y=None, height=50))
        layout.add_widget(Button(text='Voltar', font_size=24, size_hint_y=None, height=50, on_press=self.voltar))
        self.add_widget(layout)

    def voltar(self, *args):
        self.manager.current = 'primeira'

class MyApp(App):
    def build(self):
        sm = GerenciadorTelas()
        sm.add_widget(PrimeiraTela(name='primeira'))
        sm.add_widget(SegundaTela(name='segunda'))
        return sm

if __name__ == '__main__':
    MyApp().run()

