# 3 DESENVOLVIMENTO DE SOLUÇÕES DE SI

## 3.1 Conexão com o plano de IC e definição do escopo

A solução de Business Intelligence desenvolvida no Power BI foi concebida em estreita conexão com o Plano de Inteligência Competitiva detalhado no Capítulo 2 deste trabalho. O escopo da solução foi definido para responder diretamente às necessidades informacionais da Escola de Música, visando transformar dados brutos em insights acionáveis para a tomada de decisão estratégica, especialmente no que tange à retenção de alunos.

### 3.1.1 Seleção de Key Intelligence Questions para os dashboards

Os dashboards foram projetados para responder a um conjunto específico de KIQs, identificadas no item 2.1.4 deste projeto. As principais KIQs abordadas pelas visualizações incluem:


- Quais fatores influenciam a evasão ou interrupção dos alunos na Escola de Música?
- Existe relação entre professor e evasão?
- Existe relação entre o tipo de aula (instrumentais específicas ou de canto) e evasão?
- Existe um período (mês) do ano com maior evasão?
- Há uma faixa de idade dos alunos em que há maior evasão?

Além das respostas às KIQs, os dados possibilitaram incluir gráficos que trouxeram análises extras, como evasão por bairro, evasões comparadas à quantidade de matrículas por professor, evasões por professor e curso, total de matrículas por professor e faixa etária, comparativos de evasão e total de matrículas por faixa etária e por bairro, além do total de matrículas por ano, por professor e por curso.

As Figuras 6 a 20 foram desenvolvidas especificamente para fornecer respostas visuais e analíticas a todas estas questões. Por exemplo, as Figuras 6 e 7 respondem diretamente à KIQ sobre o período do ano com maior evasão, enquanto as Figuras de 8 a 20 exploram a relação entre professor, curso, faixa etária, total de matrículas, localidade e as evasões, abordando as demais KIQs mencionadas e outras análises extras.


### 3.1.2 Definição das fontes de dados

Conforme estabelecido no planejamento de coleta de dados (item 2.3.1), a principal fonte de dados para esta solução de BI é interna. Os relatórios foram extraídos do sistema de gestão Emusys, utilizados pela Escola de Música. Estes relatórios, exportados em formato Excel, contêm informações sobre alunos, matrículas, cursos, professores, e o histórico de evasões. Para o escopo atual do projeto, não foram utilizadas fontes de dados externas, embora estas possam ser consideradas em evoluções futuras da solução.

### 3.1.3 Relação entre métricas, indicadores e objetivos de negócio

O desenvolvimento da solução de BI está intrinsecamente ligado aos objetivos de negócio e decisões críticas da Escola de Música, como a necessidade de manter os alunos matriculados (especialmente em períodos de férias), alcançar a meta de 200 alunos em 2025 e aumentar o faturamento. O Key Intelligence Topic  central deste projeto é, portanto, o estudo da evasão de alunos e a promoção da retenção.
Os dashboards desenvolvidos apresentam métricas e indicadores chave para monitorar e analisar este KIT, tais como:

- Quantidade de Evasões: Analisada mensalmente por todo o período e em 2024 (Figuras 6 e 7), por curso (Figuras 8 e 9), por professor (Figuras 10, 11, 12 e 18), por curso e professor (Figura 13), por bairro (Figura 14), e por faixa etária (Figura 15, 16) e por faixa etária e professor (Figura 19);
- Total de Matrículas: Contextualizado por professor (Figuras 9, 15), por faixa etária (Figura 16), por professor e faixa etária (Figura 20), permitindo uma análise proporcional da evasão;
Taxa de Evasão: Explicitamente calculada por professor e por matrículas e para a escola como um todo (Figura 18), sendo este um indicador crítico;
- Composição das Evasões e Matrículas: Detalhada por curso para cada professor (Figura 10), por bairro (Figura 17) e por faixa etária para cada professor (Figura 19).

A análise contínua desses indicadores, facilitada pelos dashboards, permite aos gestores identificarem os principais pontos de perda de alunos, compreender os fatores correlacionados (como mês, curso, professor, bairro, faixa etária) e, consequentemente, direcionar esforços e recursos para implementar estratégias de retenção mais eficazes. A redução da evasão impacta diretamente a capacidade da escola de atingir suas metas de crescimento de alunos e faturamento.


## 3.2 Organização e modelagem de dados

A etapa de organização e modelagem dos dados é fundamental para garantir a qualidade e a confiabilidade das análises geradas pela solução de Business Intelligence. Este processo envolveu a estruturação dos dados extraídos, o mapeamento das variáveis relevantes e a validação da consistência para uso analítico.

### 3.2.1 Organização dos dados 

Conforme detalhado no Plano de Coleta (item 2.3.2), os dados primários foram extraídos do sistema Emusys por meio da exportação de relatórios no formato Excel. Estas planilhas continham informações sobre alunos, matrículas, cursos, professores e o histórico de evasões. Antes da importação para o Power BI, foi realizado um tratamento inicial nesses dados brutos, pois os relatórios de Excel continham linhas com informações que deveriam ocupar várias linhas. Para isso, foi necessário tratamento das tabelas em formato .CSV com Python, para que as linhas extras fossem incluídas com os devidos dados. Após esse ajuste, já no PowerBI, a transformação no Power Query incluiu a padronização de formatos, a correção de possíveis inconsistências e a remoção de dados vazios ou irrelevantes, visando garantir a integridade e a qualidade da base de dados que alimentaria os dashboards. 


### 3.2.2 Mapeamento de variáveis, filtros e categorias

Para a construção das visualizações e análises, foram mapeadas as seguintes variáveis principais, presentes nos relatórios extraídos e utilizadas nos gráficos (Figuras 6 a 17):


- Dimensões Temporais: Mês e Ano (utilizados para filtros e análise de tendências, como na Figura 6).
- Dimensões Acadêmicas e Operacionais: Curso, Professor, Bairro de residência do aluno e Faixa Etária.
- Métricas Principais: Quantidade de Evasões, Total de Matrículas e Taxa de Evasão (calculada).

As categorias para cada variável correspondem aos valores distintos encontrados nos dados, como os diferentes nomes de cursos, professores, bairros e as faixas etárias definidas (Infantil, Adolescente, Jovem Adulto, Adulto, Melhor Idade). Os dashboards foram projetados para incluir filtros interativos, principalmente por "Ano" e "Curso" (observados nas imagens dos gráficos), permitindo aos gestores segmentar e explorar os dados de forma dinâmica.

### 3.2.3 Validação da consistência dos dados 

A validação da consistência dos dados foi uma preocupação central para assegurar a precisão das análises. O processo de tratamento inicial dos dados (item 2.4.3) já contemplava etapas de limpeza e padronização. Adicionalmente, o plano de coleta de dados (item 2.3.4) prevê a validação dos dados após cada exportação periódica (mensal) para garantir a manutenção da consistência ao longo do tempo. 

