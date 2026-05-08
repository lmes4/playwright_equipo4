from playwright.sync_api import Page, expect

class ProductosPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Catálogo de Productos"

    def abrir_productos_page(self):
        self.page.goto(self.url)

    def verificar_productos_category(self, category):
        expect(self.page.get_by_text(category).nth(2)).to_be_visible()

    def verificar_productos_name(self,product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verificar_productos_price(self,price):
        expect(self.page.get_by_text(price)).to_be_visible()

    def verificar_productos_title(self):
        expect(self.page.locator("h1")).to_contain_text(self.title)

    def verificar_productos_url(self):
        expect(self.page).to_have_url(self.url)