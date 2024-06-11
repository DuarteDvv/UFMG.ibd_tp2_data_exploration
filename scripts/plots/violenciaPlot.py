

# %%
## Connect

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../../Database/tp2.db')

# %% query atrasados
query = """
SELECT hByCidade.nm_municipio, hByCidade.sigla, hByCidade.vitimas, ea.total_fund, ea.total_em
FROM (
	SELECT h.nm_municipio, h.sigla, sum(h.vitimas) as vitimas
	from homicidios h 
	group by h.nm_municipio
) hByCidade
LEFT JOIN estados e ON hByCidade.sigla = e.sigla
LEFT JOIN estudos_atrasados ea ON hByCidade.nm_municipio = ea.nm_municipio AND hByCidade.sigla = ea.sigla
WHERE ea.tipo_local = 'Total' and ea.tipo_escola = 'Total'
"""

df = pd.read_sql(query, conn)
df

plt.figure(figsize=(10, 6))

plt.scatter(df['total_fund'], df['vitimas'], color='blue', label='Fundamental')

plt.scatter(df['total_em'], df['vitimas'], color='green', label='Em')

plt.xlabel('atrasados')
plt.ylabel('homicidios')
plt.legend()

plt.show()

# %% query aprovados
query = """
SELECT hByCidade.nm_municipio, hByCidade.sigla, hByCidade.vitimas, tar.total_aprov_fund , tar.total_aprov_em 
FROM (
	SELECT h.nm_municipio, h.sigla, sum(h.vitimas) as vitimas
	from homicidios h 
	group by h.nm_municipio
) hByCidade
LEFT JOIN estados e ON hByCidade.sigla = e.sigla
LEFT JOIN taxas_aprov_reprov_aband tar ON hByCidade.nm_municipio = tar.nm_municipio AND hByCidade.sigla = tar.sigla
WHERE tar.tipo_local = 'Total' and tar.tipo_escola = 'Total'
"""

df = pd.read_sql(query, conn)
df

plt.figure(figsize=(10, 6))

plt.scatter(df['total_aprov_fund'], df['vitimas'], color='blue', label='Fundamental')

plt.scatter(df['total_aprov_em'], df['vitimas'], color='green', label='Em')

plt.xlabel('aprovados')
plt.ylabel('homicidios')
plt.legend()

plt.show()


# %% query reprovados
query = """
SELECT hByCidade.nm_municipio, hByCidade.sigla, hByCidade.vitimas, tar.total_reprov_fund , tar.total_reprov_em 
FROM (
	SELECT h.nm_municipio, h.sigla, sum(h.vitimas) as vitimas
	from homicidios h 
	group by h.nm_municipio
) hByCidade
LEFT JOIN estados e ON hByCidade.sigla = e.sigla
LEFT JOIN taxas_aprov_reprov_aband tar ON hByCidade.nm_municipio = tar.nm_municipio AND hByCidade.sigla = tar.sigla
WHERE tar.tipo_local = 'Total' and tar.tipo_escola = 'Total'
"""

df = pd.read_sql(query, conn)
df

plt.figure(figsize=(10, 6))

plt.scatter(df['total_reprov_fund'], df['vitimas'], color='blue', label='Fundamental')

plt.scatter(df['total_reprov_em'], df['vitimas'], color='green', label='Em')

plt.xlabel('aprovados')
plt.ylabel('homicidios')
plt.legend()

plt.show()


# %% query abandonamento
query = """
SELECT hByCidade.nm_municipio, hByCidade.sigla, hByCidade.vitimas, tar.total_aband_fund , tar.total_aband_em 
FROM (
	SELECT h.nm_municipio, h.sigla, sum(h.vitimas) as vitimas
	from homicidios h 
	group by h.nm_municipio
) hByCidade
LEFT JOIN estados e ON hByCidade.sigla = e.sigla
LEFT JOIN taxas_aprov_reprov_aband tar ON hByCidade.nm_municipio = tar.nm_municipio AND hByCidade.sigla = tar.sigla
WHERE tar.tipo_local = 'Total' and tar.tipo_escola = 'Total'
"""

df = pd.read_sql(query, conn)
df

plt.figure(figsize=(10, 6))

plt.scatter(df['total_aband_fund'], df['vitimas'], color='blue', label='Fundamental')

plt.scatter(df['total_aband_em'], df['vitimas'], color='green', label='Em')

plt.xlabel('aprovados')
plt.ylabel('homicidios')
plt.legend()

plt.show()


# %%
