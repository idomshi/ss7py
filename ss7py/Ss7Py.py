from enum import Enum
from Ssp import Ss7Python as Ss7
import CommonException


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
