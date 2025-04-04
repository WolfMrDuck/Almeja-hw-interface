import time
from _thread import start_new_thread

def thr_send_data():
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

start_new_thread(thr_send_data, ())

while True:
    try:
        cmd, arg = input().split()
        cmd = cmd.upper()
        arg = int(arg)
    except:
        continue
    if cmd == 'B':
        if arg == 0:
            battery.off()
        elif arg == 1:
            battery.on()
    elif cmd == 'S':
        if arg == 0:
            solar.off()
        elif arg == 1:
            solar.on()
    elif cmd == 'W':
        if arg == 0:
            wind.off()
        elif arg == 1:
            wind.on()
    elif cmd == 'X':
        controllers['solar'].set_duty_cycle(arg)
    elif cmd == 'Y':
        controllers['wind'].set_duty_cycle(arg)
