import sys


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
                printer.print(message)

    def add_printer(self, printer):
        self.printers.append(printer)


class Printer:
    def __init__(self, fun):
        self.fun = fun

    def print(self, msg):
        self.fun(msg)


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
