from .adaptee import Adaptee
from .target import Target


class Adapter(Target):
    """Adapter makes Adaptee's interface compatible with Target."""

    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self) -> str:
        # Translate the adaptee's specific_request to the Target.request format
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()}"
