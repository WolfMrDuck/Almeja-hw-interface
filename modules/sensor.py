from machine import ADC, Pin

class Sensor:
    def __init__(self, pin_number: int, calibration_factor: float = 1.0,
                 offset: float = 0.0, threshold: float = 0.0,
                 attenuation=ADC.ATTN_0DB, resolution=ADC.WIDTH_12BIT):
        """
        Initialize the ADC sensor.
        
        :param int pin_number: The GPIO pin number to which the sensor is connected.
        :param float calibration_factor: The factor to calibrate the reading.
        :param float offset: The offset to calibrate the reading.
        :param float threshold: The threshold to ignore close to 0 values.
        :param attenuation: The ADC block attenuation.
        :param resolution: The ADC block resolution.
        """
        self.adc = ADC(Pin(pin_number), atten=attenuation)
        self.adc.block().init(bits=ADC.WIDTH_12BIT)
        self.calibration_factor = calibration_factor
        self.offset = offset
        self.threshold = threshold

    def raw_read(self) -> int:
        """
        Read the raw ADC value

        :return The ADC value (0-65535)
        """
        return self.adc.read_u16()

    def read_voltage(self) -> int:
        """
        Computes the voltage corresponding to the raw ADC value

        :return The Voltage in millivolts.
        """
        voltage = int(self.adc.read_uv() / 1000)
        return voltage

    def read(self) -> float:
        """
        Computes a calibrated voltage

        :return calibrated voltage
        """
        voltage = self.read_voltage()
        if voltage <= self.threshold:
            read = 0
        else:
            read = voltage * self.calibration_factor - self.offset
        return read
