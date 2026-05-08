from playwright.sync_api import Page, expect

def test_visitar_los_enlaces_del_menú(page: Page):
    print("Given el usuario abre la página Inicio | Vida Verde “https://web-qa.dev.adalab.es/”")
    page.goto("https://web-qa.dev.adalab.es/")
    expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()
    page.get_by_role("link", name="Quiénes Somos").click()
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()
    page.get_by_role("link", name="Productos").click()
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()
    page.get_by_role("link", name="Contacto").click()
    expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()

    