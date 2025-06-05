import time
from sys import stdin
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
                    "battery": battery.state,
                    "load": load.state,
                    "vca": vca.state
                    }
                }
        for key, voltmeter in voltmeters.items():
            data["voltmeters"][key] = 0.0
        for key, ammeter in ammeters.items():
            data["ammeters"][key] = 0.0
        for key, thermometer in thermometers.items():
           data["thermometers"][key] = 0.0

        for i in range(cfg['core']['samples_per_read']):
            for key, voltmeter in voltmeters.items():
                data["voltmeters"][key] += voltmeter.read()
            for key, ammeter in ammeters.items():
                data["ammeters"][key] += ammeter.read()
            for key, thermometer in thermometers.items():
               data["thermometers"][key] += thermometer.read()

        for key, voltmeter in voltmeters.items():
            data["voltmeters"][key] /= cfg['core']['samples_per_read']
        for key, ammeter in ammeters.items():
            data["ammeters"][key] /= cfg['core']['samples_per_read']
        for key, thermometer in thermometers.items():
           data["thermometers"][key] /= cfg['core']['samples_per_read']
            
        for key, controller in controllers.items():
            data["controllers"][key] = controller.duty_cycle
    
        json_data = json.dumps(data, separators=(',', ':'))
        print(json_data)
        time.sleep(cfg['core']['read_period'])

def thr_battery_watchdog():
    for _, thermometer in thermometers.items():
        if thermometer.read() >= cfg['core']['temp_threshold']:
            battery.off()
    time.sleep(cfg['core']['battery_wd_period'])

def safe_solar_on():
    wind.off()
    solar.on()

def safe_wind_on():
    solar.off()
    wind.on()

def safe_load_on():
    vca.off()
    load.on()

def safe_vca_on():
    load.off()
    vca.on()

def instruction_handler():
    while True:
        try:
            cmd, arg = stdin.readline().split()
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
                safe_solar_on()
        elif cmd == 'W':
            if arg == 0:
                wind.off()
            elif arg == 1:
                safe_wind_on()
        elif cmd == 'L':
            if arg == 0:
                load.off()
            elif arg == 1:
                safe_load_on()
        elif cmd == 'V':
            if arg == 0:
                vca.off()
            elif arg == 1:
                safe_vca_on()
        elif cmd == 'X':
            controllers['solar'].set_duty_cycle(arg)
        elif cmd == 'Y':
            controllers['wind'].set_duty_cycle(arg)

start_new_thread(thr_send_data, ())
start_new_thread(thr_battery_watchdog, ())

instruction_handler()
