import csv
import re

# Função para remover parênteses e seu conteúdo
def remover_parenteses_conteudo(linha):
    # Usa uma expressão regular para encontrar e remover parênteses e o conteúdo dentro deles
    linha_limpa = re.sub(r'\s*\([^)]*\)', '', linha)
    return linha_limpa.strip()

# Caminho para o arquivo de entrada e o arquivo de saída
caminho_entrada = 'raw_data_csv_converted/POP2021_20230710_tratado.csv'
caminho_saida = 'raw_data_csv_converted/POP2021_20230710_final.csv'

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(caminho_entrada, mode='r', encoding='utf-8') as arquivo_entrada, \
     open(caminho_saida, mode='w', encoding='utf-8', newline='') as arquivo_saida:
    
    # Cria um leitor e um escritor de CSV
    leitor_csv = csv.reader(arquivo_entrada, delimiter=';')
    escritor_csv = csv.writer(arquivo_saida, delimiter=';')
    
    # Processa cada linha do arquivo de entrada
    for linha in leitor_csv:
        # Junta a linha em uma string, remove os parênteses e o conteúdo dentro deles
        linha_processada = remover_parenteses_conteudo(';'.join(linha))
        # Divide a linha processada de volta em uma lista e escreve no arquivo de saída
        escritor_csv.writerow(linha_processada.split(';'))
