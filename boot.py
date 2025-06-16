from modules import Sensor, Switch, IndicatedSwitch, VoltageController
from machine import ADC
import json

config_file = open("config.json",'r')
cfg = json.load(config_file)

voltmeters = {
        "solar": Sensor(pin_number=cfg['pin']['solar_vm'],
                        calibration_factor=cfg['factor']['solar'],
                        offset=cfg['offset']['solar'],
                        threshold=cfg['threshold']['solar']),
        "wind": Sensor(pin_number=cfg['pin']['wind_vm'],
                        calibration_factor=cfg['factor']['wind'],
                        offset=cfg['offset']['wind'],
                        threshold=cfg['threshold']['wind']),
        "batt": Sensor(pin_number=cfg['pin']['batt_vm'],
                        calibration_factor=cfg['factor']['batt_vm'],
                        offset=cfg['offset']['batt_vm'],
                        threshold=cfg['threshold']['batt_vm'])
        }

ammeters = {
        "source": Sensor(pin_number=cfg['pin']['source'],
                        calibration_factor=cfg['factor']['source'],
                         attenuation=ADC.ATTN_11DB,
                        offset=cfg['offset']['source'],
                        threshold=cfg['threshold']['source']),
        "batt": Sensor(pin_number=cfg['pin']['batt_amm'],
                        calibration_factor=cfg['factor']['batt_amm'],
                         attenuation=ADC.ATTN_11DB,
                        offset=cfg['offset']['batt_amm'],
                        threshold=cfg['threshold']['batt_amm'])
        }

thermometers = {
        "therm1": Sensor(pin_number=cfg['pin']['batt_temp1'],
                        calibration_factor=cfg['factor']['batt_temp1'],
                        offset=cfg['offset']['batt_temp1'],
                        threshold=cfg['threshold']['batt_temp1']),
        "therm2": Sensor(pin_number=cfg['pin']['batt_temp2'],
                        calibration_factor=cfg['factor']['batt_temp2'],
                        offset=cfg['offset']['batt_temp2'],
                        threshold=cfg['threshold']['batt_temp2']),
        "therm3": Sensor(pin_number=cfg['pin']['batt_temp3'],
                        calibration_factor=cfg['factor']['batt_temp3'],
                        offset=cfg['offset']['batt_temp3'],
                        threshold=cfg['threshold']['batt_temp3'])
        }
controllers = {
        "solar": VoltageController(pin_number=cfg['pin']['solar_vctr'],
                                   freq=cfg['core']['pwm_freq']),
        "wind": VoltageController(pin_number=cfg['pin']['wind_vctr'],
                                  freq=cfg['core']['pwm_freq'])
        }


load = Switch(pin_number=cfg['pin']['load_sw'])
vca = Switch(pin_number=cfg['pin']['vca_sw'])
solar = IndicatedSwitch(switch_pin=cfg['pin']['solar_sw'],
                        switch_led=cfg['pin']['solar_led'])
wind = IndicatedSwitch(switch_pin=cfg['pin']['wind_sw'],
                       switch_led=cfg['pin']['wind_led'])
battery = IndicatedSwitch(switch_pin=cfg['pin']['batt_sw'],
                          switch_led=cfg['pin']['batt_led'])
