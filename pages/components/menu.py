from playwright.sync_api import Page, expect

class Menu:

    def __init__(self, page: Page):
        self.page = page
        self.menu_quienes_somos = "Quiénes Somos"
        self.menu_productos = "Productos"
        self.menu_contactos = "Contacto"
        self.menu_mobile = "Abrir menú principal"

    def esMobile (self):
        ancho = self.page.viewport_size['width']
        if ancho < 1024:
            return True;
        else:
            return False;


    def abrir_menu_quienes_somos (self):
        if(self.esMobile()):
            #Mobile
            print("Navegando en móvil")
            self.page.get_by_role("button", name=self.menu_mobile).click()
            self.page.get_by_role("menuitem", name=self.menu_quienes_somos).click()
        else:
            #Desktop
            print("Navegando en escritorio")
            self.page.get_by_role("link", name=self.menu_quienes_somos).click()




    def abrir_menu_productos (self):
        if(self.esMobile()):
            #Mobile
            print("Navegando en móvil")
            self.page.get_by_role("button", name=self.menu_mobile).click()
            self.page.get_by_role("menuitem", name=self.menu_productos).click()
        else:
            #Desktop
            print("Navegando en escritorio")
            self.page.get_by_role("link", name=self.menu_productos).click()


    
    def abrir_menu_contactos (self):
        if(self.esMobile()):
            #Mobile
            print("Navegando en móvil")
            self.page.get_by_role("button", name=self.menu_mobile).click()
            self.page.get_by_role("menuitem", name=self.menu_contactos).click()
        else:
            #Desktop
            print("Navegando en escritorio")
            self.page.get_by_role("link", name=self.menu_contactos).click()

