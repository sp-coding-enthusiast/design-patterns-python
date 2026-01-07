class Target:
    """Target interface expected by the client."""

    def request(self) -> str:
        """Return a string representing the standard request."""
        raise NotImplementedError()
