from plugin import ThrowExceptionExample
from tuneflow_devkit import Debugger

if __name__ == "__main__":
    Debugger(plugin_class=ThrowExceptionExample).start()