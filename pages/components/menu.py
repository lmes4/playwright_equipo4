from playwright.sync_api import Page, expect

class Menu:

    def __init__(self, page: Page):
        self.page = page
        self.menu_quienes_somos = "Quiénes Somos"
        self.menu_productos = "Productos"
        self.menu_contactos = "Contacto"

    def abrir_menu_quienes_somos (self):
        self.page.get_by_role("link", name=self.menu_quienes_somos).click()

    def abrir_menu_productos (self):
        self.page.get_by_role("link", name=self.menu_productos).click()
    
    def abrir_menu_contactos (self):
        self.page.get_by_role("link", name=self.menu_contactos).click()