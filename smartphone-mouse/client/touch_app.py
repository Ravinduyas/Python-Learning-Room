from flask import app
from kivy.app import MyApp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.clock import Clock
import socket
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# Import other necessary components


class TouchWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_touch_move=self.on_touch_move)
        self.server_address = ('127.0.0.1', 65432)  # Replace with your PC's IP if not using ADB

    def on_touch_move(self, instance, touch):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.server_address)
                data = f"{touch.x},{touch.y}"
                sock.sendall(data.encode())
        except Exception as e:
            print(f"Failed to send data: {e}")

class TouchApp(app):
    def build(self):
        return TouchWidget()

if __name__ == '__main__':
    MyApp().run()