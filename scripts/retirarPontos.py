import pandas as pd


def remover_pontos(s):
    if isinstance(s, str):
        return s.replace('.', '')
    return s


caminho_entrada = 'raw_data_csv_converted/municipios_final.csv'  
caminho_saida = 'raw_data_csv_converted/municipios__final.csv'  


df = pd.read_csv(caminho_entrada)


df = df.applymap(remover_pontos)


df.to_csv(caminho_saida, index=False)

print(f'Arquivo salvo como {caminho_saida}')
