class HostEntry:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def __str__(self):
        return f"HostEntry(name={self.name}, address={self.address})"
