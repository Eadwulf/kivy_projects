import kivy

from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import RunTouchApp


# Create a dorpdown with 10 buttons
dopdown = DropDown()

for index in range(10):
    btn = button(
        text = f'Value {index}',
        size_hint_y = None,
        height = 40
    )
    btn.bind(on_release = lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)

mainbutton = Button(
    text = 'Hello',
    size_hint = (None, None),
    pos = (350, 300)
)

mainbutton.bind(on_release = dropdown.open)
dropdown.bind(on_select = lambda instance, x: setattr(
    mainbutton, 'text', x)
)


runTouchApp(mainbutton)
