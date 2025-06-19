import pandas as pd
import re

# Carregar o CSV com codificação apropriada
df = pd.read_csv("interrompidos.csv", encoding="latin1")

# Selecionar as colunas relevantes
colunas_utilizadas = [
    'Nº do Aluno', 'Data de Nascimento', 'Data Matric.',
    'Curso / Situação', 'Conclusão', 'Bairro'
]
df = df[colunas_utilizadas]

# Função para extrair blocos de 'Curso / Situação'
def extrair_blocos_curso_situacao(texto):
    linhas = [l.strip() for l in str(texto).split('\n') if l.strip()]
    blocos = []
    bloco_atual = {}

    for linha in linhas:
        if not linha.startswith("-"):
            if bloco_atual:
                blocos.append(bloco_atual)
            bloco_atual = {"Nome do Curso": linha, "Nome do Professor": "", "Data da Interrupção": ""}
        elif "prof." in linha.lower():
            bloco_atual["Nome do Professor"] = re.sub(r"^-+\s*", "", linha)
        elif "interrompido" in linha.lower():
            data_match = re.search(r"(\d{2}/\d{2}/\d{4})", linha)
            if data_match:
                bloco_atual["Data da Interrupção"] = data_match.group(1)

    if bloco_atual:
        blocos.append(bloco_atual)

    return blocos

# Processamento
linhas_expandidas = []

for _, row in df.iterrows():
    blocos = extrair_blocos_curso_situacao(row['Curso / Situação'])
    datas_matricula = [d.strip() for d in str(row['Data Matric.']).split('\n') if d.strip()]
    conclusoes = [c.strip() for c in str(row['Conclusão']).split('\n') if c.strip()]

    for i, bloco in enumerate(blocos):
        nova_linha = {
            "Nº do Aluno": row['Nº do Aluno'],
            "Data de Nascimento": row['Data de Nascimento'],
            "Data da Matrícula": datas_matricula[i] if i < len(datas_matricula) else '',
            "Nome do Curso": bloco['Nome do Curso'],
            "Nome do Professor": bloco['Nome do Professor'],
            "Data da Interrupção": bloco['Data da Interrupção'],
            "Conclusão": conclusoes[i] if i < len(conclusoes) else '',
            "Bairro": row['Bairro']
        }
        linhas_expandidas.append(nova_linha)

# Criar DataFrame final e salvar
df_final = pd.DataFrame(linhas_expandidas)
df_final.to_csv("interrompidos_tratado.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'interrompidos_tratado.csv' gerado com sucesso.")
