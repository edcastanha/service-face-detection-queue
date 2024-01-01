import logging

class LogManager:
    '''
    LogManager
    Exemplo::

    if __name__ == "__main__":
    log_manager = LogManager('my_logs.log')

    log_manager.log_info('Esta é uma mensagem de informação.')
    log_manager.log_warning('Este é um aviso.')
    log_manager.log_error('Ocorreu um erro.')
    try:
        # Algum código que pode gerar uma exceção
        raise ValueError('Um erro ocorreu aqui!')
    except ValueError as e:
        log_manager.log_exception('Ocorreu uma exceção: ' + str(e))

    
    '''
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO) 

        # Criar um manipulador para escrever logs em um arquivo
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)  # Nível de log para o arquivo

        # Definir o formato dos logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Adicionar o manipulador ao logger
        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, message):
        self.logger.exception(message)
