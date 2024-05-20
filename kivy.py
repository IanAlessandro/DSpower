# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MinhaTela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        
        label1 = Label(text="Olá, mundo!")
        label2 = Label(text="Bem-vindo à minha primeira aplicação Kivy.")
        
        self.add_widget(label1)
        self.add_widget(label2)

class MinhaApp(App):
    def build(self):
        return MinhaTela()

if __name__ == "__main__":
    MinhaApp().run()
