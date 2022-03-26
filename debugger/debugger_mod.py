class _Color:
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    GREEN   = "\033[92m"
    CYAN    = "\033[96m"
    BLUE    = "\033[94m"
    PURPLE  = "\033[95m"
    END     = "\033[0m"

class Debugger:
    _debug: bool
    def __init__(self, set_active: bool=False, name: str="") -> None:
        """Constructor

        Parameters
        ----------
        set_active : bool, optional
            Whether debug statements should be printed, by default False
        name : str, optional
            The name to be associated with the debugger, if left empty no name will be printed
        """
        self._debug = set_active
        self._name = name

        if set_active:
            self.debug("DEBUGGING ENABLED")


    def _print(self, color: _Color, string: str):
        print(f"{f'[{self._name}] ' if self._name else ''}{color}{string}{_Color.END}", flush=True)

    def ok(self, string: str):
        self._print(_Color.GREEN, string)

    def debug(self, string: str):
        if self._debug:
            self._print(_Color.PURPLE, string)

    def info(self, string: str):
        self._print(_Color.CYAN, string)

    def warn(self, string: str):
        self._print(_Color.YELLOW, string)

    def err(self, string: str):
        self._print(_Color.RED, string)

    def printf(self, string: str):
        self._print(_Color.END, string)

D = Debugger(False)

def ok(string: str):
    D.ok(string)
def info(string: str):
    D.info(string)
def warn(string: str):
    D.warn(string)
def err(string: str):
    D.err(string)
def printf(string: str):
    D.printf(string)

if __name__ == "__main__":
    d = Debugger(True, "main")
    d.printf("printf")
    d.debug("debug")
    d.info("info")
    d.warn("warn")
    d.err("err")