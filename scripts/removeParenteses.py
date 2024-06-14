import csv
import re

def remover_parenteses_conteudo(linha):
    
    linha_limpa = re.sub(r'\s*\([^)]*\)', '', linha)
    return linha_limpa.strip()


caminho_entrada = ''
caminho_saida = ''

with open(caminho_entrada, mode='r', encoding='utf-8') as arquivo_entrada, \
     open(caminho_saida, mode='w', encoding='utf-8', newline='') as arquivo_saida:
    
    leitor_csv = csv.reader(arquivo_entrada, delimiter=';')
    escritor_csv = csv.writer(arquivo_saida, delimiter=';')
    
    for linha in leitor_csv:

        linha_processada = remover_parenteses_conteudo(';'.join(linha))
        escritor_csv.writerow(linha_processada.split(';'))
