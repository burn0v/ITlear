from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, device_id, location, is_on=False):
        self._device_id = device_id
        self.location = location
        self._is_on = is_on

    @property
    def device_id(self):
        return self._device_id

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if value == "":
            print("Ошибка локации")
        else:
            self._location = value

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, value):
        if type(value) != bool:
            print("is_on должен быть bool")
        self._is_on = value

    def toggle_power(self):
        self._is_on = not self._is_on

    @abstractmethod
    def perform_action(self):
        pass

    @abstractmethod
    def get_status(self):
        pass
