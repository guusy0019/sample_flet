import flet as ft
from gui.calculator_app import CalculatorApp

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # サポート言語を日本語と英語で、初期値を日本語に設定する
    page.locale_configuration = ft.LocaleConfiguration(
    supported_locales=[ft.Locale("ja", "JP"), ft.Locale("en", "US")], current_locale=ft.Locale("ja", "JP")
    )

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.WB_SUNNY_OUTLINED),
    middle=ft.Text("CupertinoAppBar Example"),
    )
    page.title = "Calculator"
    calc = CalculatorApp()
    page.add(calc)

ft.app(target=main)