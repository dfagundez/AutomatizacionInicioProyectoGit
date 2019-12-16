import sys
import os
from  selenium import webdriver


# Espesifico la ruta de la carpeta que va a contener mis proyectos
path = "C:/Users/Home/Documents/MyProjects/"
browser = webdriver.Chrome()
browser.get('http://github.com/login')

# Creo funcion para:
# - Crear carpeta del nuevo proyecto
# - Loguearme en GitHub
# - Crear nuevo repositorio
# La carpeta y el repositorio toman el nombre que se pasa como argumento
def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    python_button = browser.find_element_by_id('login_field')
    python_button.send_keys('yourname@mail.com')
    python_button = browser.find_element_by_id('password')
    python_button.send_keys('yourpassword')
    python_button = browser.find_element_by_name('commit')
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_element_by_id('repository_name')
    python_button.send_keys(folderName)
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()
    browser.quit()

if __name__ == "__main__":
    create()