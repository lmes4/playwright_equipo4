from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
       self.page = page
       self.url = "https://web-qa.dev.adalab.es"
       self.titulo = "Vida Verde"

    def abrir_pagina_inicio (self):
        self.page.goto(self.url)

    def verificar_pagina_inicio (self):
        expect(self.page.get_by_role("heading", name=self.titulo)).to_be_visible()

