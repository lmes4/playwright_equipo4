from playwright.sync_api import Page, expect

class ContactPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/contact"
        self.titulo = "Contáctanos"

    def abrir_pagina_contactos (self):
        self.page.goto(self.url)

    def verificar_titulo_contacto (self):
        expect(self.page.get_by_role("heading", name=self.titulo)).to_be_visible()

    def verificar_contacto_url (self):
        expect(self.page).to_have_url(self.url)

    def rellenar_nombre_contacto (self, name):
        self.page.get_by_role("textbox", name="Nombre *").fill(name)

    def rellena_email_contacto (self, email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def rellena_mensaje_contacto (self, mensaje):
        self.page.get_by_role("textbox", name="Mensaje *").fill(mensaje)

    def hace_click_enviar (self):
        self.page.get_by_role("button", name="Enviar Mensaje").click()

    def verifica_mensaje (self, texto):
        expect(self.page.get_by_text(texto)).to_be_visible()