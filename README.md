# Python Debugger Prototype

A small educational project exploring how a Python debugging workflow can be implemented with Python's runtime inspection facilities.

## Current implementation

The repository includes:

- `debugger.py` — a `PyDebugger` class with breakpoint storage, frame inspection, local-variable access, stack-trace retrieval, and an interactive debug loop.
- `example.py` — an example that exercises the debugger around a recursive factorial function and a handled `ValueError`.
- `index.html` and `main.js` — accompanying web-interface files.

## Run the Python example

Use Python 3:

```bash
python example.py
```

The debugger is an experimental learning project. Its execution-control behaviour should be tested carefully before relying on it; it is not intended to replace Python's built-in `pdb` or a production IDE debugger.

## Concepts explored

- Python stack frames and runtime inspection
- Breakpoint tracking
- Local-variable inspection
- Stack traces and exception handling
- Interactive debugging workflows

## Project status

Academic / experimental prototype. The repository does not currently include a formal automated test suite or a packaged release.
