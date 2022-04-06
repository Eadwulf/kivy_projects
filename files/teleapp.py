import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.uix.


class HBoxLayout(App):

    def build(self):
        layout = BoxLayout(padding=50, spacing=20)
        
        elements = [
            'Kilos Diarios',
            'Tolvas',
            'Calibración',
            'Porcentaje',
            'Horas de Reparto'
        ]

        for item in elements:
            label = Label(
                text = item,
                size_hint = (None, None),
                pos_hint = {
                    'center_x': 0.4,
                    'center_y': 0.5,
                }
            )
            layout.add_widget(label)

        for item in elements:
            textinput = TextInput(
                text = item,
                multiline = True,
                size_hint = (0.1, 0.05),
                pos_hint = {
                    'center_x': 0.5, 
                    'center_y': 0.5,
                }
            )
            layout.add_widget(textinput)

        return layout


if __name__ == '__main__':
    app = HBoxLayout()
    app.run()
