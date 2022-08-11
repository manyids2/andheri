# andheri

Introspection of codebase, ui powered by [rich](https://github.com/Textualize/rich).

TODO:

- [ ] loc
- [ ] file tree
- [ ] interfaces
- [ ] classes
- [ ] methods
- [ ] globals

## Installation

```sh
git clone https://github.com/manyids2/andheri.git
cd andheri
pip install -e .
```

## Documentation

From `andheri` root folder,

```sh
cd docs
make html
google-chrome-stable build/html/index.html
```

## Usage

As an example, we check whats up with the `PIL` library.
To make sure it is installed,

```
pip install Pillow
```

### Summary

```
andheri summary PIL
```

### Lines of code ( loc )

```
andheri loc PIL
```

### File tree

```
andheri filetree PIL
```

### Interfaces ( dataclasses )

```
andheri interfaces PIL
```

### Globals

```
andheri globals PIL
```

### Paths

```
andheri paths PIL
```

## Resources

- [this page](https://github.com/manyids2/andheri)
- [rich docs](https://rich.readthedocs.io/en/latest/index.html)
- [BBCode](https://en.wikipedia.org/wiki/BBCode)
