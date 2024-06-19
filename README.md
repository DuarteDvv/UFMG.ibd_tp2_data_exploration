# ufmg_tp2_data_exploration
  Bancos de Dados ou algo assim: 

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
  + Período de Referência dos dados: Ano de 2021
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
  
  ### > Estimativas de População - Municípios
  + Fonte: [Instituto Brasileiro de Geografia e Estatística - IBGE](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html)
  + Data de Obtenção: 14/06/2024
  + Período de Referência dos dados: Ano de 2021
  + Órgão produtor: IBGE
  + Limitações registradas: Uma quantidade significativa dos dados na coluna de população do dataset possui índices (exemplo: ' ¹ ') juntamente ao dado. Além disso, há a presença de um cabeçalho acima dos dados. Ambas essas características dificultam a formatação dos dados para uso com um SGBD.
  + Cobertura: Todos os municípios do Brasil
  + A metodologia adotada para estimar os contingentes populacionais dos municípios brasileiros baseia-se na relação da tendência de crescimento populacional do município, observada entre dois censos demográficos consecutivos, com a tendência de crescimento de uma área geográfica maior, as Unidades da Federação.
    + O método adotado tem como princípio fundamental a subdivisão de uma área maior, em n áreas menores, de tal forma que seja assegurada ao final das estimativas das áreas menores a reprodução da estimativa, previamente conhecida, da área maior através da soma das estimativas das áreas menores.
  #### Características dos dados:
  + As estimativas municipais incorporam, ano a ano, remanejamento da população resultado de alterações de limite territorial que ocorrem entre os municípios.
    + Dessa forma, a comparação histórica das estimativas anuais deve ser feita com cautela.
  



  
=======
O objetivo desse projeto é explorar dados publicos, registrando os problemas encontrados nos dados e a correlação entre violência e educação no país.
