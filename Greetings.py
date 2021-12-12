from myhdl import block, Signal, delay,always, now, instances

from ClkDriver import ClkDriver
from Hello import Hello

@block
def Greetings():

    clk1 = Signal(0)
    clk2 = Signal(0)

    clkdriver_1 = ClkDriver(clk1)
    clkdriver_2 = ClkDriver(clk=clk2, period=19)
    hello_1 = Hello(clk=clk1)
    hello_2 = Hello(to="MyHDL", clk=clk2)

    return clkdriver_1, clkdriver_2, hello_1, hello_2

inst = Greetings()
inst.run_sim(50)



