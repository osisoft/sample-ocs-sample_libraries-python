from enum import Enum


class SdsSummaryType(Enum):
    """
    enum 0-4096  not fully inclusive
    """
    None_ = 0,
    Count = 1,
    Minimum = 2,
    Maximum = 4,
    Range = 8,
    Mean = 16,
    StandardDeviation = 32,
    PopulationStandardDeviation = 64,
    Total = 128,
    Skewness = 256,
    Kurtosis = 512,
    WeightedMean = 1024,
    WeightedStandardDeviation = 2048,
    WeightedPopulationStandardDeviation = 4096