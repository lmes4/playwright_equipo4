from playwright.sync_api import Page, expect

class CompraPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Compra"

    def abrir_productos_page(self):
        self.page.goto(self.url)
        