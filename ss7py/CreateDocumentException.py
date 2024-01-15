from .Ss7PyException import Ss7PyException


# CreateDocumentに関連する例外
class CreateDocumentError(Ss7PyException):
    """不明な理由で出力に失敗した場合に発生する例外"""


class ResultNameInvalidError(Ss7PyException):
    """不正な結果名を指定した場合に発生する例外"""


class InvalidItemNameError(Ss7PyException):
    """不正な出力項目を指定した場合に発生する例外"""


class InvalidFileNameError(Ss7PyException):
    """不正な出力ファイル名を指定した場合に発生する例外"""


class StructureTypeRestrictedError(Ss7PyException):
    """構造種別に対応したライセンスがない場合に発生する例外"""


class FloorNumberRestrictedError(Ss7PyException):
    """ライセンスの階数制限を超えたモデルで計算書出力をしようとした場合に発生する例外"""


class TallyLicenseMissingError(Ss7PyException):
    """Op.積算のライセンスがない場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """ファイルが存在しており保存出来ない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """ファイルが上書き禁止になっている場合に発生する例外"""


class OutputFailedError(Ss7PyException):
    """出力処理が不正終了した場合に発生する例外"""


class WoodStructureLicenseMissingError(Ss7PyException):
    """Op.木造ラーメンのライセンスがない場合に発生する例外"""


class IsolationStructureLicenseMissingError(Ss7PyException):
    """Op.免震部材のライセンスがない場合に発生する例外"""


class PremiumLicenseMissingError(Ss7PyException):
    """SS7 Premiumのライセンスがない場合に発生する例外"""
