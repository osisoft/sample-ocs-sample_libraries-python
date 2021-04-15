import json
from __future__ import annotations  # To type hint the enclosing class

from .. import SDS
from .Enum import SdsExtrapolationMode, SdsInterpolationMode
from .SdsTypeProperty import SdsTypeProperty


class SdsType(object):
    """Sds type definitions"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 sds_type_code: SDS.SdsTypeCode = None, is_generic_type: bool = None,
                 is_reference_type: bool = None, generic_arguments: list[SdsType] = None,
                 properties: list[SdsTypeProperty] = None, base_type: SdsType = None,
                 derived_types: list[SdsType] = None,
                 interpolation_mode: SdsInterpolationMode = None,
                 extrapolation_mode: SdsExtrapolationMode = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param sds_type_code: required
        :param is_generic_type: not required
        :param is_reference_type: not required
        :param generic_arguments: not required
        :param properties: required
        :param base_type: not required
        :param derived_types: not required
        :param interpolation_mode: not required
        :param extrapolation_mode: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.SdsTypeCode = sds_type_code
        self.IsGenericType = is_generic_type
        self.IsReferenceType = is_reference_type
        self.GenericArguments = generic_arguments
        self.Properties = properties
        self.BaseType = base_type
        self.DerivedTypes = derived_types
        self.InterpolationMode = interpolation_mode
        self.ExtrapolationMode = extrapolation_mode

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self._id

    @Id.setter
    def Id(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._id = value

    @property
    def Name(self) -> str:
        """
        not required
        :return:
        """
        return self._name

    @Name.setter
    def Name(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self._description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._description = value

    @property
    def SdsTypeCode(self) -> SDS.SdsTypeCode:
        """
        SdsTypeCode    required
        :return:
        """
        return self._type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SDS.SdsTypeCode):
        """
        SdsTypeCode    required
        :param value:
        :return:
        """
        self._type_code = value

    @property
    def IsGenericType(self) -> bool:
        """
        not required
        :return:
        """
        return self._is_generic_type

    @IsGenericType.setter
    def IsGenericType(self, value: bool):
        """
        not required
        :param value:
        :return:
        """
        self._is_generic_type = value

    @property
    def IsReferenceType(self) -> bool:
        """
        not required
        :return:
        """
        return self._is_reference_type

    @IsReferenceType.setter
    def IsReferenceType(self, value: bool):
        """
        not required
        :param value:
        :return:
        """
        self._is_reference_type = value

    @property
    def GenericArguments(self) -> list[SdsType]:
        """
        not required
        :return:
        """
        return self._generic_arguments

    @GenericArguments.setter
    def GenericArguments(self, value: list[SdsType]):
        """
        not required
        :param value:
        :return:
        """
        self._generic_arguments = value

    @property
    def Properties(self) -> list[SdsTypeProperty]:
        """
        required
        :return:
        """
        return self._properties

    @Properties.setter
    def Properties(self, value: list[SdsTypeProperty]):
        """
        required
        :param value:
        :return:
        """
        self._properties = value

    @property
    def BaseType(self) -> SdsType:
        """
        not required
        :return:
        """
        return self._base_type

    @BaseType.setter
    def BaseType(self, value: SdsType):
        """
        not required
        :param value:
        :return:
        """
        self._base_type = value

    @property
    def DerivedTypes(self) -> list[SdsType]:
        """
        not required
        :return:
        """
        return self._base_types

    @DerivedTypes.setter
    def DerivedTypes(self, value: list[SdsType]):
        """
        not required
        :param value:
        :return:
        """
        self._base_types = value

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

    @property
    def ExtrapolationMode(self) -> SdsExtrapolationMode:
        """
        not required
        :return:
        """
        return self._extrapolation_mode

    @ExtrapolationMode.setter
    def ExtrapolationMode(self, value: SdsExtrapolationMode):
        """
        not required
        :param value:
        :return:
        """
        self._extrapolation_mode = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id,
                  'SdsTypeCode': self.SdsTypeCode.name, 'Properties': []}
        if self.Properties is not None:
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.IsGenericType is not None:
            result['IsGenericType'] = self.IsGenericType

        if self.IsReferenceType is not None:
            result['IsReferenceType'] = self.IsReferenceType

        if self.GenericArguments is not None:
            result['GenericArguments'] = []
            for value in self.GenericArguments:
                result['GenericArguments'].append(value.toDictionary())

        if self.BaseType is not None:
            result['BaseType'] = self.BaseType.toDictionary()

        if self.DerivedTypes is not None:
            result['DerivedTypes'] = []
            for value in self.DerivedTypes:
                result['DerivedTypes'].append(value.toDictionary())

        if self.InterpolationMode is not None:
            result['InterpolationMode'] = self.InterpolationMode.name

        if self.ExtrapolationMode is not None:
            result['ExtrapolationMode'] = self.ExtrapolationMode.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsType()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'SdsTypeCode' in content:
            result.SdsTypeCode = SDS.SdsTypeCode(content['SdsTypeCode'])

        if 'IsGenericType' in content:
            result.IsGenericType = content['IsGenericType']

        if 'IsReferenceType' in content:
            result.IsReferenceType = content['IsReferenceType']

        if 'GenericArguments' in content:
            generic_arguments = content['GenericArguments']
            if generic_arguments is not None and len(generic_arguments) > 0:
                result.GenericArguments = []
                for value in generic_arguments:
                    result.GenericArguments.append(SdsType.fromJson(value))

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(SdsTypeProperty.fromJson(value))

        if 'BaseType' in content:
            result.BaseType = SdsType.fromJson(content['BaseType'])

        if 'DerivedTypes' in content:
            derived_types = content['DerivedTypes']
            if derived_types is not None and len(derived_types) > 0:
                result.DerivedTypes = []
                for value in derived_types:
                    result.DerivedTypes.append(SdsType.fromJson(value))

        if 'InterpolationMode' in content:
            result.InterpolationMode = SdsInterpolationMode(
                content['InterpolationMode'])

        if 'ExtrapolationMode' in content:
            result.ExtrapolationMode = SdsExtrapolationMode(
                content['ExtrapolationMode'])

        return result
