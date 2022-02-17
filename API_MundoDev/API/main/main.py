
class API:
    def buscar_dados(query):
        import requests
        import json

        request = requests.get(f"http://ip-api.com/json/{query}")
        dados = json.loads(request.content)

        return dados

    def salvar_dados(ip, dado, planilha):
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
