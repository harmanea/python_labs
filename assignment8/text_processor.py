import abc
import sys


class TextProcessorPlugin(abc.ABC):
    @abc.abstractmethod
    def process(self, text: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def name() -> str:
        pass


class ToUpperPlugin(TextProcessorPlugin, abc.ABC):
    def process(self, text: str):
        return text.upper()

    @staticmethod
    def name() -> str:
        return 'ToUpperPlugin'


class ToLowerPlugin(TextProcessorPlugin, abc.ABC):
    def process(self, text: str):
        return text.lower()

    @staticmethod
    def name() -> str:
        return 'ToLowerPlugin'


class CapitalizePlugin(TextProcessorPlugin, abc.ABC):
    def process(self, text: str):
        return text.capitalize()

    @staticmethod
    def name() -> str:
        return 'CapitalizePlugin'


if __name__ == '__main__':
    plugins = []
    for arg in sys.argv[1:]:
        if arg == ToUpperPlugin.name():
            plugins.append(ToUpperPlugin())
        elif arg == ToLowerPlugin.name():
            plugins.append(ToLowerPlugin())
        elif arg == CapitalizePlugin.name():
            plugins.append(CapitalizePlugin())

    while True:
        text = input()
        for plugin in plugins:
            text = plugin.process(text)

        print(text)
