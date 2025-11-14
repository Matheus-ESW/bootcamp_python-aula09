from etl import pipeline_calcular_kpi_vendas_consolidado

pasta_argumento = 'data'
formatos_saida = ['csv', 'parquet']
pipeline_calcular_kpi_vendas_consolidado(pasta_argumento, formatos_saida)