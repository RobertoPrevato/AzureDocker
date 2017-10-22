using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;

namespace webhelloworld
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            // TO DEPLOY: https://docs.microsoft.com/en-us/azure/app-service/scripts/app-service-cli-deploy-local-git
        }

        private const int MaxPage = 101;

        private static Dictionary<int, string> Values { get; set; }

        private static string GetBodyOfSize(int i) 
        {
            if (Values.ContainsKey(i))
                return Values[i];
            
            var s = new String('X', i);
            Values.TryAdd(i, s);
            return s;
        }

        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            Values = new Dictionary<int, string>();

            app.Run(async (context) =>
            {
                var request = context.Request;
                var s = request.Query["s"];

                if (string.IsNullOrEmpty(s)) {
                    // return simple hello, world
                    var now = DateTime.UtcNow;
                    await context.Response.WriteAsync($"Hello World, from ASP.NET Core and Net Core 2.0! {now.ToString("yyyy-MM-dd HH:mm:ss.FFF")}");
                    return;
                }

                if (int.TryParse(s, out int i)) {
                    if (i > 0 && i < MaxPage) {
                        var body = GetBodyOfSize(i * 1000);
                        await context.Response.WriteAsync(body);
                    } else {
                        context.Response.StatusCode = 400;
                        await context.Response.WriteAsync($"Size must be an integer between 1 and {MaxPage}");
                    }
                } else {
                    context.Response.StatusCode = 400;
                    await context.Response.WriteAsync($"Size must be an integer between 1 and {MaxPage}");
                }
            });
        }
    }
}
