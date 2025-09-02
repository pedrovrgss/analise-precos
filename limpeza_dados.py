import pandas as pd

arquivos = [
    "julho25.xlsx", "junho25.xlsx", "maio25.xlsx", "abril25.xlsx",
    "marco25.xlsx", "fevereiro25.xlsx", "janeiro25.xlsx",
    "dezembro24.xlsx", "novembro24.xlsx", "outubro24.xlsx",
    "setembro24.xlsx", "agosto24.xlsx"
]

arq_geral = "tabelas/dados.xlsx"
colunas = [
            'Mês', 'Ano', 'Alimentação e bebidas',
            'Habitação', 'Artigos de residência', 'Vestuário',
            'Transportes', 'Saúde e cuidados pessoais', 
            'Despesas pessoais', 'Educação', 'Comunicação'
           ]

def getMes(arquivo):
    return arquivo.split('.')[0][:-2].capitalize()

def getAno(arquivo):
    return f"20{arquivo.split('.')[0][-2:]}"

for arquivo in arquivos:
    arq = pd.read_excel("tabelas/" + arquivo)

    mes = getMes(arquivo)
    ano = getAno(arquivo)

    
    
