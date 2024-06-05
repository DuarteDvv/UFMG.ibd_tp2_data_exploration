import pandas as pd

def xls_to_csv(input_file, output_file):
    df = pd.read_excel(input_file)
    df.to_csv(output_file, index=False)


input_file = 'raw_data_xlsx\estudos_atrasados_2021.xlsx'
output_file = 'raw_data_xlsx\estudos_atrasados_2021.csv'

xls_to_csv(input_file, output_file)

