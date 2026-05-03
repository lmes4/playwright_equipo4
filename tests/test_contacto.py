from playwright.sync_api import Page, expect

def test_enviar_formulario_con_campos_obligatorios_validos(page: Page):
    print("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact ”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When rellena el nombre con “Marta Diaz”")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    print("And rellena el email con “test_automation@test.com”")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("and rellena el mensaje con “test mensaje”")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("And envía el formulario")
    expect(page.get_by_role("button", name="Enviar Mensaje")).to_be_visible()


def test_enviar_formulario_con_campo_obligatorio_email_vacío(page: Page):
    print("Given la usuaria abre la página de contacto “https://web-qa.dev.adalab.es/contact ”")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("Cuando rellena el campo obligatorio nombre con “Marta Diaz”")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    print("And rellena el campo obligatorio mensaje con “test mensaje”")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("And pulsa enviar")
    expect(page.get_by_role("button", name="Enviar Mensaje")).to_be_visible()


