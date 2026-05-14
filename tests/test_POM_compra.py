from playwright.sync_api import Page
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.productos_page import ProductosPage
from pages.cart_page import CartPage


#Realizado por Lorena
def test_compra_con_tarjeta_vacia(page: Page):

    checkout_page = CheckoutPage (page)
    productos_page = ProductosPage (page)
    cart_page = CartPage (page)

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.abrir_productos_page()

    print("When filtra por nombre “Palas”")
    productos_page.filtrar_por_categoria ("Palas")

    print("And agrega el producto al carrito")
    productos_page.añadir_producto("Juego de Palas")

    print("And visita la página del carrito")
    cart_page.abrir_cart_page()

    print("And hace click en proceder al pago")
    cart_page.hacer_click_pago()

    print("When rellena el campo de nombre válido “Maria Díaz”")
    checkout_page.rellenar_nombre_contacto("María Díaz")

    print("And rellena el campo email válido “test@gmail.com”")
    checkout_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion válida “Calle Aragón, 25, Madrid”")
    checkout_page.rellenar_direccion_contacto("Calle Aragón 25 Madrid")

    print("And hace click en completar compra")
    checkout_page.completar_click_compra()

    print("Then el usuario permanece en la página de check out Finalizar Compra | Vida Verde ")
    checkout_page.visualizar_checkout_compra()

#Realizado por Lorena
def test_compra_con_tarjeta_invalida(page: Page):
    
    checkout_page = CheckoutPage (page)
    productos_page = ProductosPage (page)
    cart_page = CartPage (page)

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.abrir_productos_page()

    print("When filtra por nombre “Palas”")
    productos_page.filtrar_por_nombre("Palas")

    print("And agrega el producto al carrito")
    productos_page.añadir_producto("Juego de Palas")

    print("And visita la página del carrito")
    cart_page.abrir_cart_page()

    print("And hace click en proceder al pago")
    cart_page.hacer_click_pago()

    print("When rellena el campo de nombre valido “Maria Díaz”")
    checkout_page.rellenar_nombre_contacto("Maria Díaz")

    print("And rellena el campo email válido “test@gmail.com”")
    checkout_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion válida “Calle Aragón, 25, Madrid”")
    checkout_page.rellenar_direccion_contacto("Calle Aragón 25 Madrid")

    print("And añade número de tarjeta inválido “1111 4242 4242 4242”")
    checkout_page.añadir_tarjeta("1111 4242 4242 4242")

    print("And hace click en completar compra")
    checkout_page.completar_click_compra()

    print("Then debe ver un mensaje de error en la tarjeta")
    checkout_page.verificar_error_tarjeta("Tarjeta de crédito no válida")


    #Realizado por Eli
def test_compra_datos_validos (page: Page):

    productos_page = ProductosPage (page)
    cart_page = CartPage (page)
    checkout_page = CheckoutPage (page)
    confirmation_page = ConfirmationPage (page)


    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    productos_page.abrir_productos_page()
    print ("Filtra por nombre de producto 'Palas'")
    productos_page.filtrar_por_categoria()
    print ("Añade el artículo 'Juego de Palas'")
    productos_page.añadir_producto()
    print ("Visita la página del carrito")
    cart_page.abrir_cart_page()
    print ("Hace clic en proceder al pago")
    cart_page.hacer_click_pago()

    print ("Comprueba el 'Resumen del pedido'")
    checkout_page.verifica_resumen_compra()
    print("Ve el producto 'Juego de palas'")
    checkout_page.verificar_producto_compra("Juego de Palas")
    print("Verifica el precio del producto")
    checkout_page.verificar_precio_compra("Juego de Palas '15,99 €'")
    print("Ve el IVA '3,36 €'")
    checkout_page.verificar_iva_compra("3,36 €")
    print("Ve el envío '5 €'")
    checkout_page.verificar_envio_compra("5 €")
    print("Ve el total de compra por importe '24,35€'")
    checkout_page.verificar_total_compra("24,35 €")
    print ("Rellena el nombre 'Marta Díaz'")
    checkout_page.rellenar_nombre_contacto()
    print ("Rellena el email 'test@gmail.com'")
    checkout_page.rellenar_email_contacto()
    print ("Rellena la dirección 'Calle Aragón, 25, Madrid'")
    checkout_page.rellenar_direccion_contacto()
    print ("Rellena el número de la tarjeta '4242 4242 4242 4242'")
    checkout_page.añadir_tarjeta()
    print ("Hace clic en completar compra")
    checkout_page.completar_click_compra("4242 4242 4242 4242")

    print ("Comprueba el resumen del pedido completado confirmando el mensaje de '¡Compra realizada con éxito!'")
    confirmation_page.verificar_compra_realizada()
    print("Ve el producto 'Juego de palas' por valor '15,99€'")
    confirmation_page.verificar_producto_y_valor()
    print("Ve el IVA '3,36€'")
    confirmation_page.verificar_IVA()
    print("Ve el envío '5€'")
    confirmation_page.verificar_envio()
    print("Ve el total de compra por importe '24,35€'")
    confirmation_page.verificar_total_compra()
    print ("Hace clic en 'Volver a la tienda'")
    confirmation_page.hace_clic_volver_tienda()
 
    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    productos_page.abrir_productos_page()