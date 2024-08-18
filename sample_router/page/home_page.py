import flet as ft

class HomePage:
    def __init__(self):
        self.container = ft.Column(
            [
                ft.Text("Home Page Content"),
                ft.ElevatedButton("Visit Store", on_click=self.on_store_click),
            ]
        )
    
    def on_store_click(self, e):
        e.page.go("/store")
