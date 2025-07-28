import pandas as pd
from sqlalchemy import create_engine

# dados de acesso sql e origem dos arquivos
excel_path = r"C:\Users\milenaaxs\Desktop\scriptimportcsvsql\BASE_COBRANÇA_2025 NOVA.xlsx"
sheet_name = "BASE 2025"     # nome da aba correta no excel
mysql_url = "mysql+mysqlconnector://root:senharoot@localhost:portatoot/base_cobrança_corrigido"
tabela     = "base_cobranca_corrigido"

# Carrega o excel
df = pd.read_excel(excel_path, sheet_name=sheet_name, engine="openpyxl")

# removendo linhas sem conteúdo
df = df.dropna(how="all")

# organizando padrão de colunas
df.columns = (
    df.columns
      .astype(str)
      .str.strip()
      .str.replace(" ", "_")
      .str.replace(r"[^\w]", "", regex=True)
      .str[:64]
)


# Exporta para o MySQL 
engine = create_engine(mysql_url)
df.to_sql(name=tabela, con=engine, if_exists="replace", index=False)

print("✅ Importação concluída com pandas!")
