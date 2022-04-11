import kivy

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class GridLayoutApp(App):

    label_colors = [0, 0, 0, 0.9]

    parameters = [
       'T. Reparto (TR)',
       'T. Espera (TE)',
       'Tolvas',
       'Calibración',
       'H. Trabajo'
    ]

    parameters_row_two = [
        'KG/Disparo',
        'T. Reparto (TR)',
        'T. Espera (TE)',
        'H. Trabajo',
    ]

    solution_textinput = ''
    solution_textinput_row_two = ''

    parameters_inputtext_list = []
    parameters_inputtext_list_row_two = []


    def build(self):

        row_two_floatlayout = FloatLayout()

        # Create a Label Widget to hold functions' title
        self.title_label = Label(
            text = 'CÁLCULO DE ALIMENTACIÓN EN BASE A VALORES TEÓRICOS',
           color = self.label_colors,
        )

        # Create an AnchorLayout to hold label_title
        self.title_label_anchorlayout = AnchorLayout(
            anchor_x = 'center',
            anchor_y = 'top',
        )

        # Layout that holds the params widgets
        self.params_gridlayout = GridLayout(
            cols = len(self.parameters),
            row_force_default = True,
            row_default_height = 40
        )

        # Layout to hold the layout that holds the params
        self.params_anchorlayout = AnchorLayout(
            anchor_x = 'center',
            anchor_y = 'top',
        )

        # Layout to hold the solution text input
        self.solution_anchorlayout = AnchorLayout(
            anchor_x = 'right',
            anchor_y = 'top',
        )

        # Layout that holds the button widget
        self.button_anchorlayout = AnchorLayout(
            anchor_x = 'right',
            anchor_y = 'top',
        )

        # Text input to show the math results
        self.solution_textinput = TextInput(
            text = '0.00',
            size_hint = (.2, None),
            height = 30,
            multiline = False,
            readonly = True,
            halign = 'right',
            font_size = 15,
        )

        # Button to start formula evaluation
        self.result_button = Button(
            text = 'Calcular',
            size_hint_x = 0.2,
            size_hint_y = 0.4,
        )

        # Bind an action for on pressed button state
        self.result_button.bind(on_press=self.on_pressed_calcular)

        # Add parameters' labels
        for parameter in self.parameters:
            self.params_gridlayout.add_widget(Label(
                text = parameter,
                color = self.label_colors,
            )
        )

        # Add parameters' InputText widgets
        for parameter in self.parameters:
            self.parameter_widget = TextInput(text = "")
            self.parameters_inputtext_list.append(self.parameter_widget)
            self.params_gridlayout.add_widget(self.parameter_widget)

        main_gridlayout = GridLayout(
            cols = 1,
            #row_force_default = True,
        )

        ###
        # Create a Label Widget to hold functions' title
        self.title_label_row_two = Label(
            text = 'CÁLCULO DE ALIMENTACIÓN EN BASE A VALORES TOMADOS EN CAMPO',
            color = self.label_colors,
        )

        # Create an AnchorLayout to hold label_title
        self.title_label_anchorlayout_row_two = AnchorLayout(
            anchor_x = 'center',
            anchor_y = 'top',
        )

        self.params_gridlayout_row_two = GridLayout(
            cols = len(self.parameters_row_two),
            row_force_default = True,
            row_default_height = 40,
        )

        self.params_anchorlayout_row_two = AnchorLayout(
            anchor_x = 'right',
            anchor_y = 'top',
        )

        self.solution_anchorlayout_row_two = AnchorLayout(
            anchor_x = 'right',
            anchor_y = 'top',
        )

        # Layout that holds the button widget
        self.button_anchorlayout_row_two = AnchorLayout(
            anchor_x = 'right',
            anchor_y = 'top',
        )

        # Text input to show the math results
        self.solution_textinput_row_two = TextInput(
            text = '0.00',
            size_hint = (.2, None),
            height = 30,
            multiline = False,
            readonly = True,
            halign = 'right',
            font_size = 15,
        )

        # Button to start formula evaluation
        self.result_button_row_two = Button(
            text = 'Calcular',
            size_hint_x = 0.2,
            size_hint_y = 0.4,
        )

        # Bind an action for on pressed button state
        self.result_button_row_two.bind(on_press=self.on_pressed_calcular_row_two)

        # Add parameters' labels
        for parameter in self.parameters_row_two:
            self.params_gridlayout_row_two.add_widget(Label(
                text = parameter,
                color = self.label_colors,
            )
        )

        # Add parameters' InputText widgets
        for parameter in self.parameters_row_two:
            self.parameter_widget_row_two = TextInput(text = "")
            self.parameters_inputtext_list_row_two.append(self.parameter_widget_row_two)
            self.params_gridlayout_row_two.add_widget(self.parameter_widget_row_two)

        ###
        # Add the title_label to the title_label_layout
        self.title_label_anchorlayout.add_widget(self.title_label)

        # Add the gridlayout to the params_anchorlayout
        self.params_anchorlayout.add_widget(self.params_gridlayout)

        # Add self.solution_textinput to the solution_anchorlayout
        self.solution_anchorlayout.add_widget(self.solution_textinput)

        # Add the result_button to the button_anchorlayout
        self.button_anchorlayout.add_widget(self.result_button)

        # Add params_anchorlayout, solution_anchorlayout and button_anchorlayout
        # to the main layout which is main_gridlayout
        main_gridlayout.add_widget(self.title_label_anchorlayout)
        main_gridlayout.add_widget(self.params_anchorlayout)
        main_gridlayout.add_widget(self.solution_anchorlayout)
        main_gridlayout.add_widget(self.button_anchorlayout)

        ###
        # Add the title_label_row_two to the title_label_layout_row_two
        self.title_label_anchorlayout_row_two.add_widget(self.title_label_row_two)

        # Add the gridlayout to the params_anchorlayout
        self.params_anchorlayout_row_two.add_widget(self.params_gridlayout_row_two)

        # Add self.solution_textinput to the solution_anchorlayout
        self.solution_anchorlayout_row_two.add_widget(self.solution_textinput_row_two)

        # Add the result_button to the button_anchorlayout
        self.button_anchorlayout_row_two.add_widget(self.result_button_row_two)

        # Add params_anchorlayout, solution_anchorlayout and button_anchorlayout
        # to the main layout which is main_gridlayout
        main_gridlayout.add_widget(self.title_label_anchorlayout_row_two)
        main_gridlayout.add_widget(self.params_anchorlayout_row_two)
        main_gridlayout.add_widget(self.solution_anchorlayout_row_two)
        main_gridlayout.add_widget(self.button_anchorlayout_row_two)

        floatlayout = FloatLayout()
        
        background_img = Image(
                source='C:\\Users\\Confremar\\workspace\\img\\PISCMA\\01.jpg'
        )
        floatlayout.add_widget(background_img)
        floatlayout.add_widget(main_gridlayout)


        return floatlayout

    def on_pressed_calcular(self, instance):
        textinput_object_list = self.parameters_inputtext_list
        result = 1.0

        try:
            if textinput_object_list:
                for (index, parameter) in enumerate(self.parameters):
                    if index == 1:
                        tr = float(eval(textinput_object_list[index-1].text))
                        te = float(eval(textinput_object_list[index].text))
                        result *= 3600 / (tr + te)
                    else:
                        result *= float(eval(textinput_object_list[index].text))
            self.solution_textinput.text = f'{result:.2f} Kgs'

        except ValueError:
            self.solution_textinput.text = 'ERROR'
        except SyntaxError:
            self.solution_textinput.text = 'ERROR'

    def on_pressed_calcular_row_two(self, instance):
        textinput_object_list = self.parameters_inputtext_list_row_two
        result = 1.0

        try:
            if textinput_object_list:
                for (index, parameter) in enumerate(self.parameters_row_two):
                    if index == 2:
                        tr = float(eval(textinput_object_list[index-1].text))
                        te = float(eval(textinput_object_list[index].text))
                        print(f'Disparos: {3600 / (tr+te)}') 
                        result *= 3600 / (tr + te)
                    elif index == 1:
                        pass
                    else:
                        result *= float(eval(textinput_object_list[index].text))
            self.solution_textinput_row_two.text = f'{result:.2f} Kgs'

        except ValueError:
            self.solution_textinput_row_two.text = 'ERROR'
        except SyntaxError:
            self.solution_textinput_row_two.text = 'ERROR'


if __name__ == '__main__':
    app = GridLayoutApp()
    app.run()
