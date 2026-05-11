from playwright.sync_api import Page, expect
from pages.components.menu import MenuPage


#Realizado por Elisabet
def test_visitar_los_enlaces_del_menú(page: Page):

    menu_page = MenuPage()

    print("Cuando el usuario abre la página Inicio | Vida Verde “https://web-qa.dev.adalab.es”")
    page.goto("https://web-qa.dev.adalab.es")

    print ("Ve el título 'Vida Verde'")
    expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()

    print ("Hace click en 'Quiénes Somos'")
    page.get_by_role("link", name="Quiénes Somos").click()

    print ("Ve el título 'Quiénes Somos'")
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()

    print ("Ve la URL https://web-qa.dev.adalab.es/about")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/about")

    print ("Hace click en 'Productos'")
    page.get_by_role("link", name="Productos").click()

    print ("Ve el título 'Catálogo de Productos'")
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")

    print ("Hace click en 'Contacto'")
    page.get_by_role("link", name="Contacto").click()

    print ("Ve el título 'Contáctanos'")
    expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()

    print ("Ve la URL https://web-qa.dev.adalab.es/contact")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/contact")