## 3.3 Planejamento dos dashboards

O planejamento dos dashboards foi uma etapa estratégica no desenvolvimento da solução de Business Intelligence, visando traduzir os Key Performance Indicators e as Key Intelligence Questions em visualizações claras, objetivas e acionáveis para os gestores da Escola de Música.

### 3.3.1 Planejamento dos gráficos a partir dos KPIs desejados

Os indicadores de desempenho chave (KPIs) para este projeto estão centrados na compreensão e mensuração da evasão de alunos. Estes incluem, mas não se limitam a: número total de evasões, taxa de evasão geral, taxa de evasão por professor, distribuição de evasões por mês, por curso, por faixa etária e por bairro. Os 15 gráficos desenvolvidos (Figuras 6 a 20), detalhados no subitem 3.5, foram cuidadosamente planejados para visualizar um ou mais desses KPIs e para responder diretamente às KIQs formuladas no Plano de Inteligência Competitiva (item 2.1.4). Por exemplo:

Para a KIQ "Existe um período(mês) do ano com maior evasão?", foi planejado o gráfico de Quantidade de evasões mensais e Quantidade de evasões mensais no ano de 2024 (Figuras 6 e 7 respectivamente).

Para a KIQ "Existe relação entre professor e evasão?", foram concebidos múltiplos gráficos, incluindo Quantidade de evasões por professor (Figura 10), Quantidade de evasões por professor no ano de 2024 (Figura 11), Comparativo entre evasões e total de matrículas por professor (Figura 12), Taxa de evasão e total de matrículas por professor (Figura 18), Distribuição das evasões por curso para cada professor (Figura 13) e Distribuição das evasões por faixa etária para cada professor (Figura 19).

A KIQ "Existe relação entre o tipo de aula (instrumentais específicas ou de canto) e evasão?" é abordada pelo gráfico de Quantidade de evasões por curso (Figura 8) e Quantidade de evasões por curso no ano de 2024 (Figura 9).

A KIQ "Há uma faixa de idade dos alunos em que há maior evasão?" é respondida pelo gráfico de Distribuição percentual e absoluta das evasões por faixa etária (Figura 15), pelo Comparativo entre evasões e total de matrículas por faixa etária (Figura 16) e complementada pelas Figuras 19 e 20. 

A seleção dos tipos de gráficos (barras, pizza, empilhados, agrupados) também foi pensada para otimizar a clareza e a comparabilidade dos dados.


### 3.3.2 Identificação de filtros e visualizações Interativas

A escolha do Power BI como ferramenta de desenvolvimento (item 2.4.1) se deu, em parte, por sua robusta capacidade de criar visualizações interativas. Os dashboards foram planejados para permitir que os gestores não apenas visualizem os dados de forma estática, mas também interajam com eles. Foram identificados e implementados filtros chave, como Ano e Curso (conforme observado nas imagens dos gráficos analisados), que permitem aos usuários segmentar os dados e aprofundar a análise em contextos específicos. A interatividade natural do Power BI, onde a seleção de um elemento em um gráfico pode filtrar outros visuais no mesmo painel, foi considerada como um requisito para facilitar a exploração e a descoberta de insights adicionais pelos próprios usuários.


### 3.3.3 Validação da estrutura com base nos objetivos de IC

A estrutura geral dos dashboards e a organização dos gráficos foram planejadas para atender aos objetivos de Inteligência Competitiva definidos: fornecer informações claras e relevantes sobre o fenômeno da evasão para subsidiar a tomada de decisão estratégica. A intenção foi criar painéis que oferecessem tanto uma visão macro dos indicadores de evasão (como a taxa geral e os principais fatores correlacionados) quanto a possibilidade de detalhamento para investigar causas específicas. A validação dessa estrutura buscou garantir que os dashboards fossem intuitivos e que as informações fossem apresentadas de forma lógica, facilitando a compreensão dos gestores sobre os fatores que impactam a retenção de alunos e, assim, contribuindo para a formulação de estratégias para alcançar as metas da escola, como a redução da evasão e o aumento do número de alunos matriculados. 

## 3.4 Início da construção e automação

Com o planejamento dos dashboards concluído, iniciou-se a fase de construção da solução de Business Intelligence no Power BI, envolvendo a conexão com as fontes de dados, a criação das visualizações e a estruturação da navegação, seguida pela validação inicial.

### 3.4.1 Montagem do dashboard e conexão com os dados

A ferramenta selecionada para a construção dos dashboards foi o Microsoft Power BI, devido à sua capacidade de criar visualizações interativas e dinâmicas. A conexão com os dados foi estabelecida a partir das planilhas em formato Excel extraídas do sistema Emusys. Essas planilhas, contendo os dados brutos sobre matrículas, evasões, cursos, professores, alunos, bairros e faixas etárias, foram importadas para o Power BI. Dentro do Power BI, os dados passaram por etapas de transformação e modelagem para adequá-los às necessidades de análise. Isso incluiu a limpeza de dados, a criação de colunas calculadas (como a "Taxa de Evasão", “Quantidade de Matrículas” e “Quantidade de Evasões”) e o estabelecimento de relacionamentos entre as diferentes tabelas de dados (fato e dimensões), garantindo que as informações pudessem ser cruzadas e analisadas de forma integrada nas diversas visualizações.


### 3.4.2 Criação das visualizações principais e estrutura de navegação

As visualizações principais da solução são os 15 gráficos (Figuras 6 a 20) que serão apresentados no subitem 3.5. Estes gráficos foram desenvolvidos para abordar diretamente as KIQs e os KPIs definidos no planejamento. A estrutura de navegação foi pensada para agrupar essas visualizações em painéis temáticos (dashboards) que oferecessem uma experiência de usuário intuitiva e lógica.

### 3.4.3 Validação dos dados e testes iniciais de visualização

Após a criação das visualizações iniciais, foram realizados testes para validar a precisão dos dados exibidos e a correção dos cálculos se necessário. Esta etapa é crucial para garantir a confiabilidade da solução de BI. Conforme o plano de coleta, foi feita uma validação dos dados após cada exportação, e a periodicidade de coleta recomendada é mensal, o que implica a necessidade de um processo de atualização e validação contínua dos dashboards. Os testes iniciais também envolveram a verificação da interatividade dos filtros e da clareza das visualizações, assegurando que os dashboards estivessem prontos para a fase de análise e interpretação dos resultados pelos gestores.


## 3.5 Análise das informações apresentadas nos dashboards

