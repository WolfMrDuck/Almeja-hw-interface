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

        :return The ADC value (0-65535)
        """
        return self.adc.read_u16()

    def read_voltage(self):
        """
        Computes the voltage corresponding to the raw ADC value

        :return The Voltage in millivolts.
        """
        #TODO This value will need some tuning and also some configurable parameters
        voltage = int(self.adc.read_uv() / 1000) - 21
        return voltage
