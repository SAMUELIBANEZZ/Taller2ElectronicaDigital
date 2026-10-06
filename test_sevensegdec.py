import pytest
from myhdl import *
from sevensegdec import sevensegdec, read_table

TABLE = read_table("table.txt")

@pytest.mark.parametrize("bcd_val", range(16))
def test_decoder_parameterized(bcd_val):
    bcd_tb = Signal(intbv(0)[4:])
    sseg_tb = Signal(intbv(0)[7:])
    
    uut = sevensegdec(bcd_tb, sseg_tb, TABLE, invert=False)
    
    @instance
    def stimulus():
        bcd_tb.next = bcd_val
        yield delay(10)
        sseg_readed = int(sseg_tb.val)
        sseg_expect = TABLE[bcd_val]
        assert sseg_readed == sseg_expect, f"Mismatch at BCD {bcd_val}: expected {sseg_expect:07b}, got {sseg_readed:07b}"
        
    sim = Simulation(uut, stimulus)
    sim.run()
