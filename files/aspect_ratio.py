from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class GridCell(Widget):
    color = ListProperty([1, 1, 1, 1])
    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)
        self.color = (0.0, 0.0, 0.0, 1.0)
        self.pos = (x, y)

class Level(GridLayout):
    def __init__(self, **kwargs):
        super(Level, self).__init__(**kwargs)
        self.cols = 30
        self.rows = 30
        self.spacing = 2
        self.positions = [(row, column) for row in range(self.rows) for column
                          in range(self.cols)]
        self.grid_cells = {}
        self.create_grid()

    def create_grid(self):
        for position in self.positions:
            self.grid_cells[position] = GridCell(*position)
            self.add_widget(self.grid_cells[position])


if __name__ == '__main__':
    from kivy.app import App
    Builder.load_file('grid_cell.kv')
    Window.clearcolor = (1.0, 1.0, 1.0, 1.0)


    class LevelApp(App):
        def build(self):
            self.title = 'Level'
            level = Level()
            return level


    level_app = LevelApp()
    level_app.run()

