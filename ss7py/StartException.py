import Ss7PyException


# Startに関連する例外
class Ss7VersionNotFoundError(Ss7PyException):
    """指定されたバージョンがインストールされていない場合に発生する例外"""


class Ss7VersionUnsupportedError(Ss7PyException):
    """Op.Python実行をサポートしていないバージョンが指定された場合に発生する例外"""


class Ss7NotStartedError(Ss7PyException):
    """Startコマンドが呼び出される前に他のコマンドを呼び出した場合に発生する例外"""


class Ss7VersionCannotChangeError(Ss7PyException):
    """一連のスクリプトの中で異なるバージョンを指定して複数回Startコマンドを呼び出した場合に発生する例外"""


class DifferentSs7VersionError(Ss7PyException):
    """1つのソースファイル内で2つ以上のバージョンを指定してStartコマンドを呼び出した場合に発生する例外"""


class AlreadyStartedError(Ss7PyException):
    """Endコマンドを呼ぶ前に複数回Startコマンドを呼び出した場合に発生する例外"""
