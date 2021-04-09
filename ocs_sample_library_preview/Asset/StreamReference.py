import json


class StreamReference(object):
    """OCS Asset Stream Reference definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 stream_id: str = None):
        """
        :param id: required
        :param name: required
        :param description: not required
        :param stream_id: required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.StreamId = stream_id

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def Name(self) -> str:
        """
        required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self.__description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__description = value

    @property
    def StreamId(self) -> str:
        """
        required
        :return:
        """
        return self.__stream_id

    @StreamId.setter
    def StreamId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__stream_id = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        # required properties
        result = {'Id': self.Id, 'Name': self.Name,
                  'StreamId': self.StreamId}

        # optional properties
        if hasattr(self, 'Description'):
            result['Description'] = self.Description

        return result

    @staticmethod
    def from_json(content):
        result = StreamReference()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'StreamId' in content:
            result.StreamId = content['StreamId']

        return result
