from bs4 import BeautifulSoup
import requests
import pandas as pd 

#url da pagina alvo

url = 'https://www.themoviedb.org/movie'

#cabeçalho com user -agente para simular um navegador especifico

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }

# fazendo a requisição com o cabeçalho e a url alvo
respose = requests.get(url,headers=headers0)

# verificar se a resposta foi positiva
if response.status_code == 403:
    print(f'Erro{response.status_code}: Não autorizado')
elif response.status_code != 200:
    print(f'Erro{response,status_code}:Não foi possivel acessar a página')

#se passou daqui, tudo deu certo ao capturar a pagina, então vamos realizar o scrapping
else:
    # realizar o parse no conteudo html
    soup = BeautifulSoup(response.text,"html.parser")

   #verificar a estrutura html para ver o que está sendo retornado
    print(soup.prettify()[;1000]) #mostra as 1000 linhas do html para entender a estrutura
    
