def test_carrito_agregar_productos_al_carrito_ver_resumen_y_vaciar_carrito(page: Page):
    def run(playwright: Playwright) -> None:
    page.goto("https://web-qa.dev.adalab.es/products")
    page.get_by_role("searchbox", name="Nombre").click()
    page.get_by_role("searchbox", name="Nombre").fill("sansevieria")
    page.get_by_role("button", name="Añadir Sansevieria al carrito").click()
    page.get_by_role("button", name="Quitar filtros y ver todos").click()
    page.get_by_role("searchbox", name="Nombre").click()
    page.get_by_role("searchbox", name="Nombre").fill("maceta de barro")
    page.get_by_role("button", name="Añadir Maceta de Barro Grande").click()
    page.get_by_role("link", name="Carrito de compra").click()
    page.get_by_role("heading", name="Sansevieria").click()
    page.get_by_text("Plantas").click()
    page.get_by_text("22.00 €").click()
    page.get_by_role("heading", name="Maceta de Barro Grande").click()
    page.get_by_text("Macetas").click()
    page.get_by_text("10.50 €").click()
    page.get_by_role("heading", name="Resumen del Pedido").click()
    page.get_by_text("Productos (2)32.50 €").click()
    page.get_by_text("IVA (21%)6.83 €").click()
    page.get_by_text("Envío5.00 €").click()
    page.get_by_text("Total44.33 €").click()
    page.get_by_role("button", name="Vaciar Carrito").click()
    page.get_by_text("Tu carrito está vacío").click()





def test_carrito_quitar_productos_del_carrito_y_ver_resumen(page: Page):
    page.goto("https://web-qa.dev.adalab.es/products")
    expect(page.get_by_role("searchbox", name="Nombre")).to_be_visible()
    page.get_by_role("searchbox", name="Nombre").click()
    page.get_by_role("searchbox", name="Nombre").fill("ficus")
    page.get_by_role("button", name="Añadir Ficus Lyrata al carrito").click()
    page.get_by_role("button", name="Quitar filtros y ver todos").click()
    page.get_by_role("searchbox", name="Nombre").click()
    page.get_by_role("searchbox", name="Nombre").fill("tijeras")
    page.get_by_role("button", name="Añadir Tijeras de Podar al carrito").click()
    page.get_by_role("link", name="Finalizar Compra").click()
    page.get_by_role("button", name="Eliminar Ficus Lyrata del carrito").click()
    page.locator("div").filter(has_text=re.compile(r"^HerramientasTijeras de Podar18\.50 €Eliminar$")).click()
    page.get_by_role("complementary", name="Resumen del Pedido").click()
    page.get_by_text("Productos (1)18.50 €").click()
    page.get_by_text("IVA (21%)3.88 €").click()
    page.get_by_text("Envío5.00 €").click()
    page.get_by_text("Total27.38 €").click()













