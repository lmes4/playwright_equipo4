from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/cart'
        self.title = "Carrito de Compra"

    def abrir_cart_page(self):
        self.page.goto(self.url)

    def verificar_producto_en_carrito(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def verificar_total_precio(self, total):
        expect(self.page.get_by_text(total)).to_be_visible()

    def verificar_numero_productos(self, cantidad):
        expect(self.page.locator(".cart-item")).to_have_count(cantidad)

    def eliminar_producto(self, product_name):
        self.page.get_by_role("button", name=f"Eliminar {product_name}").click()

    def vaciar_carrito(self):
        self.page.get_by_role("button", name="Vaciar carrito").click()

    def ir_a_checkout(self):
        self.page.get_by_role("button", name="Finalizar compra").click()

    
    