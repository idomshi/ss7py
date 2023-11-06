from .ss7py import *


def main():
    Init()

    try:
        Ss7Py.Start(Version.LATEST, ClearLog.CLEAR)

        data = Ss7Py.Open(
            "C:\\UsrData\\Ss7Data\\sample.ikn",
            Overwrite.SAVE_NEWNAME,
            SymbolDuplicate.INTERRUPT,
        )
        data.Calculate(Results.RESULT_1, "+必要保有水平耐力")

        res = data.GetResultData(Results.RESULT_1)
        res.ExportInputCsv(
            "C:\\UsrData\\Ss7Data\\sample_input.csv",
            Overwrite.SAVE_NEWNAME,
            SymbolDuplicate.INTERRUPT,
        )

        data.Close(Save.SAVE)

    except Exception as e:
        print(e)

    Ss7Py.End()


if __name__ == "__main__":
    main()
