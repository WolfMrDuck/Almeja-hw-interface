import time

while True:
    for key, voltmeter in voltmeters.items():
        print(f"{key} voltage value is: {voltmeter.read()} mV")
    for key, ammeter in ammeters.items():
        print(f"{key} current value is: {ammeter.read()} mA")
    for key, thermometer in thermometers.items():
        print(f"{key} temp value is: {thermometer.read()} m°C")
    time.sleep(5)
