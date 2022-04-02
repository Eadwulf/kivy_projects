import kivy

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class GridLayoutApp(App):
    parameters = [
       'Tiempo de Reparto (TR)',
       'Tiempo de Espera (TE)',
       'Tolvas',
       'Calibración',
       'Horas de trabajo'
    ]

    solution_textinput = ''
    parameters_inputtext_list = []

    def build(self):
        main_gridlayout = GridLayout(
            cols = 1,
            #row_force_default = True,
        )

        # Layout to hold the layout that holds the params
        params_anchorlayout = AnchorLayout(
            anchor_x = 'center',
            anchor_y = 'top',
        )

        # Layout to hold the solution text input
        solution_anchorlayout = AnchorLayout(
            anchor_x = 'right',
            anchor_y = 'top',
        )

        # Layout that holds the button widget
        button_anchorlayout = AnchorLayout(
            anchor_x = 'center',
            anchor_y = 'bottom',
        )

        # Layout that holds the params widgets
        gridlayout = GridLayout(
            cols = len(self.parameters),
            row_force_default = True,
            row_default_height = 40
        )

        # Add parameters' labels
        for parameter in self.parameters:
            gridlayout.add_widget(Label(text = parameter))

        # Add parameters' InputText widgets
        for parameter in self.parameters:
            parameter_widget = TextInput(text = "")
            self.parameters_inputtext_list.append(parameter_widget)
            gridlayout.add_widget(parameter_widget)

        # Text input to show the math results
        self.solution_textinput = TextInput(
            text = 'Solution Text',
            size_hint = (.2, None),
            height = 30,
            multiline = False,
            readonly = True,
            halign = 'right',
            font_size = 15,
        )

        # Button to start formula evaluation
        result_button = Button(
            text = 'Calcular',
            size_hint_x = 0.2,
            size_hint_y = 0.2,
        )

        # Bind an action for on pressed button state
        result_button.bind(on_press=self.on_pressed_calcular)

        # Add the gridlayout to the params_anchorlayout
        params_anchorlayout.add_widget(gridlayout)

        # Add self.solution_textinput to the solution_anchorlayout
        solution_anchorlayout.add_widget(self.solution_textinput)

        # Add the result_button to the button_anchorlayout
        button_anchorlayout.add_widget(result_button)

        # Add params_anchorlayout, solution_anchorlayout and button_anchorlayout
        # to the main layout which is main_gridlayout
        main_gridlayout.add_widget(params_anchorlayout)
        main_gridlayout.add_widget(solution_anchorlayout)
        main_gridlayout.add_widget(button_anchorlayout)

        return main_gridlayout

    def on_pressed_calcular(self, instance):
        textinput_object_list = self.parameters_inputtext_list
        result = 1.0

        if textinput_object_list:
            for (index, parameter) in enumerate(self.parameters):
                if index == 1:
                    tr = float(eval(textinput_object_list[index-1].text))
                    te = float(eval(textinput_object_list[index].text))
                    result *= 3600 / (tr + te)
                else:
                    result *= float(eval(textinput_object_list[index].text))
                
        self.solution_textinput.text = f'{result:.2f}'


if __name__ == '__main__':
    app = GridLayoutApp()
    app.run()
