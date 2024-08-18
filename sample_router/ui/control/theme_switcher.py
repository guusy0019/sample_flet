import flet as ft

class ThemeSwitcher(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.is_dark_mode = False  # 初期状態はライトモード
        self.button = ft.ElevatedButton(
            text="Switch to Dark Mode",
            on_click=self.toggle_theme
        )

    def toggle_theme(self, e):
        # ダークモードとライトモードを切り替える
        self.is_dark_mode = not self.is_dark_mode
        if self.is_dark_mode:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.button.text = "Switch to Light Mode"
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.button.text = "Switch to Dark Mode"
        self.page.update()

    def build(self):
        # ボタンを返す
        return self.button
