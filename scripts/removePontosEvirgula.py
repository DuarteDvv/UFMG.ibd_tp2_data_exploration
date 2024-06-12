# Importa o módulo csv para trabalhar com arquivos CSV
import csv

# Função para remover pontos e vírgulas em excesso no final das linhas
def remover_excesso_pontos_virgulas(linha):
    # Divide a linha em uma lista de campos
    campos = linha.strip().split(';')
    # Remove campos vazios no final da lista de campos
    while campos and not campos[-1]:
        campos.pop()
    # Junta os campos novamente em uma linha, separados por ponto e vírgula
    return ';'.join(campos)

# Caminho para o arquivo de entrada e o arquivo de saída
caminho_entrada = 'raw_data_csv_converted/POP2021_20230710.csv'
caminho_saida = 'raw_data_csv_converted/POP2021_20230710_tratado.csv'

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(caminho_entrada, mode='r', encoding='utf-8') as arquivo_entrada, \
     open(caminho_saida, mode='w', encoding='utf-8', newline='') as arquivo_saida:
    
    # Cria um leitor e um escritor de CSV
    leitor_csv = csv.reader(arquivo_entrada, delimiter=';')
    escritor_csv = csv.writer(arquivo_saida, delimiter=';')
    
    # Processa cada linha do arquivo de entrada
    for linha in leitor_csv:
        # Remove os pontos e vírgulas em excesso e escreve a linha processada no arquivo de saída
        linha_processada = remover_excesso_pontos_virgulas(';'.join(linha))
        escritor_csv.writerow(linha_processada.split(';'))
