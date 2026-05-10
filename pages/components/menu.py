from playwright.sync_api import Page, expect

class MenuPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/"

    def abrir_pagina_inicio (self):
        self.page.goto(self.url)

        self.page.goto("https://web-qa.dev.adalab.es/")