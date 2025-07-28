import pandas as pd
from sqlalchemy import create_engine

# Parâmetros — ajuste conforme necessário
excel_path = r"C:\Users\milenaaxs\Desktop\scriptimportcsvsql\BASE_COBRANÇA_2025 NOVA.xlsx"
sheet_name = "BASE 2025"      # ou nome da aba correta
mysql_url = "mysql+mysqlconnector://root:741598ma@localhost:3306/base_cobrança_corrigido"
tabela     = "base_cobranca_corrigido"

# Carrega todo o Excel de uma vez
df = pd.read_excel(excel_path, sheet_name=sheet_name, engine="openpyxl")

# Remove linhas totalmente vazias
df = df.dropna(how="all")

# Padroniza nomes de coluna para MySQL
df.columns = (
    df.columns
      .astype(str)
      .str.strip()
      .str.replace(" ", "_")
      .str.replace(r"[^\w]", "", regex=True)
      .str[:64]
)

# (Opcional) converta tipos
# df["Valor"] = df["Valor"].astype(float)
# df["Data"]  = pd.to_datetime(df["Data"], dayfirst=True)

# 1.3) Exporta para o MySQL (replace ou append)
engine = create_engine(mysql_url)
df.to_sql(name=tabela, con=engine, if_exists="replace", index=False)

print("✅ Importação concluída com pandas!")