from playwright.sync_api import Page, expect

def test_enviar_formulario_con_campos_obligatorios_validos(page: Page):
    print("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact ”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When rellena el nombre con “Marta Diaz”")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    print("And rellena el email con “test_automation@test.com”")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And rellena el mensaje con “test mensaje”")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("And envía el formulario")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print("Then debería ver un mensaje de exito")
    expect(page.get_by_text("¡Mensaje enviado con éxito!")).to_be_visible()


def test_enviar_formulario_con_campo_obligatorio_email_vacio(page: Page):
    print("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact ”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When rellena el campo obligatorio nombre con “Marta Diaz”")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    print("And rellena el campo obligatorio mensaje con “test mensaje”")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("And pulsa enviar")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print("Then se muestra el mensaje de error el email es obligatorio")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()


def test_enviar_formulario_con_campo_obligatorio_mensaje_vacio(page: Page):
    print("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When rellena el campo obligatorio nombre con “Marta Diaz”")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And rellena el campo obligatorio email con “test_automation@test.com”")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And pulsa enviar")
    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()



def test_enviar_formulario_con_campo_obligatorio_nombre_vacio(page: Page):
    print("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("And hace click en el campo Email")
    page.get_by_role("textbox", name="Email *").click()
    print("And escribe un email válido")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("And hace click en el campo Mensaje")
    page.get_by_role("textbox", name="Mensaje *").click()
    print("And escribe un mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("texto mensaje")
    print("And pulsa enviar")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print ("Then debe ver un mensaje de error “El nombre es obligatorio”")
    expect(page.get_by_text("El nombre es obligatorio")).to_be_visible()
    
    


def test_enviar_formulario_con_campo_obligatorio_email_invalido(page: Page):
    print ("Given el usuario entra en la página de contacto Contáctanos | Vida Verde “https://web-qa.dev.adalab.es/contact”)")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print ("When rellena el campo obligatorio nombre con “Elisabet QA”")
    page.get_by_role("textbox", name="Nombre *").fill("Elisabet QA")
    print ("And rellena el campo obligatorio email con “email”")
    page.get_by_role("textbox", name="Email *").fill("email")
    print ("And rellena el campo obligatorio mensaje con “test mensaje”")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print ("And pulsa enviar")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print ("Then debe ver un mensaje de error “El formato del email no es válido”")
    expect(page.get_by_text("El formato del email no es válido")).to_be_visible()
