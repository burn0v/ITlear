from smart_device import SmartDevice


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, location, current_temperature, target_temperature, is_on=False):
        super().__init__(device_id, location, is_on)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, value):
        if value < -50 or value > 50:
            value = 20
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        if value < 5 or value > 35:
            print("Неверная температура")
        self._target_temperature = value

    def perform_action(self):
        return f"Нагрев до {self.target_temperature}°C"

    def get_status(self):
        state = "вкл" if self.is_on else "выкл"
        return f"Термостат {self.device_id} {state}, {self.current_temperature}/{self.target_temperature}°C"
