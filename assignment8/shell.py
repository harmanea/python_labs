from abc import ABC, abstractmethod
import datetime


class Command(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def help(self) -> str:
        pass

    @abstractmethod
    def execute(self, *args):
        pass


class Exit(Command, ABC):
    def name(self) -> str:
        return 'exit'

    def help(self) -> str:
        return 'usage: exit\nExits the shell.'

    def execute(self, *args):
        print('Goodbye!')
        exit(0)


class Date(Command, ABC):
    def name(self) -> str:
        return 'date'

    def help(self) -> str:
        return 'usage: date\nPrints the current date.'

    def execute(self, *args):
        print(datetime.datetime.now())


class Sum(Command, ABC):
    def name(self) -> str:
        return 'sum'

    def help(self) -> str:
        return 'usage: sum a b [c]*\nPrints a sum of the given int arguments.'

    def execute(self, *args):
        try:
            result = 0
            for arg in args:
                result += int(arg)
            print(result)
        except ValueError as error:
            print(error)


if __name__ == '__main__':

    commands = [Exit(), Date(), Sum()]

    print('Welcome to the interactive shell!')
    print('Type "help" for a list of available commands.')
    print('Type "help command_name" for info on how to use that command.')

    while True:
        line = input()
        tokens = line.split()

        if tokens[0] == 'help':
            if len(tokens) == 1:
                for command in commands:
                    print(command.name())
            elif len(tokens) == 2:
                for command in commands:
                    if tokens[1] == command.name():
                        print(command.help())
                        break
                else:
                    print('Invalid command!')
                    print('Type "help" for a list of available commands.')
            else:
                print('Invalid use of the help command!')

        else:
            for command in commands:
                if tokens[0] == command.name():
                    command.execute(*tokens[1:])
                    break
            else:
                print('Invalid command!')
                print('Type "help" for a list of available commands.')
