from .Ss7PyException import Ss7PyException


# ExportResultCsvに関連する例外
class InvalidItemNameError(Ss7PyException):
    """項目名に誤りがある場合に発生する例外"""


class ItemHasNoResultError(Ss7PyException):
    """指定された項目に出力できる内容が無い場合に発生する例外"""


class InvalidFileNameError(Ss7PyException):
    """不正なファイル名が指定された場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """ファイルが存在しており保存出来ない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """ファイルが上書き禁止になっている場合に発生する例外"""


class ExportResultFailedError(Ss7PyException):
    """不明な理由によりCSVのエクスポートに失敗した場合に発生する例外"""
