import flet as ft

class SecondPage:
    def __init__(self):
        self.container = ft.Column(
            [
                ft.Text("Second Page Content"),
                ft.ElevatedButton("Go Home", on_click=self.on_home_click),
            ]
        )
    
    def on_home_click(self, e):
        e.page.go("/")
