import kivy

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MainApp(App):

    def build(self):
        textinput = TextInput(
            text = 'Enter some text',
            multiline = False,
        )

        textinput.bind(on_text_validate=self.on_enter)
        return textinput
    
    def on_enter(self, instance, value):
        print('User pressed enter in', instance)


if __name__ == '__main__':
    app = MainApp()
    app.run()
