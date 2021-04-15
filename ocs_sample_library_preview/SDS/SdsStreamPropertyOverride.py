import json

from .Enum import SdsInterpolationMode


class SdsStreamPropertyOverride(object):
    """
    Sds Stream PropertyOverride definitions
    """

    def __init__(self, sds_type_property_id: str = None, uom: str = None,
                 interpolation_mode: SdsInterpolationMode = None):
        """
        :param sds_type_property_id: required
        :param uom: not required
        :param interpolation_mode: not required
        """
        self.SdsTypePropertyId = sds_type_property_id
        self.Uom = uom
        self.InterpolationMode = interpolation_mode

    @property
    def SdsTypePropertyId(self) -> str:
        """
        required
        :return:
        """
        return self._sds_type_property_id

    @SdsTypePropertyId.setter
    def SdsTypePropertyId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._sds_type_property_id = value

    @property
    def Uom(self) -> str:
        """
        not required
        :return:
        """
        return self._uom

    @Uom.setter
    def Uom(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._uom = value

    @property
    def InterpolationMode(self) -> SdsInterpolationMode:
        """
        not required
        :return:
        """
        return self._interpolation_mode

    @InterpolationMode.setter
    def InterpolationMode(self, value: SdsInterpolationMode):
        """
        not required
        :param value:
        :return:
        """
        self._interpolation_mode = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'SdsTypePropertyId': self.SdsTypePropertyId}

        # optional properties
        if self.Uom is not None:
            result['Uom'] = self.Uom

        if self.InterpolationMode is not None:
            result['InterpolationMode'] = self.InterpolationMode

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamPropertyOverride()

        if not content:
            return result

        if 'SdsTypePropertyId' in content:
            result.SdsTypePropertyId = content['SdsTypePropertyId']

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'InterpolationMode' in content:
            result.InterpolationMode = SdsInterpolationMode[content['InterpolationMode']]

        return result
