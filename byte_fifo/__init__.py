
from .fifo import BytesFIFO

has_threading = False

try:
    import threading
    has_threading = True
except ModuleNotFoundError:
    raise Warning(
            "threading module not present, ThreadsafeBytesFIFO not available")

if has_threading:
    from .threadsafe_fifo import ThreadsafeBytesFIFO

