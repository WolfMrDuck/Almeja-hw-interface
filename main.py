import time
while True:
    data = {
            "voltmeters": {},
            "ammeters": {},
            "thermometers": {},
            "controllers": {},
            "switches": {
                "solar": solar.state,
                "wind": wind.state,
                "battery": battery.state
                }
            }
    for key, voltmeter in voltmeters.items():
        data["voltmeters"][key] = voltmeter.read()
    for key, ammeter in ammeters.items():
        data["ammeters"][key] = ammeter.read()
    for key, thermometer in thermometers.items():
        data["thermometers"][key] = thermometer.read()
    for key, controller in controllers.items():
        data["controllers"][key] = controller.duty_cycle

    json_data = json.dumps(data, separators=(',', ':'))
    print(json_data)
    time.sleep(5)
