import urllib
import urllib.request

try:
    pudim = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print(f'Não Consigo Acessar o site')
else:
    print(f'Consigo Acessar o site')
