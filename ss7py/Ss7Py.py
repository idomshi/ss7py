from enum import Enum, Flag, auto

from Ssp import Ss7Python as Ss7
from . import CommonException
from . import OpenException
from . import CreateDataCsvException
from .ErrInfo import ErrInfo


class Version(Enum):
    """処理中に使うSS7のバージョン"""

    LATEST = None
    V1_1_1_19 = "1.1.1.19"


class ClearLog(Enum):
    """処理開始時にログファイルをリセットするか追記するか"""

    CLEAR = 1
    NOT_CLEAR = 2


class OmitSymbol(Enum):
    """結果出力時に数値に記号を付加するか"""

    OMIT = 1
    PRINT = 2


class PrintMember(Enum):
    """全部材を出力するか代表部材のみ出力するか"""

    ALL = 1
    REPRESENTATIVE = 2


class Results(Enum):
    """解析結果のスロット番号"""

    RESULT_1 = "結果1"
    RESULT_2 = "結果2"
    RESULT_3 = "結果3"
    RESULT_4 = "結果4"
    RESULT_5 = "結果5"


class SaveChange(Enum):
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


class Ss7Input:
    def __init__(self, input) -> None:
        self.data = input

    def ExportInputCsv(
        self, csv_path: str, overwrite: Overwrite, symbol_duplicate: SymbolDuplicate
    ) -> None:
        self.data.ExportInputCsv(csv_path, overwrite, symbol_duplicate)


class Ss7Result:
    def __init__(self, result) -> None:
        self.data = result

    def CreateDocument(
        self, document_type: DocumentType, document_name: str, overwrite: Overwrite
    ) -> None:
        # DocumentTypeを整数に変換する。
        doc_type: int = 0
        if DocumentType.構造計算書 in document_type:
            doc_type = doc_type * 10 + 1
        if DocumentType.入力データ出力 in document_type:
            doc_type = doc_type * 10 + 2
        if DocumentType.結果出力添付資料 in document_type:
            doc_type = doc_type * 10 + 3
        if DocumentType.積算 in document_type:
            doc_type = doc_type * 10 + 4

        self.data.CreateDocument(doc_type, document_name, overwrite)

    def ExportInputCsv(
        self, csv_path: str, overwrite: Overwrite, symbol_duplicate: SymbolDuplicate
    ) -> None:
        self.data.ExportInputCsv(csv_path, overwrite.value, symbol_duplicate.value)

    def ExportResultCsv(
        self,
        export_item: str,
        csv_path: str,
        overwrite: Overwrite,
        omit_symbol: OmitSymbol,
        print_member: PrintMember,
    ) -> None:
        """export_item == ""とすると全ての項目を出力する。"""

        # item == Noneですべての項目を出力する。
        item = None if export_item == "" else export_item

        self.data.ExportResultCsv(
            item, csv_path, overwrite.value, omit_symbol.value, print_member.value
        )

    def ExportCad7(self, cad7_path: str, overwrite: Overwrite) -> None:
        self.data.ExportCad7(cad7_path, overwrite)


class Ss7Data:
    def __init__(self, data) -> None:
        self.data = data

    def GetInputData(self) -> Ss7Input:
        input = self.data.GetInputData()
        return Ss7Input(input)

    def GetResultData(self, result_number: Results) -> Ss7Result:
        data = self.data.GetResultData(result_number.value)
        return Ss7Result(data)

    def Save(self) -> None:
        self.data.Save()

    def Close(self, save: SaveChange) -> None:
        self.data.Close(save.value)

    def Restore(self, result_number: Results) -> None:
        self.data.Restore(result_number)

    def DeleteResult(self, result_number: Results) -> None:
        self.data.DeleteResult(result_number)

    def Calculate(self, result_number: Results, calculation_item: str = "") -> None:
        """モデルの解析を行う。

        parameter
        ---------
        result_number: Results
            解析結果のスロット番号。
        calculation_item: str = ""
            解析項目を";"でつなげた文字列。何も指定しないと全て解析する。
        """

        # 第二引数の扱い：
        # ok: self.data.Calculate(result_number.value, "")
        # ok: self.data.Calculate(result_number.value)
        # ng: self.data.Calculate(result_number.value, None)
        self.data.Calculate(result_number.value, "")

    def IsCalcEnd(self, result_number: Results, calculation_item: str) -> bool:
        result = self.data.IsCalcEnd(result_number.value, calculation_item)
        return result

    def GetPathName(self) -> str:
        path = self.data.GetPathName()
        return path


