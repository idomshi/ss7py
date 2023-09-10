import Ss7PyException


# Calculateに関連する例外
class InvalidResultNameError(Ss7PyException):
    """不正な解析結果名が指定された場合に発生する例外"""


class OverwriteRestrictedError(Ss7PyException):
    """ロックされている解析結果を上書きしようとした場合に発生する例外"""


class InvalidCalculationItemError(Ss7PyException):
    """計算項目名に誤りがある場合に発生する例外"""


class CalculationAlreadyFinishedError(Ss7PyException):
    """指定された計算項目がすべて計算済みである場合に発生する例外"""


class FloorNumberRestrictedError(Ss7PyException):
    """ライセンスの階数制限を超えたモデルで計算をしようとした場合に発生する例外"""


class TallyLicenseMissingError(Ss7PyException):
    """計算項目に積算を指定したがOp.積算のライセンスがない場合に発生する例外"""


class CalculationError(Ss7PyException):
    """計算が不正終了した場合に発生する例外"""


class UnknownCalculationError(Ss7PyException):
    """不明な理由により計算が失敗した場合に発生する例外"""
