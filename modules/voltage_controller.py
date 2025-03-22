from machine import PWM, Pin

class VoltageController:
    def __init__(self, pin_number, duty_cycle=128, freq=5000):
        """
        Initialize the PWM controller

        :param int pin_number: The GPIO pin number to which the sensor is connected.
        :param int duty_cycle: The duty cycle at the start, can be 0-1023.
        :param int freq: The frequency in Hz at the start, at most 40Mhz.
        """
        self.pwm = PWM(Pin(pin_number), freq=freq, duty=duty_cycle)
        self.duty_cycle = duty_cycle / 10.23

    def set_duty_cycle(self, duty_cycle: int):
        """
        Changes the duty cycle

        :param int duty_cycle: A percentage of duty in each cycle, can be from 0 to 100
        """
        if 0 <= duty_cycle <= 100:
            self.duty_cycle = duty_cycle
            new_duty_cycle = int(duty_cycle * 10.23)
            self.pwm.duty(new_duty_cycle)
