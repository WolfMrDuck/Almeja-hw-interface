from modules import Sensor
import json

config_file = open("config.json",'r')
cfg = json.load(config_file)

solar_voltmeter = Sensor(pin_number=cfg['pin']['solar'])
