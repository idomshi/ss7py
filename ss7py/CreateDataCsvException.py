from .Ss7PyException import Ss7PyException

# CreateDataCsvに関連する例外


class CsvFileNotFoundError(Ss7PyException):
    """CSVファイルが見つからない場合に発生する例外"""


class InvalidCsvFileError(Ss7PyException):
    """CSVファイルの内容が規定のフォーマットではない場合に発生する例外"""


class InvalidCsvDataError(Ss7PyException):
    """読み込んだ階数やスパン数などに不整合がある場合に発生する例外"""


class FileCannotOpenError(Ss7PyException):
    """CSVファイルを開けない場合に発生する例外"""


class CannotReadBasicInformationError(Ss7PyException):
    """CSVファイルの基本事項セクションが読み込めない場合に発生する例外"""


class StructureTypeRestrictedError(Ss7PyException):
    """構造種別に対応したライセンスが無い場合に発生する例外"""


class FloorNumberRestrictedError(Ss7PyException):
    """ライセンスの階数制限を超えたモデルを生成しようとした場合に発生する例外"""


class InvalidPathError(Ss7PyException):
    """生成先に不正なパスを指定した場合に発生する例外"""


class FileLockError(Ss7PyException):
    """生成先のファイルが使用中でモデルを生成できない場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """生成先のファイルが存在しておりモデルを生成できない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """生成先のファイルが上書き禁止でモデルを生成できない場合に発生する例外"""


class UnknownCreateModelError(Ss7PyException):
    """不明な理由によりモデル生成に失敗した場合に発生する例外"""


class WoodStructureLicenseMissingError(Ss7PyException):
    """Op.木造ラーメンのライセンスが無くモデルを生成できない場合に発生する例外"""


class IsolationStructureLicenseMissingError(Ss7PyException):
    """Op.免震部材のライセンスが無くモデルを生成できない場合に発生する例外"""


class InputCsvContainedError(Ss7PyException):
    """元になるCSVファイルが生成先の物件フォルダに含まれておりモデルを生成できない場合に発生する例外"""


class VersionUnmatchedError(Ss7PyException):
    """生成先に存在するモデルデータと実行中のSS7のバージョンが異なる場合に発生する例外"""


class PremiumLicenseMissingError(Ss7PyException):
    """SS7 Premiumのライセンスが無くモデルを生成できない場合に発生する例外"""
