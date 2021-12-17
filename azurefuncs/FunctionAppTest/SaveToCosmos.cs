using IoTHubTrigger = Microsoft.Azure.WebJobs.EventHubTriggerAttribute;

using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Azure.EventHubs;
using System.Text;
using System.Net.Http;
using Microsoft.Extensions.Logging;

namespace FunctionAppTest
{
    public static class SaveToCosmos
    {
        private static HttpClient client = new HttpClient();

        [FunctionName("Function1")]
        public static void Run([IoTHubTrigger("messages/events", Connection = "IotHubConnection")]EventData message, [CosmosDB(
                databaseName: "molnprojektdb",
                collectionName: "Messages",
                ConnectionStringSetting = "ComosDbConnection",
                CreateIfNotExists = true
            )]out dynamic cosmos,
            ILogger log
        )
        {
            log.LogInformation($"C# IoT Hub trigger function processed a message: {Encoding.UTF8.GetString(message.Body.Array)}");
            cosmos = Encoding.UTF8.GetString(message.Body.Array);
        }
    }
}