def Init() -> None:
    """Ss7Python全体の初期化を行う。"""
    # Ss7.Init()
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
            raise CommonException.AlreadyRunningError(err)
        elif no == 107:
            raise CommonException.LicenseExpiredError(err)

    @staticmethod
    def End(save: SaveChange = SaveChange.WITHOUT_SAVE) -> None:
        Ss7.End(save.value)

    @staticmethod
    def LinkSS3(
        ss3path: str,
        ss7path: str,
        overwrite: Overwrite,
        link_limitstrength: LinkLimitStrengthModel,
    ) -> str:
        path = Ss7.LinkSS3(ss3path, ss7path, overwrite.value, link_limitstrength.value)
        return path

    @staticmethod
    def CreateDataCsv(
        csv_path: str, ss7_path: str, overwrite: CreateDataCsvOverwrite
    ) -> str:
        result: str = Ss7.CreateDataCsv(csv_path, ss7_path, overwrite.value)

        if result == "":
            err = Ss7.GetLastError()
            no: int = err.GetErrorNo()

            if no == 101:
                raise CommonException.LicenseMissingError(err)
            elif no == 102:
                raise CommonException.AlreadyRunningError(err)
            elif no == 107:
                raise CommonException.LicenseExpiredError(err)
            elif no == 1:
                raise CreateDataCsvException.CsvFileNotFoundError(err)
            elif no == 2:
                raise CreateDataCsvException.InvalidCsvFileError(err)
            elif no == 3:
                raise CreateDataCsvException.InvalidCsvDataError(err)
            elif no == 4:
                raise CreateDataCsvException.FileCannotOpenError(err)
            elif no == 5:
                raise CreateDataCsvException.CannotReadBasicInformationError(err)
            elif no == 6:
                raise CreateDataCsvException.StructureTypeRestrictedError(err)
            elif no == 7:
                raise CreateDataCsvException.FloorNumberRestrictedError(err)
            elif no == 8:
                raise CreateDataCsvException.InvalidPathError(err)
            elif no == 9:
                raise CreateDataCsvException.FileLockError(err)
            elif no == 10:
                raise CreateDataCsvException.FileExistsError(err)
            elif no == 11:
                raise CreateDataCsvException.FileWriteAccessError(err)
            elif no == 12:
                raise CreateDataCsvException.UnknownCreateModelError(err)
            elif no == 15:
                raise CreateDataCsvException.WoodStructureLicenseMissingError(err)
            elif no == 16:
                raise CreateDataCsvException.IsolationStructureLicenseMissingError(err)
            elif no == 18:
                raise CreateDataCsvException.InputCsvContainedError(err)
            elif no == 19:
                raise CreateDataCsvException.VersionUnmatchedError(err)
            elif no == 20:
                raise CreateDataCsvException.PremiumLicenseMissingError(err)
            else:
                raise Exception()

        else:
            return result

    @staticmethod
    def Open(path: str, convert: ConvertModel, backupdata: BackupData) -> Ss7Data:
        result = Ss7.Open(path, convert.value, backupdata.value)

        if result == None:
            err = Ss7.GetLastError()
            no: int = err.GetErrorNo()

            if no == 101:
                raise CommonException.LicenseMissingError(err)
            elif no == 102:
                raise CommonException.AlreadyRunningError(err)
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
                raise Exception()

        else:
            return Ss7Data(result)

    @staticmethod
    def GetLastError() -> ErrInfo:
        err = Ss7.GetLastError()
        return ErrInfo(err)

    @staticmethod
    def GetInfoVersion(ss7_path: str) -> str:
        """物件データのバージョン番号を'Ver.1.2.3.4'の形式で取得する。"""
        # バージョン番号を文字列で返したい。
        version: int = Ss7.GetInfoVersion(ss7_path)
        s = str(version)

        # なんかもうちょっとスマートに書けそうだけど仕方あるまい。
        verstr = "Ver." + ".".join(
            map(
                str,
                map(
                    int,
                    [
                        s[:-7],
                        s[-7:-5],
                        s[-5:-3],
                        s[-3:],
                    ],
                ),
            )
        )
        return verstr

    @staticmethod
    def GetInfoFloor(ss7_path: str) -> int:
        """物件データの全階数を取得する。"""
        floor = Ss7.GetInfoFloor(ss7_path)
        return floor

    @staticmethod
    def GetInfoSpanX(ss7_path: str) -> int:
        """物件データのX方向スパン数を取得する。"""
        span = Ss7.GetInfoSpanX(ss7_path)
        return span

    @staticmethod
    def GetInfoSpanY(ss7_path: str) -> int:
        """物件データのY方向スパン数を取得する。"""
        span = Ss7.GetInfoSpanX(ss7_path)
        return span

    @staticmethod
    def GetInfoKozoRC(ss7_path: str) -> int:
        """
        物件データの主体構造を取得しRCが含まれるかを返す。

        Returns
        -------
        int
            0: RCは含まれない / 1: RCが含まれる
        """

        # boolで返したほうが良いのか？ GetInfoKozoSの返り値がtri-stateだから統一するためにintのままが良いのか？
        result = Ss7.GetInfoKozoRC(ss7_path)
        return result

    @staticmethod
    def GetInfoKozoSRC(ss7_path: str) -> int:
        """
        物件データの主体構造を取得しSRCが含まれるかを返す。

        Returns
        -------
        int
            0: SRCは含まれない / 1: SRCが含まれる
        """

        # boolで返したほうが良いのか？ GetInfoKozoSの返り値がtri-stateだから統一するためにintのままが良いのか？
        result = Ss7.GetInfoKozoSRC(ss7_path)
        return result

    @staticmethod
    def GetInfoKozoS(ss7_path: str) -> int:
        """
        物件データの主体構造を取得しSまたはCFTが含まれるかを返す。

        Returns
        -------
        int
            0: Sは含まれない / 1: Sが含まれる / 2: CFTが含まれる
        """

        # SとCFTが両方含まれるときはどうなるんだ？ あとでテストしないと。

        # この関数はこの関数として。
        # GetKozoInfo関数を新しく作って、
        # { RC: bool, SRC: bool, S: bool, CFT: bool }
        # みたいな形式で返したほうが幸せになれるのでは。
        result = Ss7.GetInfoKozoS(ss7_path)
        return result
