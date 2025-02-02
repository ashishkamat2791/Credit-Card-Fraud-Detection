import happybase
import logging
logging.basicConfig(filename='dao.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class HBaseDao:
    """
    Dao class for operation on HBase
    """
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if HBaseDao.__instance == None:
            HBaseDao()
        return HBaseDao.__instance

    def __init__(self):
        if HBaseDao.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            HBaseDao.__instance = self
            self.host = '3.235.223.92'
            for i in range(2):
                try:
                    self.pool = happybase.ConnectionPool(size=3, host=self.host, port=9090)
                    break
                except Exception as e:
                    logger = logging.getLogger('HBaseDao')
                    logger.error(f'Exception in connecting HBase: {str(e)}')

    def get_data(self, key, table):
        for i in range(2):
            try:
                with self.pool.connection() as connection:
                    t = connection.table(table)
                    row = t.row(key)
                    return row
            except Exception as e:
                logger = logging.getLogger('HBaseDao')
                logger.error(f'Error in get_data for key {key}: {str(e)}')
                self.reconnect()

    def write_data(self, key, row, table):
        for i in range(2):
            try:
                with self.pool.connection() as connection:
                    t = connection.table(table)
                    t.put(key, row)
            except:
                self.reconnect()

    def reconnect(self):
        self.pool = happybase.ConnectionPool(size=3, host=self.host)
