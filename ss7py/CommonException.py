import Ss7PyException

# 共通エラー


class LicenseMissingError(Ss7PyException):
    """SS7またはOp.Python実行のライセンスを取得していません。"""


class AlreadyRunningError(Ss7PyException):
    """すでに他のSS7またはOp.Python実行が実行中です。"""


class LicenseExpiredError(Ss7PyException):
    """SS7・Op.Python実行・または関連するライセンスの保持期限が切れました。"""
