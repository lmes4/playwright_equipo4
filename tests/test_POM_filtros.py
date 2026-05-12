from playwright.sync_api import Page
from pages.productos_page import ProductosPage


# Realizado por Ana

def test_filtrar_nombre_categoria_precio_valido(page: Page):
    productos_page= ProductosPage(page)

    print("Given: La usuaria abre la página de productos?Via Verde")
    productos_page.abrir_productos_page()

    print("When: La usuaria filtra por nombre 'Regadera'")
    productos_page.filtrar_por_nombre("Regadera") 

    print("And filtra por categoría 'Herramientas'")  
    productos_page.filtrar_por_categoria("Herramientas")

    print("And filtra por precio mínimo '20'")
    productos_page.filtrar_por_precio_minimo("20")

    print("And filtrar por precio máximo '25'")
    productos_page.filtrar_por_precio_maximo("25")

    print("Then debe ver el producto 'Regadera Metálica'")
    productos_page.verificar_producto_visible("Regadera Metalica")


 
# Realizado por Ana
def test_filtrar_valor_sin_resultados(page: Page):
    productos_page = ProductosPage(page)

    print("Given la usuaria entra en la página de productos")
    productos_page.abrir_productos_page()

    print("When filtra por el nombre 'manzana'")
    productos_page.filtrar_por_nombre("manzana")

    print("Then debería ver el mensaje 'No se encontraron productos'")
    productos_page.verificar_mensaje_no_resultados("No se encontraron productos")    








