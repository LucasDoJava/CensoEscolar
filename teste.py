import pandas as pd
import json

# Carregando os dados do arquivo csv
dados = pd.read_csv("microdados_ed_basica_2023.csv", encoding="ISO-8859-1", delimiter=";")

# Capturando os dados pela sigla PB
dados_pb = dados[dados["SG_UF"] == "PB"]

# Lista onde será inserido o ojeto json
censo_escolar = []

# Iterando as linhas das colunas para um formato json
for _, row in dados_pb.iterrows():
    censo = {
        "região": row["NO_REGIAO"],
        "UF": row["SG_UF"],
        "município": row["NO_MUNICIPIO"],
        "mesoregião": row["NO_MESORREGIAO"],
        "microregião": row["NO_MICRORREGIAO"],
        "entidade": row["NO_ENTIDADE"]
    }
    # Adicionando o objeto json a lista
    censo_escolar.append(censo)

# Extraindo os dados para o objeto json em um arquivo .js
with open("censo_escolar.js", "w", encoding="utf-8") as js_file:
    js_file.write("let censo_escolar = ")
    js_file.write(json.dumps(censo_escolar, ensure_ascii=False, indent=2))
    js_file.write(";")
