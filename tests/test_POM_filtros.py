from playwright.sync_api import Page
from pages.productos_page import ProductosPage


# Realizado por Ana

def test_filtrar_nombre_categoria_precio_valido(page: Page):
    productos= ProductosPage(page)

    print("Given: La usuaria abre la página de productos?Via Verde")
    productos_page.open_productos_page()

    print("When: La usuaria filtra por nombre 'Regadera'")
    productos_page.fill_filter_name("Regadera") 

    print("And filtra por categoría 'Herramientas'")  
    productos_page.select_filter_category("Herramientas")

    print("And filtra por precio mínimo '20'")
    productos_page.fill_filter_min_price("20")

    print("And filtrar por precio máximo '25'")
    productos_page.fill_filter_max_price("25")

    print("Then debe ver el producto 'Regadera Metálica'")
    productos_page.verify_productos_name("Regadera Metalica")


 
# Realizado por Ana
def test_filtrar_valor_sin_resultados(page: Page):
    productos_page = ProductosPage(page)

    print("Given la usuaria entra en la página de productos")
    productos_page.open_productos_page()

    print("When filtra por el nombre 'manzana'")
    productos_page.fill_filter_name("manzana")

    print("Then debería ver el mensaje 'No se encontraron productos'")
    productos_page.verify_no_results_message("No se encontraron productos")    








