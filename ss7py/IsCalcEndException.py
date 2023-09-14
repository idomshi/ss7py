import Ss7PyException


# IsCalcEndに関連する例外
class ResultNotFoundError(Ss7PyException):
    """指定された結果が存在しない場合に発生する例外"""


class ResultNameInvalidError(Ss7PyException):
    """不正な結果名が指定された場合に発生する例外"""


class InvalidCalculationItemError(Ss7PyException):
    """不正な項目名が指定された場合に発生する例外"""


class TallyLicenseMissingError(Ss7PyException):
    """Op.積算のライセンスがない場合に発生する例外"""
