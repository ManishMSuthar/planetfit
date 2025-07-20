from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.uix.image import Image

from matplotlib.backends.backend_agg import FigureCanvasAgg

class FigureCanvasKivyAgg(Widget):
    def __init__(self, figure, **kwargs):
        super(FigureCanvasKivyAgg, self).__init__(**kwargs)
        self.figure = figure
        self.canvas_agg = FigureCanvasAgg(self.figure)
        self.img = Image()
        self.add_widget(self.img)
        Clock.schedule_once(self.draw, 0)

    def draw(self, *args):
        self.canvas_agg.draw()
        w, h = map(int, self.figure.bbox.size)
        buf = self.canvas_agg.buffer_rgba()
        texture = Texture.create(size=(w, h))
        texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
        texture.flip_vertical()
        self.img.texture = texture
        self.img.size = (w, h)
