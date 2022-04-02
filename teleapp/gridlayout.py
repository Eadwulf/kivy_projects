import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class GridLayoutApp(App):
    parameters = [
       'Kilos Diarios',
       'Tolvas',
       'Calibración',
       'Horas de Reparto',
       'Porcentaje',
    ]


    def build(self):
        main_gridlayout = GridLayout(
            cols = 1,
            row_force_default = True,
        )

        gridlayout = GridLayout(
            cols = len(self.parameters),
            row_force_default = True,
            row_default_height = 40
        )

        for parameter in self.parameters:
            gridlayout.add_widget(Label(text = parameter))

        for parameter in self.parameters:
            gridlayout.add_widget(TextInput(text = ""))

        main_gridlayout.add_widget(gridlayout)
        main_gridlayout.add_widget(Button(text = 'Calcular'))

        return main_gridlayout

if __name__ == '__main__':
    app = GridLayoutApp()
    app.run()
