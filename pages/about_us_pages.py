from playwright.sync_api import Page, expect

class AboutusPage:
    def __init__(self, page: Page):
       self.page = page
       self.titulo = "Quiénes Somos"
       self.url = "https://web-qa.dev.adalab.es/about"


    def verificar_titulo_quienes_somos (self):
        expect(self.page.get_by_role("heading", name=self.titulo)).to_be_visible()

    def abrir_pagina_quienes_somos (self):
        self.page.goto(self.url)
