from .Ss7PyException import Ss7PyException

# Openに関連する例外


class FileNotFoundError(Ss7PyException):
    """モデルデータが見つからない場合に発生する例外"""


class FileAlreadyOpenedError(Ss7PyException):
    """モデルデータがすでに開かれている場合に発生する例外"""


class BackupDataExistsError(Ss7PyException):
    """バックアップデータが存在するため指定によりファイルを開く処理を中断した場合に発生する例外"""


class FileVersionLowerError(Ss7PyException):
    """モデルデータのSS7バージョンが低いため指定によりファイルを開く処理を中断した場合に発生する例外"""


class FileVersionUpperError(Ss7PyException):
    """モデルデータのSS7バージョンが高いときに発生する例外"""


class StructureTypeRestrictedError(Ss7PyException):
    """構造種別に対応したライセンスがない場合に発生する例外"""


class FileWriteAccessError(Ss7PyException):
    """ファイルが上書き禁止になっている場合に発生する例外"""


class FileCannotOpenError(Ss7PyException):
    """モデルデータが開けない場合に発生する例外"""


class WoodStructureLicenseMissingError(Ss7PyException):
    """Op.木造ラーメンのライセンスがない場合に発生する例外"""


class IsolationStructureLicenseMissingError(Ss7PyException):
    """Op.免震部材のライセンスがない場合に発生する例外"""


class PremiumLicenseMissingError(Ss7PyException):
    """SS7 Premiumのライセンスがない場合に発生する例外"""
