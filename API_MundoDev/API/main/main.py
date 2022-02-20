"""Parte principal do projeto aqui é onde estão as funções
que consulta o IP na IP-API e salva esses dados na planilha Excel"""
class API:
    def buscar_dados(query):
        """Essa função recebe um IP qualquer e retorna um dicionario
        com todos os dados do IP
        query: ip"""
        import requests
        import json

        request = requests.get(f"http://ip-api.com/json/{query}")
        dados = json.loads(request.content)

        return dados

    def salvar_dados(ip, dado, planilha):
        """Essa função recebe o IP ,o dicionario com os dados e o nome da planilha
        e salva esses dados na planilha
        ip: ip solicitado
        dado: O dicionario com os dados que a função 'buscar_dados()' retornou
        planilha: nome da planilha de formato .xlsx(formato das planilhas excel)"""
        import pandas as pd
        ver = False
        try:
            ips = list()
            dados = list()
            read = pd.read_excel(planilha)
            for i in read['IP']:
                ips.append(i)
            for d in read['Dados']:
                dados.append(d)
            ips.append(ip)
            dados.append(dado)
            ver = True
        except FileNotFoundError:
            pass

        writer = pd.ExcelWriter(planilha)
        if ver is True:
            df = pd.DataFrame({'IP': ips, 'Dados': dados})
        else:
            df = pd.DataFrame({'IP': [ip], 'Dados': [dado]})
        df.to_excel(writer, sheet_name='database', index=False)
        writer.save()

    def del_data(arquivo):
        """uma função complemetar que exclui qualquer arquivo
        no caso dessa API exclui a base de dados que é a Planilha excel"""
        from os import remove
        remove(arquivo)
