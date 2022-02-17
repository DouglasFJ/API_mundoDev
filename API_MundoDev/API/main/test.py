
from main import API

ip = str(input('IP:'))
a = API.buscar_dados(ip)


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


salvar_dados(ip, a, 'database.xlsx')
