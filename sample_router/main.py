import flet as ft
from layout import MainLayout
from routes import Router

def main(page: ft.Page):
    page.title = "Routes Example"

    # メインレイアウトを作成
    layout = MainLayout(page)

    # ルーティングを管理
    router = Router(page, layout.content_container)

    # 初期ルートを設定
    page.go(page.route)

ft.app(target=main)
