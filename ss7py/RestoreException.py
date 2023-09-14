import Ss7PyException

# Restoreに関連する例外


class ResultNotFoundError(Ss7PyException):
    """指定された解析結果が存在しない場合に発生する例外"""


class ResultNameInvalidError(Ss7PyException):
    """不正な解析結果名が指定された場合に発生する例外"""


class StructureTypeRestrictedError(Ss7PyException):
    """構造種別に対応したライセンスがない場合に発生する例外"""


class ResultRestorationError(Ss7PyException):
    """不明な理由により解析結果の復元に失敗した場合に発生する例外"""


class WoodStructureLicenseMissingError(Ss7PyException):
    """Op.木造ラーメンのライセンスがない場合に発生する例外"""


class IsolationStructureLicenseMissingError(Ss7PyException):
    """Op.免震部材のライセンスがない場合に発生する例外"""


class PremiumLicenseMissingError(Ss7PyException):
    """SS7 Premiumのライセンスがない場合に発生する例外"""
