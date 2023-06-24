class InstantiateCSVError(Exception):
    """Исключение, выполняемое в случае отсутствия необходимых полей в файле"""
    def __str__(self):
        return "Файл items.csv поврежден"