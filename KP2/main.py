from smart_light import SmartLight
from smart_thermostat import SmartThermostat


if __name__ == "__main__":
    light = SmartLight("L1", "Гостиная", 70, "теплый")
    thermo = SmartThermostat("T1", "Спальня", 22, 25)

    light.toggle_power()
    thermo.toggle_power()

    print(light.perform_action())
    print(light.get_status())

    print(thermo.perform_action())
    print(thermo.get_status())

    light.brightness = 150
    thermo.target_temperature = 100
    light.is_on = "on"

    print(light.get_status())
    print(thermo.get_status())
