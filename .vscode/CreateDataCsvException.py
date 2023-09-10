import Ss7PyException


# CreateDataCsvに関連する例外
class CsvNotFoundError(Ss7PyException):
    """CSVファイルが存在しない場合に発生する例外"""


class CsvValidationError(Ss7PyException):
    """指定されたファイルがCSV形式になっていない場合に発生する例外"""


class CsvInconsistencyError(Ss7PyException):
    """CSVファイル内の項目に不整合がある場合に発生する例外"""


class CsvCannotOpenError(Ss7PyException):
    """CSVファイルを開けない場合に発生する例外"""


class BasicInfomationError(Ss7PyException):
    """CSVファイルの基本事項セクションを読み取れない場合に発生する例外"""


class StructureTypeRestrictedError(Ss7PyException):
    """構造種別に対応したライセンスがない場合に発生する例外"""


class NumberOfFloorRestrictedError(Ss7PyException):
    """階数に対応したライセンスが無い場合に発生する例外"""


class InvalidSavePathError(Ss7PyException):
    """モデルデータの保存先パスが不正だった場合に発生する例外"""


class FileInUseError(Ss7PyException):
    """保存先のファイルが使用中だった場合に発生する例外"""


class FileExistsError(Ss7PyException):
    """既にファイルが存在しており保存出来ない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """ファイルが上書き禁止になっている場合に発生する例外"""


class CreateFromCsvError(Ss7PyException):
    """不明な理由により新規作成に失敗した場合に発生する例外"""


class WoodStructureLicenseMissingError(Ss7PyException):
    """Op.木造ラーメンのライセンスがない場合に発生する例外"""


class IsolationStructureLicenseMissingError(Ss7PyException):
    """Op.免震部材のライセンスがない場合に発生する例外"""


class CsvFileConflictError(Ss7PyException):
    """物件フォルダ内にCSVファイルがあり上書きできない場合に発生する例外"""


class VersionMismatchError(Ss7PyException):
    """上書き前後でモデルデータのSS7バージョンが変わってしまう場合に発生する例外"""


class PremiumLicenseMissingError(Ss7PyException):
    """SS7 Premiumのライセンスがない場合に発生する例外"""
