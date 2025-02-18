from machine import ADC,Pin

class Sensor:
    def __init__(self, pin_number):
        """
        Initialize the ADC sensor.
        
        :param pin_number: The GPIO pin number to which the sensor is connected.
        """
        self.adc = ADC(Pin(pin_number))
        self.adc.width(ADC.WIDTH_12BIT)
        self.adc.atten(ADC.ATTN_0DB)

    def raw_read(self):
        """
        Read the raw ADC value

        :return The ADC value (0-4095 for the 12 bit resolution)
        """
        return self.adc.read()

    def read_voltage(self):
        """
        Computes the voltage corresponding to the raw ADC value

        :return The Voltage in volts.
        """
        raw_value = self.raw_read()
        #TODO This value will need some tuning
        voltage = raw_value * (3.3/4095)
        return voltage
