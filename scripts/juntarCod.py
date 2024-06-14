import pandas as pd

def processar_csv(arquivo_entrada, arquivo_saida):
    
    df = pd.read_csv(arquivo_entrada, delimiter=';', dtype={'COD. UF': str, 'COD. MUNIC': str})
    
  
    df["COD"] = df["COD. UF"] + df["COD. MUNIC"]
    
   
    df["COD"] = df["COD"].astype(str)
    
 
    print(df)
    
  
    df.to_csv(arquivo_saida, index=False, sep=';')


arquivo_entrada = ''
arquivo_saida = ''

processar_csv(arquivo_entrada, arquivo_saida)
