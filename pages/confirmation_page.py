from playwright.sync_api import Page, expect

#Realizado por Eli
class ConfirmationPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/confirmation"
    
    def verificar_compra_realizada (self):
        expect(self.page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    def verificar_producto_y_valor (self):
        expect(self.page.get_by_text("Juego de Palas15.99 €")).to_be_visible()

    def verificar_IVA (self):
        expect(self.page.get_by_text("IVA (21%)3.36 €")).to_be_visible()

    def verificar_envio (self):
        expect(self.page.get_by_text("Envío5.00 €")).to_be_visible()

    def verificar_total_compra (self):
        expect(self.page.get_by_text("Total24.35 €")).to_be_visible()  

    def hace_clic_volver_tienda (self):
        self.page.get_by_role("link", name="Volver a la Tienda").click()  