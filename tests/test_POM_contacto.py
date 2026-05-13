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
def test_form_with_required_name_field_left_empty(page: Page):
    contact_page = ContactPage(page)
    print("Given the users enters contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()

    print ("fills required email with 'test@gmail.com'")
    contact_page.fill_contact_email("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    contact_page.fill_contact_message("test mensaje")

    print ("clicks send")
    contact_page.press_send_contact()

    print ("user should see the error message 'name is mandatory'")
    contact_page.verify_message_form("El nombre es obligatorio")
    

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

#Realizado por Lorena
def test_enviar_formulario_con_campo_obligatorio_mensaje_vacio(page: Page):
    contact_page = ContactPage ()
    
    print("Given la usuaria abre la pagina de contacto: Contáctanos | Vida Verde")
    contact_page.abrir_pagina_contactos()
    
    print("When rellena el campo obligatorio nombre")
    contact_page.rellenar_nombre_contacto("Marta Díaz")
    
    print("And rellena el campo obligatorio email")
    contact_page.rellena_email_contacto("test@gmail.com")
    
    print("And pulsa enviar")
    contact_page.hace_click_enviar()
    
    print("Then se muestra el mensaje de error: El mensaje es obligatorio")
    contact_page.verifica_mensaje("El mensaje es obligatorio")
    

# Realizado por Ana

def test_enviar_formulario_con_campo_obligatorio_nombre_vacio(page: Page):
    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto: Contáctanos | Vida Verde 'https://web-qa.dev.adalab.es/contact'")
    contact_page.abrir_pagina_contactos()

    print("When rellena el campo obligatorio email con 'test@gmail.com'")
    contact_page.rellena_email_contacto("test@gmail.com")

    print("And rellena el campo obligatorio mensaje con 'texto mensaje'")
    contact_page.rellena_mensaje_contacto("texto mensaje")

    print("And pulsar enviar")
    contact_page.hace_click_enviar()

    print("Then debe ver un mensaje de error 'El nombre es obligatorio'")
    contact_page.verifica_mensaje("El nombre es obligatorio")







