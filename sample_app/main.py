from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class RootWidget(BoxLayout):
    image_widget = ObjectProperty()

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
    
    def set_img(self):
        self.image_widget.set_image('./baboon.png')
    
    def prettify_img(self):
        self.image_widget.set_image('./lena.jpg')

class ImageWidget(BoxLayout):
    img = ObjectProperty()

    def set_image(self, fpath):
        self.img.source = fpath


class SampleApp(App):

    def build(self):
        rw = RootWidget()
	rw.set_img()
	return rw

if __name__ == "__main__":
    SampleApp().run()

