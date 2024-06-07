# ufmg_tp2_data_exploration
<<<<<<< luis
  Bancos de Dados ou algo assim: vitor consiga unidade de medida, viez, origem e processo de obtenção descrição !!!!!!!!!!!

  Dicionário do banco de dados: https://docs.google.com/document/d/1jcfJAEqQk0MAtnWVjK--dplWNc-QfsWAp99TclBvFQ0/edit
  
  ![image](https://github.com/DuarteDvv/UFMG.ibd_tp2_data_exploration/assets/140446172/04e7fce0-7487-4fed-a535-e95590b57933)

# Metadados do projeto:

**TO DO:** adicionar em cada um dos seguintes tópicos as tabelas a que eles se referem.

  ### > Média de alunos por turma
  + Fonte: [Instituto Nascional de Estudos e Pesquisas Eduacionais Anísio Teixeira (Inep)](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/media-de-alunos-por-turma)
  + Data de Obtenção: 04/06/2024
  + Período de Referência dos dados: Ano de 2021
  + Órgão produtor: Inep
  + Limitações registradas: O arquivo do banco de dados foi disponibilizado em formato de excel, otimizado para leitura por um humano, e não por um computador: existem cabeçalhos misturados com os dados, os nulos não são vazios (são preenchidos como "--") e ocupam espaço, e existem muitas colunas redundantes (que são úteis para a leitura por um humano mas contém valores que podem ser deduzidos pelas outras colunas).
  + Cobertura: Municípios do Brasil 
  
  ### > Taxas de Distorção Idade-série
  + Fonte: [Instituto Nascional de Estudos e Pesquisas Eduacionais Anísio Teixeira (Inep)](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-distorcao-idade-serie)
  + Data de Obtenção: 04/06/2024
  + Período de Referência dos dados: Ano de 2021
  + Órgão produtor: Inep
  + Limitações registradas: O arquivo do banco de dados foi disponibilizado em formato de excel, otimizado para leitura por um humano, e não por um computador: existem cabeçalhos misturados com os dados, os nulos não são vazios (são preenchidos como "--") e ocupam espaço, e existem muitas colunas redundantes (que são úteis para a leitura por um humano mas contém valores que podem ser deduzidos pelas outras colunas).
  + Cobertura: Municípios do Brasil 
 
  ### > Taxas de Rendimento Escolar
  + Fonte: [Instituto Nascional de Estudos e Pesquisas Eduacionais Anísio Teixeira (Inep)](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar)
  + Data de Obtenção: 04/06/2024
  + Período de Referência dos dados: Ano de 2021
  + Órgão produtor: Inep
  + Limitações registradas: O arquivo do banco de dados foi disponibilizado em formato de excel, otimizado para leitura por um humano, e não por um computador: existem cabeçalhos misturados com os dados, os nulos não são vazios (são preenchidos como "--") e ocupam espaço, e existem muitas colunas redundantes (que são úteis para a leitura por um humano mas contém valores que podem ser deduzidos pelas outras colunas).
  + Cobertura: Municípios do Brasil
    
  ### > Taxas de Homicídios | Taxas de Homicídios (jovens)
  + Fonte: [MS/SVS/CGIAE - Sistema de Informações sobre Mortalidade - SIM](https://www.ipea.gov.br/atlasviolencia/filtros-series/1/homicidios) (Ipea - Atlas da Violência v.2.7)
  + Data de Obtenção: 04/06/2024
  + Período de Referência dos dados: Anos de 1989 até 2021 (usamos apenas os dados de 2021)
  + Órgão produtor: Ipea
  + Limitações registradas: Esse dataset possui alguns municípios a menos em relação ao total (faltam cerca de 60 municípios). Também não apresenta nenhum identificador do município além do nome. Isso torna impossível de tratar municípios de nomes idênticos caso pertençam a estados diferentes (além de exigir a tarefa trabalhosa de relacionar cada município de volta com seu respectivo estado)
  + Cobertura: Municípios do Brasil
  #### Características dos dados:
  + Considera os óbitos da faixa etária de 15 a 29 anos sem distinção de gênero.
  + Colunas:
    + **sigla**, a sigla da unidade federativa (string de 2 caracteres)
    + **mortes**, número inteiro representando a quantidade de homicídios.
  ### > Dados Nacionais de Segurança Pública - Municípios
  + Fonte: [Ministério da Justiça e Segurança Pública (MJSP)](https://dados.gov.br/dados/conjuntos-dados/sistema-nacional-de-estatisticas-de-seguranca-publica)
  + Data de Obtenção: 04/06/2024
  + Período de Referência dos dados: Anos de 2021
  + Órgão produtor: MJSP
  + Limitações registradas: Esse dataset possui pouquíssimos municípios em relação ao total (faltam quase todos os municípios). É difícil dizer se isso se dá por subnotificação de homicídios, se o método de coleta dos dados ignorou boa parte dos homicídios (banco ruim), ou se realmente não houveram homicídios dolosos em grande parte dos municípios.
  + Cobertura: Alguns municípios do Brasil
   + A coleta dos dados foi mensal, sendo apurados os dados dos 3 meses anteriores em relação à data de cada coleta
   + As informações que subsidiam a produção das estatísticas oficiais são fornecidas pelos setores estaduais de estatística e unidades policiais através da Coordenação Geral de Estatística- CGEst, seguindo um fluxo que consiste nas seguintes etapas: Coleta de dados, validação e atualização.
     + Para a coleta de dados, a CGEst utiliza os dados e informações de 02 sistemas: SINESPJC e Sinesp Integração.
     + Mensalmente, os dados são retirados dos sistemas e são disponibilizados em formulário eletrônico para conferência e validação pelos setores de estatística das Unidades da Federação. Com o processo de validação finalizado, as tabelas são encaminhadas para atualização da base de dados e do painel público de dados nacionais de segurança pública.
  #### Características dos dados:
   + Os dados são uma relação temporal entre os municípios do brasil e o número de vítimas registradas num boletim de ocorrência caracterizada como homicídio doloso.
   + Os dados foram validados pelos Gestores estaduais de estatística
   + Variações entre os Totais por UF e Municípios podem ocorrer devido aos processos permanentes de coleta, tratamento e análise dos dados pelos gestores estaduais.
   + Os dados registrados em data anterior à publicação da Portaria nº 229,de 10 de dezembro de 2018, não seguem a padronização contida no citado documento.
   + Os dados registrados no 1º trimestre de 2019 no Amapá correspondem a um grau de cobertura 33% maior que os apresentados no 1º bimestre de 2018, devido ao avanço do processo de implantação no estado da solução Sinesp PPE;



  
=======
O objetivo desse projeto é explorar dados publicos, registrando os problemas encontrados nos dados e a correlação entre violência e educação no país.
