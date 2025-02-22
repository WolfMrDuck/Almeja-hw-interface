from modules import Sensor
import json

config_file = open("config.json",'r')
cfg = json.load(config_file)

voltmeters = {
        "solar": Sensor(pin_number=cfg['pin']['solar'],
                        calibration_factor=cfg['factor']['solar']),
        "wind": Sensor(pin_number=cfg['pin']['wind'],
                        calibration_factor=cfg['factor']['wind']),
        "batt": Sensor(pin_number=cfg['pin']['batt_vm'],
                        calibration_factor=cfg['factor']['batt_vm']),
        }

ammeters = {
        "source": Sensor(pin_number=cfg['pin']['source'],
                        calibration_factor=cfg['factor']['source']),
        "batt": Sensor(pin_number=cfg['pin']['batt_amm'],
                        calibration_factor=cfg['factor']['batt_amm']),
        }

thermometers = {
        "therm1": Sensor(pin_number=cfg['pin']['batt_temp1'],
                        calibration_factor=cfg['factor']['batt_temp1']),
        "therm2": Sensor(pin_number=cfg['pin']['batt_temp2'],
                        calibration_factor=cfg['factor']['batt_temp2']),
        "therm3": Sensor(pin_number=cfg['pin']['batt_temp3'],
                        calibration_factor=cfg['factor']['batt_temp3']),
        }
