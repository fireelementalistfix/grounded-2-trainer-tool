using System;
using System.Threading;
using System.Threading.Tasks;

namespace Grounded2TrainerTool
{
    public class TrainerEngine
    {
        private readonly MemoryManager _memory;
        private bool _active;

        public TrainerEngine(MemoryManager memory)
        {
            _memory = memory;
            _active = false;
        }

        public async Task RunAsync(CancellationToken token)
        {
            _active = true;
            Console.WriteLine("Trainer engine active. Press Ctrl+C to stop.");

            while (!token.IsCancellationRequested && _active)
            {
                if (_memory.IsProcessRunning("Grounded2"))
                {
                    _memory.WriteFloat(0x12345678, 100.0f); // health
                    _memory.WriteInt32(0x87654321, 9999);   // resource
                    Console.WriteLine("Patches applied.");
                }
                await Task.Delay(1000, token);
            }

            Console.WriteLine("Trainer stopped.");
        }

        public void Stop() => _active = false;
    }
}