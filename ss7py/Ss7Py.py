from enum import Enum, Flag, auto
from Ssp import Ss7Python as Ss7
import CommonException
import OpenException


class Version(Enum):
    """処理中に使うSS7のバージョン"""

    LATEST = None
    V1_1_1_19 = "1.1.1.19"


class ClearLog(Enum):
    """処理開始時にログファイルをリセットするか追記するか"""

    CLEAR = 1
    NOT_CLEAR = 2


class PrintMember(Enum):
    ALL = 1
    REPRESENTATIVE = 2


class Results(Enum):
    """解析結果のスロット番号"""

    RESULT_1 = "結果1"
    RESULT_2 = "結果2"
    RESULT_3 = "結果3"
    RESULT_4 = "結果4"
    RESULT_5 = "結果5"


class Save(Enum):
    """物件データの変更を保存するか破棄するか"""

    SAVE = 1
    WITHOUT_SAVE = 2


class Overwrite(Enum):
    OVERWRITE = 1
    INTERRUPT = 2
    SAVE_NEWNAME = 3


class SymbolDuplicate(Enum):
    CONTINUE = 1
    INTERRUPT = 2


class DocumentType(Flag):
    構造計算書 = auto()
    入力データ出力 = auto()
    結果出力添付資料 = auto()
    積算 = auto()


class CreateDataCsvOverwrite(Enum):
    CLEAR_AND_OVERWRITE = 1
    INTERRUPT = 2
    SAVE_NEWNAME = 3
    RESERVE_AND_OVERWRITE = 4


class ConvertModel(Enum):
    CONVERT = 1
    COPY = 2
    INTERRUPT = 3


class BackupData(Enum):
    """物件データにバックアップデータが存在した場合の動作"""

    SAVEAS = 1
    DELETE = 2
    INTERRUPT = 3


class LinkLimitStrengthModel(Enum):
    LINK = 1
    NOT_LINK = 2


# IsCalcEndに関連する例外
# CreateDocumentに関連する例外
# ExportInputCsvに関連する例外
# ExportResultCsvに関連する例外
# ExpotCad7に関連する例外
# Startに関連する例外


class Ss7Data:
    def __init__(self, data) -> None:
        self.data = data

    def GetInputData(self) -> Ss7Input:
        input = self.data.GetInputData()
        return Ss7Input(input)

    def GetResultData(self, result_number: Results) -> Ss7Result:
        data = self.data.GetResultData(result_number)
        return Ss7Result(data)

    def Save(self) -> None:
        self.data.Save()

    def Close(self, save: Save) -> None:
        self.data.Close(save)

    def Restore(self, result_number: Results) -> None:
        self.data.Restore(result_number)

    def DeleteResult(self, result_number: Results) -> None:
        self.data.DeleteResult(result_number)

    def Calculate(self, result_number: Results, calculation_item: str) -> None:
        self.data.Calculate(result_number, calculation_item)

    def IsCalcEnd(self, result_number: Results, calculation_item: str) -> bool:
        result = self.data.IsCalcEnd(result_number, calculation_item)
        return result

    def GetPathName(self) -> str:
        path = self.data.GetPathName()
        return path


class Ss7Input:
    def ExportInputCsv(self, param1, param2, param3):
        pass


class Ss7Result:
    def __init__(self, result) -> None:
        self.data = result

    def CreateDocument(self, param1, param2, param3):
        pass

    def ExportInputCsv(
        self, csv_path: str, overwrite: Overwrite, symbol_duplicate: SymbolDuplicate
    ) -> None:
        self.data.ExportInputCsv(csv_path, overwrite, symbol_duplicate)

    def ExportResultCsv(self, param1, param2, param3, param4, param5):
        pass

    def ExportCad7(self, param1, param2, param3):
        pass


def Init() -> None:
    """Ss7Python全体の初期化を行う。"""
    Ss7.Init()


# Exceptionを定義しないと。


class Ss7Py:
    @staticmethod
    def Start(
        version: Version = Version.LATEST, clear_log: ClearLog = ClearLog.CLEAR
    ) -> None:
        Ss7.Start(version.value, clear_log.value)
        err = Ss7.GetLastError()
        no: int = err.GetErrorNo()

        if no == 101:
            raise CommonException.LicenseMissingError(err)
        elif no == 102:
            raise CommonException.AlreadyRunningError()
        elif no == 107:
            raise CommonException.LicenseExpiredError(err)

    @staticmethod
    def End(save: Save = Save.WITHOUT_SAVE) -> None:
        Ss7.End(save.value)

    @staticmethod
    def LinkSS3(
        ss3path: str,
        ss7path: str,
        overwrite: Overwrite,
        link_limitstrength: LinkLimitStrengthModel,
    ) -> str:
        Ss7.LinkSS3(ss3path, ss7path, overwrite.value, link_limitstrength.value)

    @staticmethod
    def CreateDataCsv(param1, param2, param3):
        pass

    @staticmethod
    def Open(path: str, overwrite: Overwrite, backupdata: BackupData) -> Ss7Data:
        result = Ss7.Open(path, overwrite, backupdata)

        if result == None:
            err = Ss7.GetLastError()
            no: int = err.GetErrorNo()

            if no == 101:
                raise CommonException.LicenseMissingError(err)
            elif no == 102:
                raise CommonException.AlreadyRunningError()
            elif no == 107:
                raise CommonException.LicenseExpiredError(err)
            elif no == 1:
                raise OpenException.FileNotFoundError(err)
            elif no == 2:
                raise OpenException.FileAlreadyOpenedError(err)
            elif no == 3:
                raise OpenException.BackupDataExistsError(err)
            elif no == 4:
                raise OpenException.FileVersionLowerError(err)
            elif no == 5:
                raise OpenException.FileVersionUpperError(err)
            elif no == 6:
                raise OpenException.StructureTypeRestrictedError(err)
            elif no == 7:
                raise OpenException.FileWriteAccessError(err)
            elif no == 8:
                raise OpenException.FileCannotOpenError(err)
            elif no == 12:
                raise OpenException.WoodStructureLicenseMissingError(err)
            elif no == 13:
                raise OpenException.IsolationStructureLicenseMissingError(err)
            elif no == 15:
                raise OpenException.PremiumLicenseMissingError(err)

        else:
            return Ss7Data(result)

    @staticmethod
    def GetLastError():
        pass

    @staticmethod
    def GetInfoVersion(param1):
        pass

    @staticmethod
    def GetInfoFloor(param1):
        pass

    @staticmethod
    def GetInfoSpanX(param1):
        pass

    @staticmethod
    def GetInfoSpanY(param1):
        pass

    @staticmethod
    def GetInfoKozoRC(param1):
        pass

    @staticmethod
    def GetInfoKozoSRC(param1):
        pass

    @staticmethod
    def GetInfoKozoS(param1):
        pass
