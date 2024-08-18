import flet as ft

class MainLayout:
    def __init__(self, page: ft.Page):
        self.page = page

        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=self.on_navigation_change,
        )

        self.content_container = ft.Column(
            [ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True
        )

        # メインレイアウトの作成
        self.page.add(
            ft.Row(
                [
                    self.rail,
                    ft.VerticalDivider(width=1),
                    self.content_container,  # ルーティングのコンテンツが表示される場所
                ],
                expand=True,
            )
        )

    def on_navigation_change(self, e):
        # ナビゲーションが変更されたときにルートを処理します
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.page.go("/")
        elif selected_index == 1:
            self.page.go("/second")
        elif selected_index == 2:
            self.page.go("/settings")
