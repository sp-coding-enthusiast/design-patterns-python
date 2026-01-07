# Adapter Pattern — Python Example

A minimal Python demonstration of the Adapter design pattern.

- Package: adapter_example
- Example runner: [examples/main.py](examples/main.py)
- Unit test: [tests/test_adapter.py](tests/test_adapter.py) (uses `pytest`)

Quick start (Windows PowerShell)

1. Run the example (ensure the project root is on `PYTHONPATH`):

```powershell
Set-Location -Path 'D:\Projects\BuilderDesignPattern'
#$env:PYTHONPATH needs to include the project root so Python can import the package
$env:PYTHONPATH = 'D:\Projects\BuilderDesignPattern'
python .\examples\main.py
```

Expected example output:

```
Client: I can work with objects that follow the Target interface:
Adapter: (TRANSLATED) Adaptee: Specific behavior.
```

2. Install test dependencies and run tests:

```powershell
Set-Location -Path 'D:\Projects\BuilderDesignPattern'
pip install -r requirements.txt
pytest -q
```

Project layout

- [adapter_example](adapter_example) — package containing `Target`, `Adaptee`, and `Adapter`.
- [examples/main.py](examples/main.py) — small runner showing the pattern.
- [tests/test_adapter.py](tests/test_adapter.py) — unit test for the adapter.
- [requirements.txt](requirements.txt) — test dependency list.


