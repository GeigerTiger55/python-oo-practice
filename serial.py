class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial number generator starting number from "start"."""
        self.start = start
        self.last_serial = start-1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} last_serial={self.last_serial}>"

    def generate(self):
        """Increases last_serial and returns last_serial """
        self.last_serial += 1
        return self.last_serial

    def reset(self):
        """Sets last_serial to one less than start number """
        self.last_serial = self.start-1


        