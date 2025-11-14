import pandas as pd
import os
import glob

# FUNCAO DE EXTRACT QUE LE E CONSOLIDA OS JSON
def extract_data(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# FUNCAO QUE TRANSFORMA
def transform_data(df_total: pd.DataFrame) -> pd.DataFrame:
    df_total["Total"] = df_total["Quantidade"] * df_total["Venda"]

    return df_total

# UMA FUNCAO Q DA LOAD EM CSV OU PARQUET
def load_data(format_saida: list, df_total: pd.DataFrame):

    for format in format_saida:
        if format == 'csv':
            df_total.to_csv("transformed_data/data.csv", index=False)
        if format == 'parquet':
            df_total.to_parquet("transformed_data/data.parquet")

def pipeline_calcular_kpi_vendas_consolidado(path: str, formato_saida: list):

    df_extract = extract_data(path)
    df_transformed = transform_data(df_total=df_extract)
    load_data(formato_saida, df_transformed)
    