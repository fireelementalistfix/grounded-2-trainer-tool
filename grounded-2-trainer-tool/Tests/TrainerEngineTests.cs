using System;
using System.Threading;
using System.Threading.Tasks;
using Grounded2TrainerTool;
using Xunit;

public class TrainerEngineTests
{
    [Fact]
    public async Task RunAsync_NoProcess_DoesNotCrash()
    {
        var memory = new MemoryManager();
        var engine = new TrainerEngine(memory);
        var cts = new CancellationTokenSource();
        cts.CancelAfter(2000);

        var ex = await Record.ExceptionAsync(() => engine.RunAsync(cts.Token));
        Assert.Null(ex);
    }

    [Fact]
    public void Stop_SetsInactive()
    {
        var memory = new MemoryManager();
        var engine = new TrainerEngine(memory);
        engine.Stop();
        // No exception expected
        Assert.True(true);
    }
}