from collections import OrderedDict

from lewis.devices import StateMachineDevice

from .states import DefaultState


class SimulatedSimDevice(StateMachineDevice):
    def _initialize_data(self):
        self.idn = "SimDevice v1.0"
        self.measurement = 0.0
        self.setpoint = 0.0

    def _get_state_handlers(self):
        return {"default": DefaultState()}

    def _get_initial_state(self):
        return "default"

    def _get_transition_handlers(self):
        return OrderedDict([])