Nesta seção, faremos a análise dos dados utilizando recursos visuais por meio dos dashboards desenvolvidos no Power BI. As figuras que serão exibidas representam os principais indicadores e tendências extraídos dos dados, facilitando a compreensão dos resultados e apoiando a tomada de decisões de forma mais estratégica e embasada. O arquivo .pbix dessa análise, contém os dashboards interativos; aqui, por se tratar de um documento, só foi possível fazer as análises com as figuras, sem interações dinâmicas.
</br>
<center>Figura 6 – Quantidade de evasões mensais</center>

![Quantidade de evasões mensais ](images/graficos/figura%206.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 6 apresenta um gráfico de barras horizontais que ilustra a quantidade de evasões de alunos na Escola de Música, distribuídas ao longo do período de março de 2023 a maio de 2025. O eixo vertical lista os meses, enquanto o eixo horizontal quantifica o número de evasões.
Observa-se que o mês de Dezembro destaca-se significativamente com o maior número de evasões, atingindo 29 ocorrências. Este dado pode estar correlacionado com o período de férias escolares e as festividades de final de ano, um dos focos de investigação do presente estudo sobre retenção de alunos.
Em seguida, os meses de Abril e Janeiro também apresentam um volume considerável de evasões, ambos com 24 evasões. A alta evasão em janeiro pode ser uma extensão do efeito de férias e das decisões de início de ano, enquanto o motivo para o volume em abril necessitaria de investigação adicional para melhor compreensão contextual.
Os demais meses apresentam um volume de evasões que varia entre 8 e 19. Os meses de Julho e Setembro têm cada um 19 evasões. Os meses de Março, Junho, Agosto e Maio registraram entre 16 e 18 evasões. Novembro apresenta 15 evasões, e Outubro e Fevereiro figuram com os menores índices, com 11 e 8 evasões, respectivamente.
A distribuição das evasões ao longo do período analisado (março de 2023 a maio de 2025) não demonstra um padrão linear de crescimento ou decréscimo contínuo, mas sim picos e vales em meses específicos. Esta visualização responde diretamente à Key Intelligence Question que busca identificar "Existe um período(mês) do ano com maior evasão?", apontando claramente para Dezembro, seguido por Abril e Janeiro, como os períodos mais críticos. A análise mais aprofundada, cruzando estes dados com outros fatores como cursos, professores ou perfil do aluno, poderá fornecer insights valiosos para as estratégias de retenção da Escola de Música.

</br>

<center>Figura 7 – Quantidade de evasões mensais no ano de 2024</center>

![Quantidade de evasões mensais ](images/graficos/figura%207.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 7 apresenta um gráfico de barras horizontais que detalha a quantidade de evasões de alunos na Escola de Música, com os dados referentes especificamente ao ano de 2024, com o uso do filtro de ano do mesmo gráfico da figura 6. Esta visualização permite uma análise focada no padrão de evasão ocorrido neste período. No gráfico, o eixo vertical lista os meses, enquanto o eixo horizontal quantifica o número de ocorrências.  A leitura do gráfico é feita da seguinte forma: o segmento azul escuro da barra representa o número de evasões mensais ocorridas especificamente no ano de 2024; o segmento azul claro representa o número de evasões ocorridas nos outros anos do período (2023 e 2025); e a barra inteira, que é a soma de ambos, representa o total de evasões naquele curso em todo o período analisado (2023 a 2025).
Conforme os dados de 2024, o mês de Dezembro destaca-se como o período com o maior número de evasões, atingindo 18 ocorrências. Este dado reafirma o final do ano como um período sazonal crítico para a retenção, possivelmente impactado pelas férias e festividades.
Após o pico de Dezembro, observa-se um segundo nível de evasões. O mês de Janeiro apresenta 11 evasões, seguido por Julho com 10 e Setembro com 9. Estes números sugerem uma sensibilidade a períodos de transição, como o início do ano e o recesso de meio de ano.
Os demais meses de 2024 demonstram um volume de evasão mais moderado. Abril, Junho e Agosto registraram um patamar similar, com 7 evasões cada. Os meses de Maio e Outubro tiveram volumes ligeiramente menores, com 5 evasões cada. Por fim, Março, Novembro e Fevereiro representam os meses de menor evasão em 2024, com 4 ocorrências cada um.
A análise da Figura 7 responde à Key Intelligence Question para o ano de 2024, identificando claramente Dezembro como o mês de maior preocupação, seguido por um período de atenção em Janeiro e no início do segundo semestre (Julho e Setembro). O mapeamento preciso do padrão de evasões ao longo de 2024 é um recurso valioso para a gestão da Escola de Música, permitindo o planejamento de ações de retenção mais direcionadas e eficazes para os desafios específicos de cada período do ano.
</br>
</br>
<center>Figura 8 – Quantidade de evasões por curso</center>

![Quantidade de evasões mensais ](images/graficos/figura%208.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 8 exibe um gráfico de barras horizontais detalhando o número de evasões por tipo de curso oferecido pela Escola de Música, referente ao período de março 2023 a maio 2025. O eixo vertical lista os diversos cursos, e o eixo horizontal quantifica o número absoluto de evasões para cada um.
Observa-se que o curso de violão individual apresenta o maior número de evasões, com 41 ocorrências no período analisado. Logo em seguida, canto individual também demonstra um volume expressivo de desistências, com 38 evasões. Estes dois cursos individuais lideram com folga em termos de números absolutos de evasão.
Outros cursos com evasões notáveis incluem piano, com 20 evasões, seguido por bateria, com 18, e guitarra, com 14 evasões. Cursos como teclado (12 evasões) e teoria (9 evasões) também figuram com um número relevante de desistências.
O gráfico também revela uma longa lista de cursos com um número menor de evasões, muitos deles abaixo de 5 ocorrências, como Cavaquinho, Musicalização individual, Ukulele, Violoncelo, Acordeão, Cajon, Gaita de boca e Trompa, que apresentam as menores quantidades.
</br>
</br>
<center>Figura 9: Quantidade de evasões por curso no ano de 2024</center>

![Quantidade de evasões mensais ](images/graficos/figura%209.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 9 apresenta um gráfico de barras que compara as evasões por curso, oferecendo uma visão sobre o desempenho do ano de 2024 em relação ao período completo de março de 2023 a maio de 2025. Foi usado o filtro de ano do gráfico anterior (Figura 8). A leitura do gráfico é feita da seguinte forma: o segmento azul escuro da barra representa o número de evasões ocorridas especificamente no ano de 2024; o segmento azul claro representa o número de evasões ocorridas nos outros anos do período (2023 e 2025); e a barra inteira, que é a soma de ambos, representa o total de evasões naquele curso em todo o período analisado (2023 a 2025). Esta análise permite, portanto, identificar quais cursos tiveram uma concentração de evasões em 2024.
A análise revela que alguns cursos tiveram uma concentração preocupante de evasões no ano de 2024. O curso de Canto Individual destaca-se negativamente, com 22 evasões ocorridas neste ano, posicionando-o como um dos principais focos de problema. Outros cursos com problemas agudos são Guitarra (8 evasões de 14 matrículas) e Teoria (6 evasões de 9 matrículas), nos quais a maioria das evasões está concentrada em 2024. Já o curso de Violão Individual, apesar de ser o que possui o maior número de evasões no total (41), teve uma situação em 2024 que, embora séria, com 17 evasões, foi proporcionalmente menos concentrada neste ano em comparação com o curso de Canto Individual.
Em uma nota positiva, a análise aponta para sucessos notáveis na retenção de alunos em outros cursos durante o ano de 2024. Piano e Bateria são os exemplos de maior sucesso. Apesar de acumularem um número alto de evasões no período total (20 e 18, respectivamente), ambos tiveram uma queda drástica em 2024, registrando pouquíssimas evasões (4 no Piano e apenas 5 na Bateria). Isso sugere que as ações tomadas ou as condições destes cursos foram altamente eficazes na retenção de alunos.
</br>
</br>
<center>Figura 10 – Quantidade de evasões por professor</center>

![Quantidade de evasões mensais ](images/graficos/figura%2010.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 10 apresenta um gráfico de barras horizontais que demonstra a distribuição da quantidade de evasões de alunos por professor na Escola de Música no período de março de 2023 a maio de 2025. O eixo vertical lista os nomes dos professores (de forma abreviada), e o eixo horizontal quantifica o número de evasões associadas a cada um.
O professor Silveira, M. é o que apresenta o maior número de evasões, com 32 ocorrências. Em seguida, destacam-se Rezende, L., com 27, Miranda, E., com 26, Ferraz, C., 23, e Abreu, V., 21 evasões. Estes cinco professores concentram os volumes mais significativos de desistências.
Outros professores como Soares, A. com 18 evasões, Alves, H., 13, Silva, E. com 12, Neto, E., 10 e Moraes, E., com 9 também apresentam um número considerável de evasões.
Na extremidade inferior do gráfico, observa-se um grupo de professores com um número significativamente menor de evasões. Matos, R. e Coronel, K. registraram 6 e 5 evasões, respectivamente. Os professores Fernandes, C., Loureiva, V., Sant'ana, G., Silva, A. e Rojas, V. apresentam os menores números, todos com menos de 5 evasões (entre 2 e 3).
Este gráfico é fundamental para investigar a KIQ: "Existe relação entre professor e evasão?". Os dados indicam que alguns professores estão associados a um número maior de desistências. Contudo, é crucial considerar que professores com um maior número de alunos ou turmas podem, naturalmente, apresentar um volume absoluto de evasões mais elevado.
</br>
</br>
<center>Figura 11 - Quantidade de evasões por professor no ano de 2024</center>

![Quantidade de evasões mensais ](images/graficos/figura%2011.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 11 apresenta um gráfico de barras que detalha as evasões de alunos por professor no ano de 2024. Foi usado o filtro de ano do gráfico anterior (Figura 10). A leitura do gráfico é feita da seguinte forma: o segmento azul escuro da barra quantifica as evasões ocorridas sob a responsabilidade de cada professor especificamente no ano de 2024; o segmento azul claro representa o número de evasões de cada professor ocorridas nos outros anos do período (2023 e 2025); e a barra inteira, que é a soma de ambos, representa o total de evasões de cada professor em todo o período analisado (2023 a 2025). Esta análise permite identificar os professores com maior impacto na evasão de alunos, destacando tanto os desafios quanto os casos de sucesso no ano de 2024.
Um pequeno grupo de professores concentrou o maior volume de evasões no ano de 2024, representando os principais pontos de atenção. Silveira, M., Rezende, L. e Miranda, E. lideram o ranking, sendo responsáveis pelo maior número absoluto de evasões em 2024, com 14, 13 e 12 ocorrências, respectivamente. Eles representam um desafio tanto pelo volume em 2024 quanto pelo alto histórico de evasões em todo o período. Soares, A., com 11 evasões em 2024, também figura entre os mais críticos, sendo notável que as evasões deste ano representam mais da metade do total histórico atribuído a ele, sugerindo um problema que se intensificou em 2024, visto que em 2025 ele ainda não tem evasões.
Em contraste, o gráfico revela casos de professores que, apesar de um histórico de evasões elevado, demonstraram uma melhora muito significativa na retenção de alunos em 2024. Ferraz, C. e Abreu, V. são os exemplos mais claros de sucesso. Ambos possuem um total acumulado de evasões elevado (23 e 21, respectivamente), mas registraram um número muito baixo de evasões em 2024 (6 e 5, respectivamente). Essa redução drástica indica que há mudanças em suas práticas que foram altamente eficazes para a retenção.
A análise também aponta para professores cujo problema de evasão parece ser recente ou específico de 2024. Moraes, E. e Silva, E. são exemplos disso, pois para ambos, a maior parte de suas evasões totais ocorreu neste ano, indicando um agravamento recente na retenção de seus alunos.
</br>
</br>
<center>Figura 12 – Comparativo entre evasões e total de matrículas por professor </center>

![Quantidade de evasões mensais ](images/graficos/figura%2012.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 12 apresenta um gráfico de barras horizontais agrupadas, que compara o número absoluto de evasões (representado pela barra azul mais clara) com o total de matrículas (representado pela barra azul mais escura) para cada professor da Escola de Música, em todo o período analisado (de 2023 a 2025).
Este visual é particularmente relevante, pois permite uma avaliação mais contextualizada da performance de cada professor em relação à retenção de alunos, possibilitando inferir visualmente a proporção ou taxa de evasão.
O professor Silveira, M., que apresentou o maior número absoluto de evasões na análise anterior, também figura aqui com o maior volume de matrículas, com 51, e um número de evasões de 32. Embora o volume de matrículas seja alto, a proporção de evasões também se mostra considerável.
De forma ainda mais acentuada, o professor Rezende, L. exibe um alto número de evasões, com 27, frente ao seu total de 34 matrículas, o que sugere uma taxa de evasão percentualmente elevada. Similarmente, Miranda, E. com 26 evasões para 38 matrículas e Abreu, V. com 21 evasões para 33 matrículas também demonstram proporções de evasão que merecem atenção.

Cabe destacar que os professores Neto, E., com 10 evasões para 10 matrículas, assim como Matos, R. com 6 evasões para 6 matrículas, Rojas, V. com 2 matrículas e 2 evasões, Coronel, K. com 5 evasões para 5 matrículas e Louveira, V. com 3 matrículas e 3 evasões apresentam assim uma taxa de evasão de 100% no período analisado. Apesar desses professores apresentarem taxas de evasão visualmente muito altas, isso se dá porque eles não são mais colaboradores da escola. Os professores Neto, E., Matos, R.e Rojas, V. finalizaram seus contratos no ano de 2023 e Coronel, K. e Louveira, V. finalizaram em 2024.
</br>
</br>
<center>Figura 13 – Distribuição das Evasões por Curso para Cada Professor </center>

![Quantidade de evasões mensais ](images/graficos/figura%2013.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 13 apresenta um gráfico de barras empilhadas que detalha a composição das evasões para cada professor da Escola de Música, segmentando o total de evasões de cada docente pelos diferentes cursos que leciona, em todo o período analisado (2023 a 2025). O eixo vertical lista os professores, e o eixo horizontal representa o número total de evasões. Cada segmento colorido dentro da barra de um professor corresponde à quantidade de evasões provenientes de um curso específico, conforme a legenda de cursos no topo do gráfico (nessa figura 13 só é possível ver parte desses cursos da extensa legenda; no Power BI há uma barra de rolagem para acesso a todos os cursos).
Este gráfico permite uma análise mais granular da origem das evasões. Para o professor Silveira, M., que possui o maior volume total de evasões (32), observa-se que estas são provenientes de uma variedade de cursos, com contribuições significativas de pelo menos três cursos distintos, sendo eles os de violão individual (rosa choque, 23 evasões), violão grupo (roxo, 4 evasões) e cavaquinho (verde escuro, 2 evasões), predominantes em sua barra.
No caso do professor Rezende, L., o segundo com maior número de evasões totais (27), uma parcela considerável das desistências parece concentrar-se em dois cursos principais, teclado (dourado/amarelo, 7 evasões) e teoria (verde-água, 9 evasões). Para Miranda, E., o terceiro com maior número de evasões totais (26), elas também se distribuem por múltiplos cursos, com destaque para os cursos canto individual (vermelho escuro, 14 evasões) e violino (roxo escuro, 6 evasões).
Para professores com um volume total de evasões menor, como Rojas, V. e Silva, A., o gráfico ilustra que suas poucas evasões estão concentradas em um ou dois cursos específicos. Por exemplo, as 2 evasões de Rojas, V. são somente do curso de musicalização (azul claro), enquanto as 3 evasões de Silva, A. provêm de dois cursos: canto individual (vermelho escuro, 2 evasões) e violoncelo (marrom, 1 evasão).
</br>
</br>
<center>Figura 14 – Quantidade de evasões por bairro</center>

![Quantidade de evasões mensais ](images/graficos/figura%2014.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 14 apresenta um gráfico de barras horizontais que ilustra a quantidade de evasões de alunos da Escola de Música, distribuídas por bairro de residência, em todo o período analisado (2023 a 2025). O eixo vertical lista os nomes dos bairros, e o eixo horizontal quantifica o número de evasões. 
O bairro Centro destaca-se com o maior número de evasões, registrando 27 ocorrências. Considerando que a Escola de Música está localizada no centro da cidade de Campo Grande - MS, este dado pode refletir uma maior concentração de alunos provenientes desta área ou, alternativamente, uma maior concorrência e oferta de atividades alternativas no próprio centro.
Um ponto de grande relevância na análise é o alto volume de evasões em bairros de elevado poder aquisitivo. Santa Fé (15 evasões), Carandá Bosque (14), Chácara Cachoeira (entre 4 e 7) e o condomínio de luxo Residencial Damha III (8) figuram com números expressivos. Nestas áreas, é provável que a desistência não esteja associada a dificuldades financeiras, mas sim a outros fatores, como a intensa concorrência com outras atividades extracurriculares (esportes, idiomas), a pressão por estudos focados em vestibulares ou uma percepção de valor do serviço que não atendeu às expectativas de um público mais exigente.
Em segundo lugar geral, o bairro Monte Castelo, uma área tradicional e de classe média, apresenta 23 casos de evasão. Este número é significativo e aponta para a importância deste perfil de cliente para a escola. Para este público, fatores como a percepção de custo-benefício, satisfação com a didática e o encaixe das aulas na rotina familiar podem ser decisivos. Outros bairros populosos e mais distantes do centro, como Tiradentes, Mata do Jacinto e Nova Lima (todos com 4 a 7 evasões), podem ter a logística de deslocamento como uma barreira adicional, tornando a continuidade do curso um desafio.
Por fim, o gráfico evidencia uma longa lista de bairros com um número reduzido de evasões (3 ou menos), como Jardim Veraneio, Panamá e Sobrinho. Esta cauda longa pode indicar duas possibilidades: ou a escola possui uma baixa penetração de marketing e poucos alunos oriundos dessas regiões, ou os alunos que vêm desses bairros são altamente engajados e apresentam excelente taxa de retenção. Compreender qual desses cenários é o verdadeiro pode abrir novas oportunidades de expansão ou revelar modelos de sucesso a serem estudados.
</br>
</br>
<center>Figura 15 – Distribuição percentual e absoluta das evasões por faixa etária</center>

![Quantidade de evasões mensais ](images/graficos/figura%2015.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 15 apresenta um gráfico de pizza que ilustra a distribuição das evasões na Escola de Música de acordo com a faixa etária dos alunos. Cada fatia do gráfico representa uma faixa etária específica, exibindo tanto o número absoluto de evasões quanto o seu percentual correspondente em relação ao total de evasões no período analisado (março de 2023 a maio de 2025).
A faixa etária com a maior proporção de evasões é a dos Adolescentes (13-17 anos), que corresponde a 27,31% do total, totalizando 59 evasões. Este dado sugere que este grupo etário representa um desafio particular para a retenção de alunos. Em seguida, a faixa de Adultos (41-59 anos) representa 23,15% das evasões (50 alunos), seguida de perto pela faixa de Adultos (26-40 anos), com 18,52% (40 alunos). Somadas, estas três faixas (Adolescentes e os dois grupos de Adultos) concentram a maior parte das desistências. 
A faixa de Jovens Adultos (18-25 anos) contribui com 15,28% das evasões (33 alunos). A faixa Infantil (1-12 anos) é responsável por 10,65% das evasões, o que corresponde a 23 alunos. Por fim, a faixa da Melhor idade (60+) apresenta o menor percentual de evasões, com 5,09% (11 alunos), devido a um volume menor de alunos nessa faixa etária, entretanto na análise do próximo gráfico (figura 16) veremos que a evasão da melhor idade é alta comparada ao número total de matrículas (baixa permanência).
Este gráfico responde diretamente à Key Intelligence Question formulada no item 2.1.4 do presente trabalho: "Há uma faixa de idade dos alunos em que há maior evasão (infantil 1 - 12 / adolescente 13 - 17 / adulto 18 - 59 / melhor idade 60+)?". A análise demonstra que, embora todas as faixas etárias apresentem evasões, os adolescentes e adultos (especialmente entre 26 e 59 anos) são os grupos que mais demandam atenção em estratégias de retenção. 

</br>
</br>
<center>Figura 16 – Comparativo entre evasões e total de matrículas por faixa etária</center>

![Quantidade de evasões mensais ](images/graficos/figura%2016.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 16 apresenta um gráfico de barras horizontais agrupadas, comparando o número absoluto de evasões (barras em azul claro) com o total de matrículas (barras em azul escuro) para cada faixa etária na Escola de Música. O eixo vertical lista as categorias de idade, enquanto o eixo horizontal quantifica o número de evasões e matrículas. Esta visualização permite uma compreensão mais aprofundada do fenômeno da evasão, contextualizando-o em relação ao volume de matrículas em cada faixa etária, possibilitando assim uma inferência da taxa de evasão proporcional.
Com base neste gráfico, a faixa etária infantil (1-12) exibe o maior número total de matrículas, com 98 matrículas. Para este grupo, há 50 evasões. Embora não seja o maior número absoluto de evasões, representa uma parcela significativa desta faixa etária.
O grupo Adolescente (13-17) possui o segundo maior número de matrículas (94) e o maior número absoluto de evasões, 59 (consistente com a Figura 15). Essa combinação indica um desafio considerável na retenção de alunos adolescentes.
Para a categoria Adulto (26-40), tem-se o total de 50 matrículas, com 40 evasões. Isso sugere uma taxa de evasão proporcionalmente muito alta para este grupo demográfico. Similarmente, Jovem Adulto (18-25) apresenta 48 matrículas e 33 evasões também indicando uma alta propensão à evasão em relação ao seu número de matrículas.
Por fim, a faixa Melhor idade (60+) apresenta o menor total de matrículas (14) e o menor número absoluto de evasões (11). Contudo, mesmo com números absolutos baixos, a proporção de evasões em relação às matrículas neste grupo parece notavelmente alta, o que mostra dificuldade na continuidade das matrículas dessa faixa etária.
</br>
</br>
<center>Figura 17 – Comparativo entre evasões e total de matrículas por bairro </center>

![Quantidade de evasões mensais ](images/graficos/figura%2017.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 17 exibe um gráfico de barras horizontais agrupadas, que realiza uma comparação entre o número absoluto de evasões (barras em azul claro) e o total de matrículas (barras em azul escuro) para cada bairro de origem dos alunos da Escola de Música. O eixo vertical lista os bairros, enquanto o eixo horizontal quantifica o volume de evasões e matrículas. Este tipo de visualização é fundamental para contextualizar o número de evasões em relação à representatividade de cada bairro no corpo discente.
O bairro Monte Castelo destaca-se com o maior número total de matrículas (44), e apresenta um número de evasões de 23. Embora o volume de evasões seja alto, ele se dá sobre uma base maior de alunos. Já o bairro Centro, que possui o segundo maior volume de matrículas (36), registra o maior número absoluto de evasões (27), indicando uma taxa de evasão proporcionalmente muito elevada.
Bairros como Santa Fé (com 15 evasões para 18 matrículas) e Carandá Bosque (com 14 evasões para 19) também chamam a atenção pelas altas taxas de evasão, onde o número de desistências se aproxima consideravelmente do total de alunos matriculados desses locais. Situação similar ocorre em Residencial Damha III (8 evasões para 11 matrículas) e Chácara Cachoeira (7 evasões para 9 matrículas).
Na outra ponta, bairros como Jardim dos Estados apresentam um número moderado de matrículas (10) com um número relativamente baixo de evasões (2), sugerindo uma melhor retenção de alunos dessa localidade. Muitos bairros listados na parte inferior do gráfico possuem um baixo volume tanto de matrículas quanto de evasões, como Jardim Paradiso e Monte Carlo. No entanto, mesmo em alguns bairros com poucas matrículas, a proporção de evasões pode ser significativa, como observado em Parque Residencial Damha IV (2 evasões para 3 matrículas).
A presente visualização permite correlacionar essas evasões com a base de alunos de cada bairro. Isso pode ajudar a identificar se a escola enfrenta desafios de retenção em bairros específicos devido a fatores como distância, concorrência local ou perfil socioeconômico dos alunos, informações que, embora não respondam diretamente a uma KIQ específica sobre bairros, contribuem para o entendimento geral dos fatores que influenciam a evasão e podem subsidiar decisões estratégicas, como campanhas de marketing direcionadas ou parcerias locais.
</br>
</br>
<center>Figura 18 – Taxa de evasão e total de matrículas por professor</center>

![Quantidade de evasões mensais ](images/graficos/figura%2018.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 18 apresenta um visual composto por um gráfico de barras horizontais à esquerda, que compara a taxa de evasões (azul claro) e o total de matrículas (azul escuro) por professor, e uma tabela à direita, que detalha os mesmos dados do gráfico de barras horizontais, trazendo a quantidade absoluta de matrículas e a taxa de evasão por professor de forma a visualizar melhor os números. Este conjunto de informações é vital para uma análise aprofundada da performance de retenção de cada professor.
Observa-se um grupo de professores com uma taxa de evasão de 100% (1.00), indicando que todos os alunos matriculados com eles evadiram no período. São eles: Coronel, K. (com 5 matrículas), Rojas, V. (2 matrículas), Louveira, V. (3 matrículas), Matos, R. (6 matrículas), Neto, E. (10 matrículas), já destacado em análises anteriores o motivo da evasão ser por esses professores não serem mais colaboradores da escola.
Outros professores apresentam taxas de evasão também muito elevadas, como Rezende, L., com uma taxa de 79% sobre um volume considerável de 34 matrículas (resultando em 27 evasões), e Fernandes, C., com 75% (3 evasões sobre 4 matrículas).
Taxas de evasão altas, entre 60% e 68%, são observadas para professores com volumes significativos de alunos: Abreu, V. (64% sobre 33 matrículas), Miranda, E. (68% sobre 38 matrículas), Silveira, M. (63% sobre 51 matrículas – o maior número de matrículas) e Soares, A. (62% sobre 29 matrículas). Sant'ana, G. também apresenta uma taxa de 60% sobre 5 matrículas.
Professores com taxas de evasão consideradas moderadas, entre 50% e 57%, incluem Alves, H. (50% sobre 26 matrículas), Ferraz, C. (51% sobre 45 matrículas), Moraes, E. (50% sobre 18 matrículas) e Silva, E. (57% sobre 21 matrículas).
Um ponto positivo é que o professor Sousa, D. apresenta uma taxa de evasão de 0% com 4 matrículas, indicando retenção total de seus alunos no período, assim como o professor Peruzzo, K., que mantém 1 matrícula em curso.
A tabela também consolida uma taxa de evasão geral de 64% (216 evasões) para a escola, considerando um total de 338 matrículas no período analisado. Este é um indicador alarmante e central para o estudo, reforçando a criticidade do tema de evasão para a Escola de Música.
Este visual responde de forma quantitativa e direta à KIQ "Existe relação entre professor e evasão?", detalhando não apenas o volume, mas a proporção de perdas por docente.
</br>
</br>
<center>Figura 19 – distribuição das evasões por faixa etária para cada professor</center>

![Quantidade de evasões mensais ](images/graficos/figura%2019.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>

</br>
A Figura 19 apresenta um gráfico de barras empilhadas que detalha a composição das evasões para cada professor da Escola de Música, segmentando o total de evasões de cada docente pela faixa etária dos alunos que desistiram. O eixo vertical lista os professores, e o eixo horizontal representa o número total de evasões. Cada segmento colorido dentro da barra de um professor corresponde à quantidade de evasões de alunos de uma determinada faixa etária, conforme a legenda no topo do gráfico.
Analisando os professores com maior volume de evasões, como Silveira, M. (32 evasões), observa-se que as desistências provêm de múltiplas faixas etárias, com destaque para faixa Adolescente (13-17 anos) (representada em azul claro no gráfico) com 6 evasões e Adulto (41-59 anos) (roxo escuro) com 8, mas também com contribuições de Adulto (26-40 anos) (azul escuro) com 8.
Para Rezende, L., as evasões (27) concentram-se significativamente na faixa Adulto (41-59 anos) (roxo escuro) com 7 evasões e Adolescentes (13-17 anos) (azul claro) com 7.
O professor Ferraz, C. tem um volume expressivo de evasões provenientes de Adolescentes com 12 evasões. Soares, A. apresenta evasões concentradas nas faixas de Adulto (26-40 anos) com 9 evasões.
</br>
</br>
<center>Figura 20 – Composição do total de matrículas por faixa etária para cada professor</center>

![Quantidade de evasões mensais ](images/graficos/figura%2020.png)
<center>Fonte: Elaborado pelos autores (2025), com base nos dados extraídos do sistema Emusys.</center>
</br>
A Figura 20 apresenta um gráfico de barras empilhadas que ilustra a composição do total de matrículas para cada professor da Escola de Música, segmentado pela faixa etária dos alunos. O eixo vertical lista os professores, e o eixo horizontal representa o "Total de Matrículas". Cada segmento colorido dentro da barra de um professor indica o volume de alunos matriculados de uma determinada faixa etária, conforme a legenda no topo do gráfico. 
Este gráfico revela o perfil de público predominante para cada docente. O professor Silveira, M., com o maior número total de matrículas (51), atende a um público diverso, com uma concentração significativa de alunos nas faixas Adolescente (13-17 anos), (representada por azul claro no gráfico, 10 matrículas) e Adulto (41-59 anos) (laranja, 11 matrículas), mas também com boa representatividade de Adulto (26-40 anos) (azul escuro, 9 evasões) e Jovem Adulto (18-25 anos) (rosa, 3 evasões).
Ferraz, C., o segundo em volume de matrículas (45), tem um corpo discente majoritariamente composto por Adolescente (13-17 anos) e Infantil (1-12 anos)" (com 17 e 13 matrículas, respectivamente). Miranda, E. (38 matrículas) possui uma distribuição relativamente equilibrada de alunos entre as faixas Adolescente (13-17 anos) (11 matrículas) e Adulto (26-40 anos) (9 matrículas).
O professor Rezende, L. (34 matrículas) foca seu atendimento principalmente nas faixas Adolescente (13-17 anos) com 8 matrículas e Infantil (1-12 anos) com 11. Abreu, V. (33 matrículas) também atende predominantemente a estas duas faixas, mas com presença de outras. Soares, A. (29 matrículas) tem em sua maioria alunos Adulto (26-40 anos) com 10 matrículas.

## 3.6 Sugestões à empresa com base nas análises dos dashboards

A análise dos dashboards desenvolvidos no Power BI, detalhada nas seções anteriores (referenciando as análises das Figuras 6 a 20), não apenas responde às KIQs inicialmente formuladas, mas também fornece análises extras com uma base sólida para a tomada de decisões estratégicas e a implementação de ações corretivas e preventivas na Escola de Música. A seguir, são apresentadas sugestões de decisões e ações, agrupadas por áreas temáticas identificadas a partir dos insights dos gráficos.

### 3.6.1 Gestão da evasão sazonal e temporal

- Insights derivados: Identificou-se um pico significativo de evasões no mês de dezembro, seguido por abril e janeiro (Figura 6). Fevereiro, por outro lado, apresenta o menor índice de evasão.
- Decisões sugeridas: 
    - Planejamento proativo para períodos críticos:
        - Implementar campanhas de renovação de matrícula antecipada com incentivos (descontos, bônus) nos meses que antecedem dezembro e janeiro, visando garantir a continuidade dos alunos.
        - Desenvolver um calendário de atividades de engajamento (workshops, apresentações internas, aulas temáticas) especificamente para os meses de dezembro, janeiro e abril, buscando manter os alunos motivados e conectados à escola durante períodos de férias ou maior propensão à desistência.
    - Análise aprofundada de picos atípicos: Investigar as causas específicas da alta evasão em abril, um mês que não coincide com férias prolongadas, para entender os fatores contextuais que podem estar influenciando as desistências.
    - Potencialização de períodos favoráveis: Utilizar o mês de fevereiro, que historicamente apresenta menor evasão, para intensificar campanhas de captação de novos alunos e para programas de boas-vindas e integração que reforcem o compromisso dos alunos que retornam ou iniciam.

### 3.6.2 Otimização da oferta de cursos e foco na retenção específica

- Diagnóstico e melhoria contínua de cursos críticos:
    - Realizar uma análise qualitativa (pesquisas de satisfação, entrevistas com alunos e ex-alunos) para entender as razões da alta evasão nos cursos de "Violão individual" e "Canto individual". Os motivos podem estar relacionados à metodologia, material didático, adequação das expectativas dos alunos, ou dificuldades específicas de aprendizado
    - Com base no feedback, promover ajustes nos planos de ensino, oferecer materiais de apoio diferenciados ou criar módulos introdutórios que alinhem melhor as expectativas.
- Aumento do engajamento em cursos populares: Considerar a criação de atividades complementares para os cursos com evasões notáveis, como workshops de técnica, masterclasses com músicos convidados, ou oportunidades de apresentação em grupo, para aumentar a motivação e o senso de comunidade.


### 3.6.3 Desenvolvimento e acompanhamento estratégico do corpo docente

- <b>Insights derivados</b>: Alguns professores apresentam taxas de evasão significativamente altas, chegando a 100% em casos de baixo volume de alunos (Figura 18). Mesmo professores com grande número de matrículas podem ter taxas de evasão preocupantes (ex: Silveira M. com 63%, Rezende L. com 79%) (Figuras 10, 11 e 18). A taxa de evasão geral da escola atingiu 64% (Figura 18). As evasões de cada professor estão distribuídas de forma variada entre os cursos (Figura 13) e faixas etárias (Figuras 19 e 20) que lecionam.
- <b>Decisões sugeridas</b>:
    - Programa de desenvolvimento e suporte docente:
        - Implementar um programa contínuo de desenvolvimento pedagógico e suporte individualizado, com foco especial nos professores que apresentam as taxas de evasão mais elevadas.
        - Utilizar os dados das figuras 13, 15, e 20 para discutir com cada professor o perfil de seus alunos (cursos e faixas etárias) e as respectivas taxas de evasão, buscando soluções conjuntas.
    - Feedback e avaliação: Conduzir pesquisas regulares de satisfação dos alunos em relação aos professores e suas metodologias, conforme recomendado no item 2.6.3 deste trabalho.
    - Gestão de casos críticos: Para professores com altas taxas de evasão, realizar uma análise aprofundada e individualizada das causas. Definir um plano de ação que pode incluir mentoria intensiva, observação de aulas, ou, se necessário, reavaliação da alocação de turmas.
    - Reconhecimento e disseminação de boas práticas: Identificar e reconhecer os professores com baixas taxas de evasão e bom desempenho em retenção (ex: SOUSA, D. ), incentivando a partilha de suas metodologias e práticas de sucesso com os demais colegas.
    - Meta institucional: Estabelecer a redução da taxa de evasão geral da escola (atualmente em 64%) como uma meta estratégica prioritária, com acompanhamento trimestral através dos dashboards e definição de submetas por área ou fator de influência.
### 3.6.4 Implementação de estratégias diferenciadas por faixa etária

- <b>Insights Derivados</b>: O bairro Centro lidera em evasões absolutas, com uma taxa de evasão proporcionalmente muito elevada (Figuras 14 e 17). Monte Castelo possui muitas matrículas, mas também um número expressivo de evasões. Bairros como Santa Fé e Carandá Bosque apresentam altas taxas de evasão.
- <b>Decisões Sugeridas</b>
    -  Análise do impacto da localização Central: Investigar a fundo os motivos da alta evasão de alunos do bairro Centro, onde a escola está localizada. Considerar fatores como maior acesso a escolas concorrentes, outros custos associados ou se o perfil de alunos do centro tem características particulares.
    - Ações de relacionamento comunitário: Para bairros com alto volume de matrículas e evasões (ex: Monte Castelo), desenvolver ações de relacionamento específicas, como apresentações de alunos em eventos comunitários do bairro ou parcerias com associações locais.
    - Investigação em bairros com alta taxa de evasão: Para bairros com taxas de evasão proporcionalmente altas (mesmo com menor volume absoluto de alunos), como Santa Fé, Carandá Bosque e Residencial Damha III, avaliar possíveis barreiras como dificuldade de transporte, segurança no trajeto, ou forte presença de alternativas de ensino musical mais próximas ou acessíveis.
    - Marketing e captação geolocalizados: Utilizar os dados de matrículas e evasões por bairro para otimizar campanhas de marketing, direcionando esforços para bairros com bom potencial de captação e retenção, ou criando ofertas específicas para áreas com desafios logísticos.


### 3.6.5 Ações estratégicas baseadas na localização geográfica dos alunos
- <b>Insights Derivados</b>: A faixa etária dos Adolescentes (13-17 anos) representa a maior parcela das evasões em números absolutos (Figuras 15, 16). As faixas de Adultos (26-40 e 41-59 anos) também são significativas. Algumas faixas, como Adulto (26-40) e Melhor idade (60+), podem apresentar taxas de evasão proporcionalmente altas (Figura 15).
- <b>Decisões Sugeridas</b>
    -  Abordagens pedagógicas segmentadas: Desenvolver e implementar abordagens de ensino, materiais didáticos e estratégias de comunicação que sejam especificamente adaptadas às necessidades, interesses e desafios de cada faixa etária crítica.
    - Compreensão das necessidades específicas: Realizar grupos focais ou pesquisas com alunos de diferentes faixas etárias para entender melhor suas motivações para aprender música, suas dificuldades e o que mais valorizam na experiência escolar.
    - Engajamento da Melhor Idade: Para os alunos da Melhor idade (60+), investigar se os objetivos (lazer, socialização, desenvolvimento cognitivo) estão sendo atendidos e se há oportunidades para fortalecer o vínculo com a escola através de atividades sociais ou repertório musical específico.

## 3.7 Sugestões à empresa para melhorias no uso do sistema e na qualidade dos dados 

- <b>Insights Derivados</b>: Durante a recente triagem de dados, foi identificado um problema relevante, como a existência de diversos campos não preenchidos no sistema Emusys, em especial informações fundamentais como data de nascimento, bairro e motivo da finalização do contrato. Essa falha compromete a integridade dos dados e pode impactar negativamente nas análises e tomadas de decisão.
- <b>Decisões Sugeridas</b>: para resolver essa questão e evitar recorrências, sugerimos as seguintes ações aos gestores da empresa:
    - Capacitação do responsável pela alimentação dos dados: Promover um treinamento específico sobre a importância da completude dos dados e o uso adequado do sistema Emusys. Reforçar a responsabilidade e o impacto direto que o preenchimento incorreto causa em processos internos e relatórios.
    - Criação de regras de validação no sistema: Sugerir à gestão que converse com o administrador do sistema Emusys para a possibilidade de configuração do sistema para que certos campos considerados obrigatórios (como data de nascimento e bairro) não possam ser deixados em branco. Isso reduz o risco de erros por esquecimento ou desatenção.
    - Checklists operacionais: Disponibilizar um checklist simples que oriente os responsáveis sobre quais campos precisam ser obrigatoriamente preenchidos em cada tipo de cadastro.
    - Monitoramento contínuo e feedback regular: Implementar uma rotina periódica de revisão dos dados inseridos, com retorno imediato ao responsável sempre que falhas forem identificadas. Isso contribui para o aprendizado contínuo e evita acúmulo de inconsistências.
    - Padronização de procedimentos: Criar e divulgar um manual interno com orientações padronizadas sobre o preenchimento correto dos cadastros no sistema, de forma objetiva e acessível.
    - Acompanhamento da liderança: Envolver a liderança direta no acompanhamento do desempenho dessa atividade, reforçando a importância do zelo com a informação.


Com a adoção dessas medidas, a empresa poderá garantir maior confiabilidade nos dados, melhorar seus processos e fortalecer a base para análises futuras mais precisas e assertivas.





