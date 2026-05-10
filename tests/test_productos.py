from playwright.sync_api import Page
from pages.contact_page import ContactoPage



def test_productos_page(page: Page):
    productos_page = ProductosPage(page);

    print("When el usuario abre la pagina de productos")
    productos_page.open_productos_page()

    print("Then el usuario ve la categoria del producto “plantas”")
    productos_page.verify_productos_category("Plantas")

    print("And el usuario ve el nombre del producto “Fycus Lyrata”")
    productos_page.verify_productos_name("Ficus Lyrata")

    print("And el usuario ve el precio del producto “35.00 euros”")
    productos_page.verify_productos_price("35.00 €")