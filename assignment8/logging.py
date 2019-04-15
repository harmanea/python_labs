import sys
import datetime
import abc
from enum import IntEnum


class Logger:
    def __init__(self, name: str):
        self.name = name
        self.level = Level.INFO
        self.printers = []

    def set_level(self, level: int):
        self.level = level

    def log(self, level: int, message: str):
        if level <= self.level:
            for printer in self.printers:
                printer.print(message, self)

    def add_printer(self, printer):
        self.printers.append(printer)


class Level(IntEnum):
    SEVERE = 1
    WARNING = 2
    INFO = 3
    FINE = 4
    FINER = 5
    FINEST = 6


class Printer(abc.ABC):
    @abc.abstractmethod
    def print(self, msg, logger):
        pass


class SimplePrinter(Printer, abc.ABC):
    def __init__(self, formatter=None):
        self.formatter = formatter

    def print(self, msg, logger):
        if self.formatter is None:
            print(msg)
        else:
            print(self.formatter.format(logger, msg))


class ErrorPrinter(Printer, abc.ABC):
    def __init__(self, formatter=None):
        self.formatter = formatter

    def print(self, msg, logger):
        if self.formatter is None:
            print(msg, file=sys.stderr)
        else:
            print(self.formatter.format(logger, msg), file=sys.stderr)


class Formatter(abc.ABC):
    @abc.abstractmethod
    def format(self, logger, message):
        pass


class NameFormatter(Formatter, abc.ABC):
    def format(self, logger, message):
        return f'{logger.name}: {message}'


class DateFormatter(Formatter, abc.ABC):
    def format(self, logger, message):
        return f'{datetime.datetime.now()}: {message}'


if __name__ == '__main__':  # test the implementation
    # Get a logger
    logger = Logger('My Logger')

    # And a couple printers
    printer = SimplePrinter()
    err_printer = ErrorPrinter()

    logger.add_printer(printer)
    logger.add_printer(err_printer)
    logger.set_level(Level.FINE)

    # Try logging with different levels
    logger.log(Level.INFO, 'This is a message')
    logger.log(Level.FINER, 'Level is too low')  # this shouldn't be printed

    logger.set_level(Level.FINEST)
    logger.log(Level.FINER, 'now it\'s okay') # this should now be printed

    # Now with formatters
    formatter = NameFormatter()
    now_formatter = DateFormatter()

    # Try the formatters
    print(formatter.format(logger, 'A cool msg'))
    print(now_formatter.format(logger, 'Another cool msg'))

    # Get a fresh new logger
    logger = Logger('Logger with formatters')

    # Simple printers with the new formatters
    printer = SimplePrinter(formatter=formatter)
    other_printer = SimplePrinter(formatter=now_formatter)

    logger.add_printer(printer)
    logger.add_printer(other_printer)

    # Try it out
    logger.log(Level.INFO, 'Message with formatters')
    logger.log(Level.INFO, 'Another message')
