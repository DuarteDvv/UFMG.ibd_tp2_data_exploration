# %%
## Connect

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../../Database/tp2.db')

# %% query atrasados
query = """
SELECT ea2.sigla, hj.mortes , ea2.total_fund, ea2.total_em
FROM (SELECT ea.sigla , AVG(ea.total_fund) as total_fund, AVG(ea.total_em) as total_em
FROM estudos_atrasados ea
WHERE ea.tipo_local = 'Total' and ea.tipo_escola = 'Total'
GROUP BY ea.sigla ) ea2
JOIN homicidios_jovens hj on hj.sigla = ea2.sigla
"""

df = pd.read_sql(query, conn)
print(df)

plt.figure(figsize=(10, 6))

plt.scatter(df['total_fund'], df['mortes'], color='blue', label='Fundamental')

plt.scatter(df['total_em'], df['mortes'], color='green', label='Em')

plt.xlabel('atrasados')
plt.ylabel('homicidios')
plt.legend()

plt.show()
# %%
# %% query aprovados
query = """
SELECT tara2.sigla, hj.mortes , tara2.total_aprov_fund, tara2.total_aprov_em
FROM (SELECT sigla, AVG(total_aprov_fund) AS total_aprov_fund , AVG(total_aprov_em) as total_aprov_em
FROM taxas_aprov_reprov_aband 
WHERE tipo_local = 'Total' and tipo_escola = 'Total'
GROUP BY sigla ) tara2
JOIN homicidios_jovens hj on hj.sigla = tara2.sigla
"""

df = pd.read_sql(query, conn)
print(df)

plt.figure(figsize=(10, 6))

plt.scatter(df['total_aprov_fund'], df['mortes'], color='blue', label='Fundamental')

plt.scatter(df['total_aprov_em'], df['mortes'], color='green', label='Em')

plt.xlabel('aprovados')
plt.ylabel('homicidios')
plt.legend()

plt.show()
# %%
# %% query reprovados
query = """
SELECT tara2.sigla, hj.mortes , tara2.total_reprov_fund, tara2.total_reprov_em
FROM (SELECT sigla, AVG(total_reprov_fund) AS total_reprov_fund , AVG(total_reprov_em) as total_reprov_em
FROM taxas_aprov_reprov_aband 
WHERE tipo_local = 'Total' and tipo_escola = 'Total'
GROUP BY sigla ) tara2
JOIN homicidios_jovens hj on hj.sigla = tara2.sigla
"""

df = pd.read_sql(query, conn)
print(df)

plt.figure(figsize=(10, 6))

plt.scatter(df['total_reprov_fund'], df['mortes'], color='blue', label='Fundamental')

plt.scatter(df['total_reprov_em'], df['mortes'], color='green', label='Em')

plt.xlabel('reprovados')
plt.ylabel('homicidios')
plt.legend()

plt.show()
# %%
