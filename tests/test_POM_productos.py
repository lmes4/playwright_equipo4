from playwright.sync_api import Page
from pages.productos_page import ProductosPage


#Realizado por Lorena
def test_productos_page(page: Page):
    productos_page = ProductosPage(page);

    print("When el usuario abre la página de productos")
    productos_page.abrir_productos_page()

    print("Then el usuario ve la categoría del producto “Plantas”")
    productos_page.verificar_productos_category("Plantas")

    print("And el usuario ve el nombre del producto “Fycus Lyrata”")
    productos_page.verificar_productos_name("Ficus Lyrata")

    print("And el usuario ve el precio del producto “35.00 €")
    productos_page.verificar_productos_price("35.00 €")