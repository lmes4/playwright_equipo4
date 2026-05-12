from playwright.sync_api import Page, expect

class Menu:

    def __init__(self, page: Page):
        self.page = page
        self.menu_quienes_somos = "Quiénes Somos"

    def abrir_menu_quienes_somos (self):
        self.page.get_by_role("link", name=self.menu_quienes_somos).click()