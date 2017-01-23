
import threading

from .fifo import BytesFIFO


class ThreadsafeBytesFIFO(BytesFIFO):
    """
    A thread-safe FIFO that can store a fixed number of bytes.
    """
    def __init__(self, init_size):
        """ Create a FIFO of ``init_size`` bytes. """
        super().__init__(init_size)
        self.lock = threading.Lock()

    def read(self, size=-1):
        """
        Read at most ``size`` bytes from the FIFO.

        If less than ``size`` bytes are available, or ``size`` is negative,
        return all remaining bytes.
        """
        self.lock.acquire()

        ret = super().read(size=size)

        self.lock.release()
        return ret

    def write(self, data):
        """
        Write as many bytes of ``data`` as are free in the FIFO.

        If less than ``len(data)`` bytes are free, write as many as can be written.
        Returns the number of bytes written.
        """
        self.lock.acquire()

        ret = super().write(data)

        self.lock.release()
        return ret

    def free(self):
        """ Return the number of bytes that can be written to the FIFO. """
        self.lock.acquire()

        size = super().free()

        self.lock.release()
        return size

    def resize(self, new_size):
        """
        Resize FIFO to contain ``new_size`` bytes. If FIFO currently has
        more than ``new_size`` bytes filled, :exc:`ValueError` is raised.
        If ``new_size`` is less than 1, :exc:`ValueError` is raised.

        If ``new_size`` is smaller than the current size, the internal
        buffer is not contracted (yet).
        """
        self.lock.acquire()

        super().resize(new_size)

        self.lock.release()
