import time

import pytest
from p4p.client.thread import Context

PREFIX = "TEST:"
SLEEP_TIME_SECONDS = 1.5


@pytest.fixture(scope="module")
def ctx(ioc):
    c = Context("pva")
    yield c
    c.close()


def test_idn(ctx):
    val = ctx.get(PREFIX + "IDN")
    assert "SimDevice" in val


def test_read_measurement(ctx):
    val = ctx.get(PREFIX + "MEAS")
    assert val == pytest.approx(0.0)


def test_set_and_readback(ctx):
    ctx.put(PREFIX + "SET", 42.0)

    time.sleep(SLEEP_TIME_SECONDS)

    sp = ctx.get(PREFIX + "SP")
    assert sp == pytest.approx(42.0)
