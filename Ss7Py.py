from enum import Enum
from Ssp import Ss7Python as Ss7
import CommonException


# # CreateDataCsvに関連する例外
# class CsvNotFoundError(Ss7PyException):
#     """CSVファイルが存在しない場合に発生する例外"""

# class CsvValidationError(Ss7PyException):
#     """指定されたファイルがCSV形式になっていない場合に発生する例外"""

# class CsvInconsistencyError(Ss7PyException):
#     """CSVファイル内の項目に不整合がある場合に発生する例外"""

# class CsvCannotOpenError(Ss7PyException):
#     """CSVファイルを開けない場合に発生する例外"""

# class BasicInfomationError(Ss7PyException):
#     """CSVファイルの基本事項セクションを読み取れない場合に発生する例外"""

# # class StructureTypeRestrictedError(Ss7PyException):
# #     """構造種別に対応したライセンスがない場合に発生する例外"""

# class NumberOfFloorRestrictedError(Ss7PyException):
#     """階数に対応したライセンスが無い場合に発生する例外"""

# class InvalidSavePathError(Ss7PyException):
#     """モデルデータの保存先パスが不正だった場合に発生する例外"""

# class FileInUseError(Ss7PyException):
#     """保存先のファイルが使用中だった場合に発生する例外"""

# class FileExistsError(Ss7PyException):
#     """既にファイルが存在しており保存出来ない場合に発生する例外"""

# # class FileWriteAccessError(Ss7PyException):
# #     """ファイルが上書き禁止になっている場合に発生する例外"""

# class CreateFromCsvError(Ss7PyException):
#     """不明な理由により新規作成に失敗した場合に発生する例外"""

# # class WoodStructureLicenseMissingError(Ss7PyException):
# #     """Op.木造ラーメンのライセンスがない場合に発生する例外"""

# # class IsolationStructureLicenseMissingError(Ss7PyException):
# #     """Op.免震部材のライセンスがない場合に発生する例外"""

# class CsvFileConflictError(Ss7PyException):
#     """物件フォルダ内にCSVファイルがあり上書きできない場合に発生する例外"""

# class VersionMismatchError(Ss7PyException):
#     """上書き前後でモデルデータのSS7バージョンが変わってしまう場合に発生する例外"""

# # class PremiumLicenseMissingError(Ss7PyException):
# #     """SS7 Premiumのライセンスがない場合に発生する例外"""

# # DeleteResultに関連する例外
# # class ResultNotFoundError(Ss7PyException):
# #     """指定された解析結果が存在しない場合に発生する例外"""

# # class ResultNameInvalidError(Ss7PyException):
# #     """不正な解析結果名が指定された場合に発生する例外"""

# class ResultPermissionError(Ss7PyException):
#     """指定された解析結果が上書き禁止になっている場合に発生する例外"""

# class ResultDeleteError(Ss7PyException):
#     """不明な理由により結果の削除に失敗した場合に発生する例外"""


# Caltulateに関連する例外
# IsCalcEndに関連する例外
# CreateDocumentに関連する例外
# ExportInputCsvに関連する例外
# ExportResultCsvに関連する例外
# ExpotCad7に関連する例外
# Startに関連する例外


class Ss7Data:
    def GetInputData(self):
        pass

    def GetResultData(self, param1):
        pass

    def Save(self):
        pass

    def Close(self, param1):
        pass

    def Restore(self, param1):
        pass

    def DeleteResult(self, param1):
        pass

    def Calculate(self, param1, param2):
        pass

    def IsCalcEnd(self, param1, param2):
        pass

    def GetPathName(self):
        pass


class Ss7Input:
    def ExportInputCsv(self, param1, param2, param3):
        pass


class Ss7Result:
    def CreateDocument(self, param1, param2, param3):
        pass

    def ExportInputCsv(self, param1, param2, param3):
        pass

    def ExportResultCsv(self, param1, param2, param3, param4, param5):
        pass

    def ExportCad7(self, param1, param2, param3):
        pass


def Init() -> None:
    Ss7.Init()


class Version(Enum):
    LATEST = None
    V1_1_1_19 = "1.1.1.19"


class ClearLog(Enum):
    CLEAR = 1
    NOT_CLEAR = 2


# Exceptionを定義しないと。


def Start(version: Version = Version.LATEST, clear_log: ClearLog = ClearLog.CLEAR):
    try:
        Ss7.Start(version.value, clear_log.value)

    except Exception as e:
        err = Ss7.GetLastError()

        no: int = err.GetErrorNo()
        if no == 101:
            raise CommonException.LicenseMissingError(err)
        elif no == 102:
            raise CommonException.AlreadyRunningError()
        elif no == 107:
            raise CommonException.LicenseExpiredError(err)
        else:
            raise e


def End(param1):
    pass


def LinkSS3(param1, param2, param3, param4):
    pass


def CreateDataCsv(param1, param2, param3):
    pass


def Open(param1, param2, param3):
    pass


def GetLastError():
    pass


def GetInfoVersion(param1):
    pass


def GetInfoFloor(param1):
    pass


def GetInfoSpanX(param1):
    pass


def GetInfoSpanY(param1):
    pass


def GetInfoKozoRC(param1):
    pass


def GetInfoKozoSRC(param1):
    pass


def GetInfoKozoS(param1):
    pass
