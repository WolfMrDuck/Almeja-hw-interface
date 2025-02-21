from machine import ADC,Pin

class Sensor:
    def __init__(self, pin_number, calibration_factor=1.0,
                 attenuation=ADC.ATTN_0DB, resolution=ADC.WIDTH_12BIT):
        """
        Initialize the ADC sensor.
        
        :param pin_number: The GPIO pin number to which the sensor is connected.
        :param calibration_factor: The factor to calibrate the reading
        """
        self.adc = ADC(pin=Pin(pin_number), atten=attenuation)
        self.adc.block().init(bits=ADC.WIDTH_12BIT)
        self.calibration_factor = calibration_factor

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

    def read(self):
        """
        Computes a calibrated voltage

        :return calibrated voltage
        """
        return self.read_voltage() * self.calibration_factor
