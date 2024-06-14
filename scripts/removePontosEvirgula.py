
import csv


def remover_excesso_pontos_virgulas(linha):
   
    campos = linha.strip().split(';')
    
    while campos and not campos[-1]:
        campos.pop()
    
    return ';'.join(campos)


caminho_entrada = ''
caminho_saida = ''


with open(caminho_entrada, mode='r', encoding='utf-8') as arquivo_entrada, \
     open(caminho_saida, mode='w', encoding='utf-8', newline='') as arquivo_saida:
    

    leitor_csv = csv.reader(arquivo_entrada, delimiter=';')
    escritor_csv = csv.writer(arquivo_saida, delimiter=';')
    
 
    for linha in leitor_csv:
       
        linha_processada = remover_excesso_pontos_virgulas(';'.join(linha))
        escritor_csv.writerow(linha_processada.split(';'))
