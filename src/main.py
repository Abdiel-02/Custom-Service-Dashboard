import flet as ft
from flet import Container, Page, Text, TextSpan


async def main(page: Page):
    page.spacing = 0
    page.bgcolor = "#1B1C31"
    page.padding = ft.padding.all(0)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window_width = 1440
    page.window_height = 957

    await page.add_async(
        Container(
            expand=1,
            alignment=ft.alignment.center,
            content=Text(
                spans=[
                    TextSpan(
                        text="Dashboard",
                        style=ft.TextStyle(
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=ft.Offset(-1.0, 0),
                                    end=ft.Offset(1.0, 0.0),
                                    color_stops=[0.0, 0.5, 1.0],
                                    colors=["#814BFD", "#9A36D7", "#F239C9"],
                                )
                            ),
                        ),
                    )
                ]
            ),
        )
    )

    await page.window_center_async()
    await page.update_async()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="./assets")
