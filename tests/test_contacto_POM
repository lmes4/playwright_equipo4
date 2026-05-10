def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):

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


def test_form_with_required_email_field_left_empty(page: Page):

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
    
