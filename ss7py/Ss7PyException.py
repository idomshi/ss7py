from .ErrInfo import ErrInfo


# 共通のSs7PyExceptionを作って継承すればいいのかもしれない。
class Ss7PyException(Exception):
    def __init__(self, error_info: ErrInfo):
        self._err_no = error_info.GetErrorNo()
        self._err_msg = error_info.GetErrorMessage()

    def __str__(self) -> str:
        # type(self).__name__で派生先のクラス名が拾える。
        return f"{type(self).__name__} ({self._err_no}): {self._err_msg}"
