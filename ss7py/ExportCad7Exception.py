from .Ss7PyException import Ss7PyException


# ExpotCad7に関連する例外
class InvalidResultNameError(Ss7PyException):
    """不正な解析結果名が指定された場合に発生する例外"""


class InvalidFileNameError(Ss7PyException):
    """不正なファイル名が与えられた場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """ファイルが存在しており保存出来ない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """ファイルが上書き禁止になっている場合に発生する例外"""


class ExportCad7Error(Ss7PyException):
    """不明な理由によりCAD7のエクスポートが失敗した場合に発生する例外"""
