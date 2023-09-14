import Ss7PyException

# LinkSS3に関連する例外


class ReadSs3DataError(Ss7PyException):
    """SS3データ情報が読み込めない場合に発生する例外"""


class GetSs3LinkVersionLimitCheckError(Ss7PyException):
    """SS3リンクのバージョン上限値の取得に失敗した場合に発生する例外"""


class GetSs3LinkVersionLimitError(Ss7PyException):
    """SS3リンクのバージョン上限の制限に抵触した場合に発生する例外"""


class StructureTypeRestrictedError(Ss7PyException):
    """構造種別に対応したライセンスがない場合に発生する例外"""


class LimitStrengthCalculationError(Ss7PyException):
    """SS3データに限界耐力計算が指定されている場合に発生する例外"""


class InvalidPathError(Ss7PyException):
    """不正なパスがリンク先として与えられた場合に発生する例外"""


class FileInUseError(Ss7PyException):
    """リンク先のファイルが使用中だった場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """リンク先にファイルが存在しており保存出来ない場合に発生する例外"""


class Ss3LinkError(Ss7PyException):
    """不明な理由によりリンク処理に失敗した場合に発生する例外"""


class Ss3FileConflictError(Ss7PyException):
    """物件フォルダ内にリンク元のSS3ファイルがあり上書きできない場合に発生する例外"""
