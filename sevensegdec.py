import argparse
from myhdl import *

@block
def sevensegdec(bcd: Signal, sseg: Signal, decod_table: tuple, invert: bool = False):
    ssegout = Signal(intbv(0)[7:])
    @always_comb
    def logic():
        ssegout.next = decod_table[int(bcd)]
    @always_comb
    def invertproc():
        if invert:
            sseg.next = ~ssegout
        else:
            sseg.next = ssegout
    return instances()

@block
def sevensegdec_nexys(bcd: Signal, sseg: Signal, bcdled: Signal, ssanodes: Signal, decod_table: tuple, invert: bool = False):
    ssdec = sevensegdec(bcd, sseg, decod_table, invert)
    @always_comb
    def logic():
        bcdled.next = bcd
        ssanodes.next = intbv(0xfe)[8:]
    return instances()

def read_table(table_file: str) -> tuple:
    if table_file != "":
        try:
            with open(table_file) as f:
                return tuple([int(x.strip(), base=2) for x in f.readlines() if x.strip()])
        except Exception as ex:
            print(f"Exception reading the table: {ex}")
    return tuple([0 for x in range(16)])

def run():
    parser = argparse.ArgumentParser(description="Seven segment decoder")
    parser.add_argument("--verilog", action="store_true", help="Convert to verilog instead of VHDL")
    parser.add_argument("--table", type=str, default="table.txt", help="Decoder table to include")
    args = parser.parse_args()

    table = read_table(args.table)

    # Signal list for conversion
    ss_sig = {
        "bcd": Signal(intbv(0)[4:]),
        "sseg": Signal(intbv(0)[7:]),
        "bcdled": Signal(intbv(0)[4:]),
        "ssanodes": Signal(intbv(0)[8:]),
        "invert": Signal(False),
        "decod_table": table
    }
    sscomponent = sevensegdec_nexys(**ss_sig)

    langout = "verilog" if args.verilog else "VHDL"
    sscomponent.convert(hdl=langout)
    print(f"Conversion done ({langout}).")

if __name__ == "__main__":
    run()
