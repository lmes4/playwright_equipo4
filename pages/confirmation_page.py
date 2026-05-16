from playwright.sync_api import Page, expect

#Realizado por Eli
class ConfirmationPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/confirmation"
    
    def verificar_compra_realizada (self):
        expect(self.page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    def verificar_producto_y_valor (self,nombre_producto):
        expect(self.page.get_by_text(nombre_producto)).to_be_visible()

    def verificar_IVA (self,IVA):
        expect(self.page.get_by_text(IVA)).to_be_visible()

    def verificar_envio (self,envio):
        expect(self.page.get_by_text(envio)).to_be_visible()

    def verificar_total_compra (self,total):
        expect(self.page.get_by_text(total)).to_be_visible()  

    def hace_clic_volver_tienda (self):
        self.page.get_by_role("link", name="Volver a la Tienda").click()  