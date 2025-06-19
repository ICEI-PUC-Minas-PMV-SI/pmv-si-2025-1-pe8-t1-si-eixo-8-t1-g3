import pandas as pd
import re

# Carrega o novo arquivo
df = pd.read_csv("todos as situações.csv", encoding="latin1")

# Define as colunas a manter
colunas_utilizadas = [
    'Nº do Aluno', 'Data de Nascimento', 'Data Matric.',
    'Curso / Situação', 'Conclusão', 'Bairro'
]
df = df[colunas_utilizadas]

# Função para extrair Nome do Curso e Nome do Professor
def extrair_blocos_sem_interrupcao(texto):
    linhas = [l.strip() for l in str(texto).split('\n') if l.strip()]
    blocos = []
    bloco_atual = {}

    for linha in linhas:
        if not linha.startswith("-"):
            if bloco_atual:
                blocos.append(bloco_atual)
            bloco_atual = {"Nome do Curso": linha, "Nome do Professor": ""}
        elif "prof." in linha.lower():
            bloco_atual["Nome do Professor"] = re.sub(r"^-+\s*", "", linha)

    if bloco_atual:
        blocos.append(bloco_atual)

    return blocos

# Processamento
linhas_expandidas = []

for _, row in df.iterrows():
    blocos = extrair_blocos_sem_interrupcao(row['Curso / Situação'])
    datas_matricula = [d.strip() for d in str(row['Data Matric.']).split('\n') if d.strip()]
    conclusoes = [c.strip() for c in str(row['Conclusão']).split('\n') if c.strip()]

    for i, bloco in enumerate(blocos):
        nova_linha = {
            "Nº do Aluno": row['Nº do Aluno'],
            "Data de Nascimento": row['Data de Nascimento'],
            "Data da Matrícula": datas_matricula[i] if i < len(datas_matricula) else '',
            "Nome do Curso": bloco['Nome do Curso'],
            "Nome do Professor": bloco['Nome do Professor'],
            "Conclusão": conclusoes[i] if i < len(conclusoes) else '',
            "Bairro": row['Bairro']
        }
        linhas_expandidas.append(nova_linha)

# Criar DataFrame final
df_final = pd.DataFrame(linhas_expandidas)

# Exportar o resultado
df_final.to_csv("situacoes_tratado.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'situacoes_tratado.csv' gerado com sucesso.")
