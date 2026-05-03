from playwright.sync_api import Page, expect

def test_enviar_formulario_con_campo_obligatorio_email_vacio(page: Page):
    print("Given user visit homepage")
    page.goto("https://bootcampqa.com")
    

