from myhdl import block, Signal, delay,always, now

from ClkDriver import ClkDriver
from Hello import Hello


SLOW, MEDIUM, FAST = range(3)

@block
def top1(speed=SLOW):
    def slowAndSmall():
       return "Small"
    def fastAndLarge():
       return "Large"
    if speed == SLOW:
        return slowAndSmall()
    elif speed == FAST:
        return fastAndLarge()
    else:
        raise NotImplementedError

# @block
# def top():
#
#     din = Signal(0)
#     dout = Signal(0)
#     clk = Signal(bool(0))
#     reset = Signal(bool(0))
#
#     channel_inst = channel(dout, din, clk, reset)
#
#     return channel_inst

# @block ## arbitrary num of channels
# def top(..., n=8):
#
#     din = [Signal(0) for i in range(n)]
#     dout = [Signal(0) for in range(n)]
#     clk = Signal(bool(0))
#     reset = Signal(bool(0))
#     channel_inst = [None for i in range(n)]
#
#     for i in range(n):
#         channel_inst[i] = channel(dout[i], din[i], clk, reset)
#
#     return channel_inst



