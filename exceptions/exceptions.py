class InstantiateCSVError(Exception):
    def __init__(self, msg='Ошибка'):
        self.msg = msg

    def __str__(self):
        return self.msg