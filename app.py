from loguru import logger

# Mensagens de log de diferentes níveis
logger.debug("Isso é uma mensagem de debug")
logger.info("Isso é uma mensagem informativa")
logger.warning("Isso é um aviso")
logger.error("Isso é um erro")
logger.critical("Isso é crítico")

# A saída será exibida no console

# Configurando o arquivo de log com rotação de 5MB
logger.add("log/meu_app.log", rotation="5 MB")

logger.info("Essa mensagem será salva no arquivo")