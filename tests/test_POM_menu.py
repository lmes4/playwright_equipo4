from playwright.sync_api import Page, expect
from pages.about_us_pages import AboutusPage
from pages.components.menu import Menu
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.productos_page import ProductosPage



#Realizado por Elisabet
def test_visitar_los_enlaces_del_menú(page: Page):

    home_page = HomePage(page)
    menu = Menu(page)
    about_us_page = AboutusPage(page)
    productos_page = ProductosPage (page)
    contact_page = ContactPage (page)

    print("Cuando el usuario abre la página Inicio | Vida Verde “https://web-qa.dev.adalab.es”")
    home_page.abrir_pagina_inicio()

    print ("Ve el título 'Vida Verde'")
    home_page.verificar_pagina_inicio()


    print ("Hace click en 'Quiénes Somos'")
    menu.abrir_menu_quienes_somos()

    print ("Ve el título 'Quiénes Somos'")
    about_us_page.verificar_titulo_quienes_somos()

    print ("Ve la URL https://web-qa.dev.adalab.es/about")
    about_us_page.verificar_quienes_somos_url()


    print ("Hace click en 'Productos'")
    menu.abrir_menu_productos()

    print ("Ve el título 'Catálogo de Productos'")
    productos_page.verificar_productos_title()

    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    productos_page.verificar_productos_url()


    print ("Hace click en 'Contacto'")
    menu.abrir_menu_contactos()

    print ("Ve el título 'Contáctanos'")
    contact_page.verificar_titulo_contacto()

    print ("Ve la URL https://web-qa.dev.adalab.es/contact")
    contact_page.verificar_contacto_url()
