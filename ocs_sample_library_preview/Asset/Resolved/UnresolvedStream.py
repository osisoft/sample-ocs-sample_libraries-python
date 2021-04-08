class UnresolvedStream(object):
    def __init__(self, name: str = None, reason: str = None):
        self.Name = name
        self.Reason = reason

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Reason(self) -> str:
        return self.__reason

    @Reason.setter
    def Reason(self, value: str):
        self.__reason = value

    @staticmethod
    def from_json(content):
        result = UnresolvedStream()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Reason' in content:
            result.Reason = content['Reason']