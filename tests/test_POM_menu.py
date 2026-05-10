from playwright.sync_api import Page, expect
from pages.components.menu import MenuPage


#Realizado por Elisabet
def test_visitar_los_enlaces_del_menú(page: Page):

    menu_page = MenuPage()