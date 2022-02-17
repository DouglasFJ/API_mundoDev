from main import API

ip = str(input('IP'))

dados = API.buscar_dados(ip)
API.salvar_dados(ip, dados, "database.xlsx")
print('FUNCIONOOOOOOOOOO AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
"""
Fazer a função que deleta o database
"""
"""
criar um endpoit
"""
