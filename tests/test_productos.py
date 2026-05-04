from playwright.sync_api import Page, expect

def test_ver_productos(page: Page):
    print("When el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    page.goto("https://web-qa.dev.adalab.es/products")
    print("Then el usuario ve la categoría del producto “plantas”")
    expect(page.get_by_text("Plantas").nth(2)).to_be_visible()
    print("And el usuario ve el nombre del producto “Fycus Lyrata”")
    page.get_by_role("heading", name="Ficus Lyrata").click()
    print("And el usuario ve el precio del producto “35.00 euros”")
    page.get_by_text("35.00 €").click()

