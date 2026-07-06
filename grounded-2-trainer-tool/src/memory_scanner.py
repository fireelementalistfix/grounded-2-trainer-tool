import ctypes
import ctypes.wintypes
from typing import List, Optional

class MemoryScanner:
    def __init__(self, process_name: str = "Grounded2.exe"):
        self.process_name = process_name
        self.process_handle: Optional[int] = None
        self._open_process()

    def _open_process(self) -> None:
        kernel32 = ctypes.windll.kernel32
        PROCESS_ALL_ACCESS = 0x1F0FFF
        self.process_handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, self._get_pid())

    def _get_pid(self) -> int:
        import psutil
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == self.process_name:
                return proc.info['pid']
        raise RuntimeError(f"Process {self.process_name} not found")

    def read_int(self, address: int) -> int:
        buffer = ctypes.c_int(0)
        bytes_read = ctypes.c_size_t(0)
        ctypes.windll.kernel32.ReadProcessMemory(
            self.process_handle, address, ctypes.byref(buffer), ctypes.sizeof(buffer), ctypes.byref(bytes_read)
        )
        return buffer.value

    def write_int(self, address: int, value: int) -> None:
        buffer = ctypes.c_int(value)
        bytes_written = ctypes.c_size_t(0)
        ctypes.windll.kernel32.WriteProcessMemory(
            self.process_handle, address, ctypes.byref(buffer), ctypes.sizeof(buffer), ctypes.byref(bytes_written)
        )

    def close(self) -> None:
        if self.process_handle:
            ctypes.windll.kernel32.CloseHandle(self.process_handle)