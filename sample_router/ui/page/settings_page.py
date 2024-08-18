import flet as ft
from ui.control.theme_switcher import ThemeSwitcher  # ThemeSwitcherをインポート

class SettingsPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.theme_switcher = ThemeSwitcher(page)  # ThemeSwitcherのインスタンスを作成

        self.container = ft.Column(
            [
                ft.Text("Settings Page Content"),
                self.theme_switcher,  # テーマ切り替えボタンを追加
            ]
        )
    
    def on_home_click(self, e):
        self.page.go("/")
