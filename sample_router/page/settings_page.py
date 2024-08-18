import flet as ft

class SettingsPage:
    def __init__(self):
        self.container = ft.Column(
            [
                ft.Text("Settings Page Content"),
                ft.ElevatedButton("Go Home", on_click=self.on_home_click),
            ]
        )
    
    def on_home_click(self, e):
        e.page.go("/")
