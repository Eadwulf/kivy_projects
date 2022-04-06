from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):

    def build(self):
        img = Image(
            source = 'C:/Users/Confremar/workspace/img/aquamar_lagunas.jpg',
            size_hint = (1, 5),
            pos_hint = {
                'center_x': .5,
                'center_y': .5,
            }
        )

        label = Label(
            text = 'Cálculo de Alimemtación',
            size_hint = (.5, .5), 
            pos_hint = {
                'center_x': .5,
                'center_y': .5,
            }
        )
        return img


if __name__ == '__main__':
    app = MainApp()
    app.run()


