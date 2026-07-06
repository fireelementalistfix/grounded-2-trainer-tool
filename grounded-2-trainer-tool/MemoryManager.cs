using System;
using System.Diagnostics;

namespace Grounded2TrainerTool
{
    public class MemoryManager
    {
        public bool IsProcessRunning(string name)
        {
            var processes = Process.GetProcessesByName(name);
            return processes.Length > 0;
        }

        public void WriteFloat(IntPtr address, float value)
        {
            // In real project: use kernel32.dll WriteProcessMemory
            Console.WriteLine($"WriteFloat: Address=0x{address.ToInt64():X8}, Value={value}");
        }

        public void WriteInt32(IntPtr address, int value)
        {
            Console.WriteLine($"WriteInt32: Address=0x{address.ToInt64():X8}, Value={value}");
        }
    }
}