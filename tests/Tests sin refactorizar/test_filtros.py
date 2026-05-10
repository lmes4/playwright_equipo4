from playwright.sync_api import Page, expect

#Realizado por Ana
def test_filtrar_nombre_categoria_precio_valido(page: Page):
    print("Given la usuaria abre la página de 'Nuestros Productos | Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When la usuaria filtra por nombre 'Regadera'")
    page.get_by_role("searchbox", name="Nombre").fill("Regadera")

    print("And filtra por categoría 'Herramientas'")
    page.get_by_label("Categoría").select_option("Herramientas")

    print("And filtra por precio mínimo '20'")
    page.get_by_role("spinbutton", name="Precio mínimo").fill("20")

    print("And filtra por precio máximo '25'")
    page.get_by_role("spinbutton", name="Precio máximo").fill("25")

    print("Then debe ver el producto 'Regadera Metálica'")
    expect(page.get_by_text("Regadera Metálica")).to_be_visible()


#Realizado por Ana
def test_filtrar_valor_sin_resultados(page: Page):
    print("Given la usuaria abre la página de 'Nuestros Productos | Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When la usuaria filtra por el nombre 'manzana'")
    page.get_by_role("searchbox", name="Nombre").fill("manzana")

    print("Then se muestra el mensaje 'No se encontraron productos'")
    expect(page.get_by_text("No se encontraron productos")).to_be_visible()