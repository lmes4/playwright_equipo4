from playwright.sync_api import Page, expect
from pages.about_us_pages import AboutusPage
from pages.components.menu import Menu
from pages.home_page import HomePage



#Realizado por Elisabet
def test_visitar_los_enlaces_del_menú(page: Page):

    home_page = HomePage(page)
    menu = Menu()
    about_us_page = AboutusPage(page)

    print("Cuando el usuario abre la página Inicio | Vida Verde “https://web-qa.dev.adalab.es”")
    home_page.abrir_pagina_inicio()

    print ("Ve el título 'Vida Verde'")
    home_page.verificar_pagina_inicio()

    print ("Hace click en 'Quiénes Somos'")
    menu.abrir_menu_quienes_somos()

    print ("Ve el título 'Quiénes Somos'")
    about_us_page.verificar_titulo_quienes_somos()





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
