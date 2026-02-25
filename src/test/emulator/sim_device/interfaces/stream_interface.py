from lewis.adapters.stream import StreamInterface, Var
from lewis.core.logging import has_log
from lewis.utils.command_builder import CmdBuilder


@has_log
class SimDeviceStreamInterface(StreamInterface):
    in_terminator = "\r\n"
    out_terminator = "\r\n"

    commands = {
        Var("idn", read_pattern=r"^\*IDN\?$", doc="Device identification"),
        Var("measurement", read_pattern=r"^MEAS\?$", doc="Current measurement"),
        Var("setpoint", read_pattern=r"^SP\?$", doc="Current setpoint"),
        CmdBuilder("set_setpoint").escape("SET ").float().eos().build(),
    }

    def set_setpoint(self, value):
        self._device.setpoint = value

    def handle_error(self, request, error):
        self.log.error("cmd=%s error=%s: %s", request, type(error).__name__, error)
