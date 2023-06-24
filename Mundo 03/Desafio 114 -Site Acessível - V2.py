from selenium import webdriver
from selenium.webdriver.edge.options import Options
import urllib
import urllib.request

try:
    pudim = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print(f'Não Consigo Acessar o site')
else:
    print(f'Consigo Acessar o site')
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
    driver.get('http://pudim.com.br/')
