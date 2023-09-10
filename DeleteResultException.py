import Ss7PyException


# DeleteResultに関連する例外
class ResultNotFoundError(Ss7PyException):
    """指定された解析結果が存在しない場合に発生する例外"""


class ResultNameInvalidError(Ss7PyException):
    """不正な解析結果名が指定された場合に発生する例外"""


class ResultPermissionError(Ss7PyException):
    """指定された解析結果が上書き禁止になっている場合に発生する例外"""


class ResultDeleteError(Ss7PyException):
    """不明な理由により結果の削除に失敗した場合に発生する例外"""
