from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage

#Realizado por Jenniffer
def test_enviar_formulario_con_campos_obligatorios_validos(page: Page):

    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    contact_page.fill_contact_name("Marta Diaz")
    

    print("And rellena el email")
    contact_page.fill_contact_email("test@gmail.com")

    print("And rellena el mensaje")
    contact_page.fill_contact_message("test mensaje")

    print("And pulsa el boton enviar")
    contact_page.press_send_contact()

    print("Then debería ver un mensaje de éxito")
    contact_page.verify_message_form("¡Mensaje enviado con éxito!")

#Realizado por Jenniffer
def test_enviar_formulario_con_campo_obligatorio_email_vacio(page: Page):

    print ("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact ”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print ("When rellena el campo obligatorio nombre con “Marta Diaz”")
    page.get_by_role("textbox", name="Nombre *").fill("ANA SANCHEZ")

    print ("And rellena el campo obligatorio mensaje con “test mensaje”")
    page.get_by_role("textbox", name="Mensaje *").fill("test message")
    
    print("And pulsa enviar")
    page.get_by_role("button", name="Enviar Mensaje").click()
    page.pause()
    
    print("Then se muestra el mensaje de error el email es obligatorio")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()
    

#Realizado por Elisabet
def test_enviar_formulario_con_campo_obligatorio_email_invalido(page: Page):

    contact_page = ContactPage ()

    print ("Given el usuario entra en la página de contacto Contáctanos | Vida Verde “https://web-qa.dev.adalab.es/contact”)")
    contact_page.abrir_pagina_contactos()

    print ("When rellena el campo obligatorio nombre con “Elisabet QA”")
    contact_page.rellenar_nombre_contacto ("Elisabet QA")

    print ("And rellena el campo obligatorio email con “email”")
    contact_page.rellena_email_contacto ("email")

    print ("And rellena el campo obligatorio mensaje con “test mensaje”")
    contact_page.rellena_mensaje_contacto ("test mensaje")

    print ("And pulsa enviar")
    contact_page.hace_click_enviar()

    print ("Then debe ver un mensaje de error “El formato del email no es válido”")
    contact_page.verifica_mensaje("El formato del email no es válido")



