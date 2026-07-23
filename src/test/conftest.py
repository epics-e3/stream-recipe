from logging import getLogger
import subprocess
import time
from pathlib import Path

import pytest
from run_iocsh import IOC

LOG = getLogger(__name__)

TEST_DIR = Path(__file__).parent
IOC_DIR = TEST_DIR / "ioc"
STARTUP_SCRIPT = IOC_DIR / "st.cmd"

SIMULATOR_BIND_ADDRESS = "127.0.0.1"
SIMULATOR_PORT = 38081
SIMULATOR_WARMUP_TIME_SECONDS = 5.0


@pytest.fixture(scope="session")
def lewis_device():
    proc = subprocess.Popen(
        [
            "lewis",
            "-a",
            TEST_DIR.as_posix(),
            "-k",
            "emulator",
            "sim_device",
            "-p",
            f"stream: {{port: {SIMULATOR_PORT}, bind_address: '{SIMULATOR_BIND_ADDRESS}'}}",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    time.sleep(SIMULATOR_WARMUP_TIME_SECONDS)
    yield proc
    proc.terminate()
    outs, errs = proc.communicate()
    # Dump logs on test failure
    LOG.error("Simulator stdout:\n%s", outs)
    LOG.error("Simulator stderr:\n%s", errs)


@pytest.fixture(scope="session")
def ioc(lewis_device):
    ioc_proc = IOC(STARTUP_SCRIPT.as_posix())
    with ioc_proc:
        ioc_proc.wait_for_output()
        yield ioc_proc
    # Dump logs on test failure
    LOG.error("IOC stdout:\n%s", ioc_proc.stdout)
    LOG.error("IOC stderr:\n%s", ioc_proc.stderr)
