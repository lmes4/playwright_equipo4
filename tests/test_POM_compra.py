from playwright.sync_api import Page
from pages.checkout_page import CompraPage
from pages.productos_page import ProductosPage
from pages.cart_page import CartPage


#Realizado por Lorena
def test_compra_con_tarjeta_vacia(page: Page):

    compra_page = CompraPage ()
    productos_page = ProductosPage ()
    cart_page = CartPage ()

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.abrir_productos_page()

    print("When filtra por nombre “palas”")
    compra_page.filtrar_productos_category ("palas")

    print("And agrega el producto al carrito")
    compra_page.agregar_productos_carrito()

    print("And visita la página del carrito")
    cart_page.abrir_cart_page

    print("And hace click en proceder al pago")
    compra_page.hacer_click_pago()

    print("Then debe ver el resumen del pedido con")
    compra_page.verifica_resumen_compra("Resumen del pedido")

    print("then debe ver el producto “juego de palas”")
    compra_page.verificar_producto_compra("Juego de Palas")

    print("then debe ver precio del producto “15.99”")
    compra_page.verificar_precio_compra("15.99")

    print("then debe ver el subtotal “15.99”")
    compra_page.verificar_subtotal_compra("15.99")

    print("then debe ver el IVA “3.36”")
    compra_page.verificar_iva_compra("3.36")

    print("then debe ver el envio “5”")
    compra_page.verificar_envio_compra("5")

    print("and debe ver el total “24”")
    compra_page.verificar_total_compra("24")

    print("When rellena el campo de nombre válido “Maria Diaz”")
    compra_page.rellenar_nombre_contacto("Maria Diaz")

    print("And rellena el campo email válido “test@gmail.com”")
    compra_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion valida “Calle Aragon, 25, Madrid”")
    compra_page.rellenar_direccion_contacto("Calle Aragon 25 Madrid")

    print("And hace click en completar compra")
    compra_page.completar_click_compra()

    print("Then el usuario permanece en la página de check out Finalizar Compra | Vida Verde ")
    compra_page.visualizar_checkout_compra

#Realizado por Lorena
def test_compra_con_tarjeta_invalida(page: Page):
    
    compra_page = CompraPage ()
    productos_page = ProductosPage ()
    cart_page = CartPage ()

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.abrir_productos_page()

    print("When filtra por nombre “palas”")
    compra_page.filtrar_productos_category ()

    print("And agrega el producto al carrito")
    compra_page.agregar_productos_carrito()

    print("And visita la página del carrito")
    cart_page.abrir_cart_page

    print("And hace click en proceder al pago")
    compra_page.hacer_click_pago()

    print("Then debe ver el resumen del pedido con")
    compra_page.verifica_resumen_compra("Resumen del pedido")

    print("then debe ver el producto “juego de palas”")
    compra_page.verificar_producto_compra("Juego de Palas")

    print("then debe ver precio del producto “15.99”")
    compra_page.verificar_precio_compra("15.99")

    print("then debe ver el subtotal “15.99”")
    compra_page.verificar_subtotal_compra("15.99")

    print("then debe ver el IVA “3.36”")
    compra_page.verificar_iva_compra("3.36")

    print("then debe ver el envio “5”")
    compra_page.verificar_envio_compra("5")

    print("and debe ver el total “24”")
    compra_page.verificar_total_compra("24")

    print("When rellena el campo de nombre válido “Maria Diaz”")
    compra_page.rellenar_nombre_contacto("Maria Diaz")

    print("And rellena el campo email válido “test@gmail.com”")
    compra_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion valida “Calle Aragon, 25, Madrid”")
    compra_page.rellenar_direccion_contacto("Calle Aragon 25 Madrid")

    print("And añade número de tarjeta invalido “1111 4242 4242 4242”")
    compra_page.añadir_tarjeta_invalida("1111 4242 4242 4242")

    print("And hace click en completar compra")
    compra_page.completar_click_compra()

    print("Then debe ver un mensaje de error en la tarjeta")
    compra_page.verificar_error_tarjeta("Tarjeta de credito no valida")


    #Realizado por Eli
def test_compra_datos_validos (page: Page):

    productos_page = ProductosPage ()
    cart_page = CartPage ()
    compra_page = CompraPage ()


    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    productos_page.abrir_productos_page
    print ("Filtra por nombre de producto 'Palas'")
    productos_page.filtrar_por_categoria()
    print ("Añade el artículo 'Juego de Palas'")
    productos_page.añadir_producto()
    print ("Visita la página del carrito")
    cart_page.abrir_cart_page()
    print ("Hace clic en proceder al pago")
    cart_page.hacer_click_pago()

    print ("Comprueba el 'Resumen del pedido'")
    checkpout_page.ver
    expect(page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()


    print("Ve el producto 'Juego de palas'")
    expect(page.get_by_text("Juego de Palas15.99 €")).to_be_visible()
    print("Ve el IVA '3,36€'")
    expect(page.get_by_text("IVA (21%)3.36 €")).to_be_visible()
    print("Ve el envío '5€'")
    expect(page.get_by_text("Envío5.00 €")).to_be_visible()
    print("Ve el total de compra por importe '24,35€'")
    expect(page.get_by_text("Total24.35 €")).to_be_visible()

    print ("Rellena el nombre 'Marta Díaz'")
    page.get_by_role("textbox", name="Nombre Completo *").fill("Marta Díaz")
    print ("Rellena el email 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print ("Rellena la dirección 'Calle Aragón, 25, Madrid'")
    page.get_by_role("textbox", name="Dirección *").fill("Calle Aragón, 25, Madrid")
    print ("Rellena el número de la tarjeta '4242 4242 4242 4242'")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("4242424242424242")
    print ("Hace clic en completar compra")
    page.get_by_role("button", name="Completar Compra").click()
    print ("Comprueba el resumen del pedido completado confirmando el mensaje de '¡Compra realizada con éxito!'")
    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    print("Ve el producto 'Juego de palas' por valor '15,99€'")
    expect(page.get_by_text("Juego de Palas15.99 €")).to_be_visible()
    print("Ve el IVA '3,36€'")
    expect(page.get_by_text("IVA (21%)3.36 €")).to_be_visible()
    print("Ve el envío '5€'")
    expect(page.get_by_text("Envío5.00 €")).to_be_visible()
    print("Ve el total de compra por importe '24,35€'")
    expect(page.get_by_text("Total24.35 €")).to_be_visible()    

    
    print ("Hace clic en 'Volver a la tienda'")
    page.get_by_role("link", name="Volver a la Tienda").click()   
    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")
