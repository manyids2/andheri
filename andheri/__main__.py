import sys
import inspect
import importlib
from rich.prompt import Prompt
from rich import print


class Structure:
    @classmethod
    def from_prompt(cls):
        name = Prompt.ask("Enter module name")
        return cls(name)

    def __init__(self, name: str):
        lib = importlib.import_module(name)
        self.lib = lib
        self.doc = inspect.getdoc(lib)
        self.file = inspect.getfile(lib)

        self.builtins = {}
        self.classes = {}
        self.modules = {}
        self.functions = {}
        self.dunders = {}
        self.privates = {}
        for k, v in vars(lib).items():
            # Dont add builtins to our list
            if inspect.isbuiltin(v):
                self.builtins[k] = v
                continue

            # Same with dunders and privates
            if k == "__builtins__":
                continue

            if k.startswith("__") & k.endswith("__"):
                self.dunders[k] = v
                continue

            elif k.startswith("_"):
                self.privates[k] = v
                continue

            if inspect.ismodule(v):
                self.modules[k] = v

            if inspect.isclass(v):
                self.classes[k] = v

            if inspect.isfunction(v):
                self.functions[k] = v

    def print(self) -> None:
        print(f"modules ->\n{list(self.modules.keys())}\n")
        for k, v in self.modules.items():
            print(f"{k} -> {v}")

        print()

        print(f"classes ->\n{list(self.classes.keys())}\n")
        for k, v in self.classes.items():
            print(f"{k} -> {inspect.signature(v.__init__)}")
            print()

        print()

        print(f"functions ->\n{list(self.functions.keys())}\n")
        for k, v in self.functions.items():
            print(f"{k} -> {inspect.signature(v)}")
            print()

        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        ss = Structure(name)
    else:
        ss = Structure.from_prompt()

    ss.print()
