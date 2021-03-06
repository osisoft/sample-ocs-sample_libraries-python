from enum import Enum


class FieldSource(Enum):
    """
    enum 0-6 fully inclusive
    """
    NotApplicable = 0
    Id = 1
    Name = 2
    PropertyId = 3
    PropertyName = 4
    Metadata = 5
    Tags = 6
