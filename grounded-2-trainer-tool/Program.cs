using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace Grounded2TrainerTool
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Grounded 2 Trainer Tool - Starting...");
            using IHost host = CreateHostBuilder(args).Build();
            var trainer = host.Services.GetRequiredService<TrainerEngine>();
            await trainer.RunAsync(CancellationToken.None);
        }

        static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((_, services) =>
                {
                    services.AddSingleton<TrainerEngine>();
                    services.AddSingleton<MemoryManager>();
                });
    }
}