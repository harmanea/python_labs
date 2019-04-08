import sys
import datetime


class Logger:
    def __init__(self, name: str):
        self.name = name
        self.level = 0
        self.printers = []

    def set_level(self, level: int):
        self.level = level

    def log(self, level: int, message: str):
        if level > self.level:
            for printer in self.printers:
                printer.print(message, self)

    def add_printer(self, printer):
        self.printers.append(printer)


class Printer:
    def __init__(self, fun=lambda msg: print(msg), formatter=None):
        self.fun = fun
        self.formatter = formatter

    def print(self, msg, logger):
        if self.formatter is None:
            self.fun(msg)
        else:
            self.fun(self.formatter.format(logger, msg))


class Formatter:
    def __init__(self, fun):
        self.fun = fun

    def format(self, logger, message):
        return self.fun(logger, message)


if __name__ == '__main__':  # test the implementation
    # Get a logger
    logger = Logger('My Logger')

    # And a couple printers
    printer = Printer(lambda msg: print(msg))
    err_printer = Printer(lambda msg: print(msg, file=sys.stderr))

    logger.add_printer(printer)
    logger.add_printer(err_printer)
    logger.set_level(3)

    # Try logging with different levels
    logger.log(5, 'This is a message')
    logger.log(2, 'Level is too low')  # this shouldn't be printed

    logger.set_level(1)
    logger.log(2, 'now it\'s okay') # this should now be printed

    # Now with formatters
    formatter = Formatter(lambda logger, msg: f'{logger.name}: {msg}')
    now_formatter = Formatter(lambda logger, msg: f'{datetime.datetime.now()}: {msg}')

    # Try the formatters
    print(formatter.format(logger, 'A cool msg'))
    print(now_formatter.format(logger, 'Another cool msg'))

    # Get a fresh new logger
    logger = Logger('Logger with formatters')

    # Simple printers with the new formatters
    printer = Printer(formatter=formatter)
    other_printer = Printer(formatter=now_formatter)

    logger.add_printer(printer)
    logger.add_printer(other_printer)

    # Try it out
    logger.log(2, 'Message with formatters')
    logger.log(4, 'Another message')
