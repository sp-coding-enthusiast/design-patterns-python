from adapter_example.adaptee import Adaptee
from adapter_example.adapter import Adapter


def test_adapter_translates() -> None:
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    result = adapter.request()
    assert "Adaptee: Specific behavior." in result
