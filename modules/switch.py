from machine import Pin

class Switch:
    def __init__(self, pin_number: int):
        """
        Initialize the Switch
    
        :param int pin_number: The GPIO pin number to which the switch is connected.
        """
        self.pin = Pin(pin_number, Pin.OUT)
        if self.pin.value():
            self.state = True
        else:
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

class IndicatedSwitch(Switch):
    def __init__(self, switch_pin: int, switch_led: int):
        """
        Initialize the Switch with an indicator LED.
    
        :param int switch_pin: The GPIO pin number to which the switch is connected.
        :param int switch_led: The GPIO pin number to which the switch's led is connected.
        """
        super().__init__(switch_pin)
        self.led = Pin(switch_led, Pin.OUT)

    def on(self):
        """
        Turn the LED on.
        """
        super().on()
        self.led.value(1)

    def off(self):
        """
        Turn the LED off.
        """
        super().off()
        self.led.value(0)
