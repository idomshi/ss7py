from .Ss7PyException import Ss7PyException


# ExportInputCsvに関連する例外
class InvalidFileNameError(Ss7PyException):
    """不正なファイル名を指定した場合に発生する例外"""


class KeywordDuplicatedError(Ss7PyException):
    """符号名、階名などの名称重複がありCSV出力が中断された場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """ファイルが存在しており保存出来ない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """ファイルが上書き禁止になっている場合に発生する例外"""
