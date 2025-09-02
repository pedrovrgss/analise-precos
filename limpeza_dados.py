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

df = pd.DataFrame()

for arquivo in arquivos:
    try:
        caminho_completo = "tabelas/" + arquivo

        aux = pd.read_excel(caminho_completo, header=None)

        mes = getMes(arquivo)
        ano = getAno(arquivo)

        pos = (aux == "1.Alimentação e bebidas").stack().idxmax()
        linha_header, col_inicio = pos

        df_aux = pd.read_excel(
            caminho_completo, 
            header=linha_header, 
            usecols=range(col_inicio, col_inicio + 9)
        )
        
        df_aux = df_aux.iloc[[1]]

        df_aux.columns = df_aux.columns.str.replace(r'^\d+\.', '', regex=True).str.strip()

        df_aux.insert(0, "Ano", ano)
        df_aux.insert(0, "Mês", mes)

        df = pd.concat([df, df_aux], ignore_index=True)

    except FileNotFoundError:
        print(f"ERRO: O arquivo {caminho_completo} não foi encontrado. Pulando...")
        continue
    except ValueError:
        print(f"ERRO: Não foi possível encontrar a célula '1.Alimentação e bebidas' no arquivo {caminho_completo}. Pulando...")
        continue
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar {arquivo}: {e}")
        continue

df = df[colunas]

df.to_excel(arq_geral, index=False)

print("\nConsolidação concluída com sucesso!")
print(f"Arquivo final salvo em: {arq_geral}\n")