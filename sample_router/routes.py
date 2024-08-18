import flet as ft
from ui.page.home_page import HomePage
from ui.page.second_page import SecondPage
from ui.page.settings_page import SettingsPage

class Router:
    def __init__(self, page: ft.Page, content_container: ft.Column):
        self.page = page
        self.content_container = content_container
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

    def route_change(self, route):
        self.content_container.controls.clear()
        if self.page.route == "/":
            home_page = HomePage()
            self.content_container.controls.append(home_page.container)
        elif self.page.route == "/second":
            second_page = SecondPage()
            self.content_container.controls.append(second_page.container)
        elif self.page.route == "/settings":
            settings_page = SettingsPage(self.page)  # pageを渡してSettingsPageを初期化
            self.content_container.controls.append(settings_page.container)
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
