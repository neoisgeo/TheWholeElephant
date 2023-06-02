from enum import Enum, auto
from termcolor import colored
from typing import Callable


class LogMessageType(Enum):
    info = auto()
    data = auto()
    user = auto()
    assistant = auto()
    warning = auto()


LogFn = Callable[[str, LogMessageType], None]


def simple_print(message: str, _: LogMessageType):
    print(message)


def print_color(message: str, log_message_type: LogMessageType):
    match log_message_type:
        case LogMessageType.info:
            color = "blue"
        case LogMessageType.data:
            color = "yellow"
        case LogMessageType.user:
            color = "cyan"
        case LogMessageType.assistant:
            color = "magenta"
        case LogMessageType.warning:
            color = "red"
        case _:
            color = "white"
    print(colored(str(message), color))
