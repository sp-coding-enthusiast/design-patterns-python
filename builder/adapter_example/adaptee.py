class Adaptee:
    """A class with an incompatible interface that we want to adapt."""

    def specific_request(self) -> str:
        """Behaves differently from `Target.request`.

        Returns a string that the adapter will translate.
        """
        return "Adaptee: Specific behavior."
