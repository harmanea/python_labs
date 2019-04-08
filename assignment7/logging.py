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
    log = Logger('My Logger')

    printer = Printer(lambda msg: print(msg))
    err_printer = Printer(lambda msg: print(msg, file=sys.stderr))

    log.add_printer(printer)
    log.add_printer(err_printer)
    log.set_level(3)

    log.log(5, 'This is a message')
    log.log(2, 'Level is too low')

    log.set_level(1)

    log.log(2, 'now it\'s okay')

    formatter = Formatter(lambda logger, msg: f'{logger.name}: {msg}')
    now_formatter = Formatter(lambda logger, msg: f'{datetime.datetime.now()}: {msg}')

    print(formatter.format(log, 'A cool msg'))
    print(now_formatter.format(log, 'Another cool msg'))

    log = Logger('Logger with formatters')

    printer = Printer(lambda msg: print(msg), formatter)
    other_printer = Printer(lambda msg: print(msg), now_formatter)

    log.add_printer(printer)
    log.add_printer(other_printer)

    log.log(2, 'Message with formatters')
