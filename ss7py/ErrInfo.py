class ErrInfo:
    def __init__(self, err):
        self.err = err

    def IsOK(self):
        pass

    def GetErrorNo(self) -> int:
        err_no = self.err.GetErrorNo()
        return err_no

    def GetErrorMessage(self) -> str:
        msg = self.err.GetErrorMessage()
        return msg
