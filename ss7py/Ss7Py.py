from enum import Enum, Flag, auto
from Ssp import Ss7Python as Ss7
import CommonException


class Version(Enum):
    LATEST = None
    V1_1_1_19 = "1.1.1.19"


class ClearLog(Enum):
    CLEAR = 1
    NOT_CLEAR = 2


class PrintMember(Enum):
    ALL = 1
    REPRESENTATIVE = 2


class Results(Enum):
    RESULT_1 = "結果1"
    RESULT_2 = "結果2"
    RESULT_3 = "結果3"
    RESULT_4 = "結果4"
    RESULT_5 = "結果5"


class Save(Enum):
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
    def __init__(self, data):
        self.data = data

    def GetInputData(self):
        pass

    def GetResultData(self, param1):
        data = self.data.GetResultData(param1)
        return Ss7Result(data)

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
    """Ss7Python全体の初期化を行う。"""
    Ss7.Init()


# Exceptionを定義しないと。


class Ss7Py:
    @staticmethod
    def Start(version: Version = Version.LATEST, clear_log: ClearLog = ClearLog.CLEAR):
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
    def End(save: Save = Save.WITHOUT_SAVE):
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
    def Open(param1, param2, param3) -> Ss7Data:
        result = Ss7.Open(param1, param2, param3)
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
