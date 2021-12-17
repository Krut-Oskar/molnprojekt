using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace FunctionAppTest
{
    public static class GetCosmosDB
    {
        [FunctionName("GetCosmosDB")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequest req,
            [CosmosDB(databaseName:"molnprojektdb", 
            collectionName:"Messages",
            ConnectionStringSetting ="ComosDbConnection",
            SqlQuery = "SELECT top 1 * FROM c order by c._ts desc")]
            IEnumerable<dynamic> cosmos,
            ILogger log)
        {
            log.LogInformation("HTTP Function executed");
            return new OkObjectResult(cosmos);
        }
    }
}
