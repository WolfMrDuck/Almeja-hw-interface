from machine import Pin

class Switch:
    def __init__(self, pin_number: int):
        """
        Initialize the Switch
    
        :param int pin_number: The GPIO pin number to which the switch is connected.
        """
        self.pin = Pin(pin_number, Pin.OUT)
        self.state = False

    def on(self):
        """
        Turn the switch on.
        """
        self.pin.value(1)
        self.state = True

    def off(self):
        """
        Turn the switch off.
        """
        self.pin.value(0)
        self.state = False
