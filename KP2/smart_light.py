from smart_device import SmartDevice


class SmartLight(SmartDevice):
    def __init__(self, device_id, location, brightness, color_temperature, is_on=False):
        super().__init__(device_id, location, is_on)
        self._brightness = brightness
        self.color_temperature = color_temperature

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if value < 0 or value > 100:
            print("Неверная яркость")
        self._brightness = value

    @property
    def color_temperature(self):
        return self._color_temperature

    @color_temperature.setter
    def color_temperature(self, value):
        if value not in ["теплый", "холодный", "нейтральный"]:
            value = "теплый"
        self._color_temperature = value

    def perform_action(self):
        return f"Свет {self.brightness}% {self.color_temperature}"

    def get_status(self):
        state = "вкл" if self.is_on else "выкл"
        return f"Лампа {self.device_id} {state}, {self.brightness}%, {self.color_temperature}"
