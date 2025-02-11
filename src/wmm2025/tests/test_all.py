import pytest
import xarray

import wmm2025 as wmm


@pytest.mark.skip(reason="this test produces a segfault")
def test_wmm2025():
    mag = wmm.wmm(65, 85, alt_km=0, yeardec=2026.5)

    assert isinstance(mag, xarray.Dataset)

    assert mag.north.item() == pytest.approx(8739.604074620373)
    assert mag.east.item() == pytest.approx(2229.254013719841)
    assert mag.down.item() == pytest.approx(60367.1560360288649)
    assert mag.total.item() == pytest.approx(61037.23274131179)

    assert mag.incl.item() == pytest.approx(81.50231579494661)
    assert mag.decl.item() == pytest.approx(14.3095835428016975)


def test_wmm2025_point():
    mag = wmm.wmm_point(65, 85, alt_km=0, yeardec=2026.5)
    assert isinstance(mag, dict)

    assert mag["north"] == pytest.approx(8739.604074620373)
    assert mag["east"] == pytest.approx(2229.254013719841)
    assert mag["down"] == pytest.approx(60367.156036028864)
    assert mag["horiz"] == pytest.approx(9019.437501241806)
    assert mag["total"] == pytest.approx(61037.23274131179)

    assert mag["incl"] == pytest.approx(81.50231579494661)
    assert mag["decl"] == pytest.approx(14.309583542801697)
