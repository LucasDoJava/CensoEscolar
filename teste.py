import pandas as pd
import json

# Carregando os dados do arquivo csv
dados = pd.read_csv("microdados_ed_basica_2023.csv", encoding="ISO-8859-1", delimiter=";")

# Capturando os dados pela sigla PB
dados_pb = dados[dados["SG_UF"] == "PB"]

# Lista onde será inserido o objeto json
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
    # Adicionando o objeto json à lista
    censo_escolar.append(censo)

# Salvando os dados em um arquivo JSON
with open("censo_escolar.json", "w", encoding="utf-8") as json_file:
    json.dump(censo_escolar, json_file, ensure_ascii=False, indent=2)
