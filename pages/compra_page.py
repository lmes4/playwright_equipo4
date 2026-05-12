from playwright.sync_api import Page, expect
#Realizado por Lorena
class CompraPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Compra"

    def abrir_productos_page(self):
        self.page.goto(self.url)

    def filtrar_productos_category(self, category):
        self.page.get_by_role("searchbox", name="category").fill("palas")
    
    def agregar_productos_carrito(self):
        self.page.get_by_role("button", name="Añadir Juego de Palas al").click()

    def visitar_pagina_carrito(self):
        self.page.get_by_role("link", name="Carrito de compra").click()
    
    def hacer_click_pago(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()

    def verifica_resumen_compra(self,name):
        expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()

    def verificar_producto_compra(self):
        expect(self.page.get_by_text("Juego de Palas")).to_be_visible()

    def verificar_precio_compra(self):
        expect(self.page.get_by_role("listitem").filter(has_text="Juego de Palas15.99 €").locator("data")).to_be_visible()

    def verificar_subtotal_compra(self):
        expect(self.page.get_by_role("definition").filter(has_text="15.99 €").locator("data")).to_be_visible()

    def verificar_iva_compra(self):
        expect(self.page.get_by_text("3.36 €")).to_be_visible()

    def verificar_envio_compra(self):
        expect(self.page.get_by_text("5.00 €")).to_be_visible()

    def verificar_total_compra(self):
        expect(self.page.get_by_text("24.35 €")).to_be_visible()

    def rellenar_nombre_contacto (self, name):
        self.page.get_by_role("textbox", name="Nombre Completo *").fill("Maria Diaz")

    def rellenar_email_contacto (self, email):
        self.page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    def rellenar_direccion_contacto (self, direccion):
        self.page.get_by_role("textbox", name="Direccion *").fill("Calle Aragon, 25, Madrid")

    def completar_click_compra(self):
        self.page.get_by_role("button", name="Completar Compra").click()

    def visualizar_checkout_compra(self):
        expect(self.page.get_by_role("heading", name="Finalizar Compra")).to_be_visible()

    def añadir_tarjeta_invalida(self):
        self.page.get_by_role("textbox", name="Numero de Tarjeta de Credito *").fill("1111 4242 4242 4242")

    def verificar_error_tarjeta(self):
        expect(self.page.get_by_text("Tarjeta de credito no valida")).to_be_visible()



    
    
