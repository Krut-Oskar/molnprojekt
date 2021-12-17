# Projekt Arbete IoT och Molntjänster

## Summary

The idea of this project is to build an app which will tell me if I can take the bike to school/work or if it's better to use the subway. It will do this by collecting temperature data from a sensor and determine wether it's too cold to bike, if it is the app will recommend subway departures for me. This is to relieve me of some stress in the morning.

I chose to build the idea in Azure mainly due to  economic reasons, since I can use their student credit. I have some earlier experience with Azure, but it's been a long time since I've used them and I wanted to refresh and expand my knowledege.

## Device

In this project I've used a simulated device to be able to produce different types of temperature data. The reason I didn't build a device with a temperature sensor is because it's winter time and I wanted to test my project with various temperatures. I built the simulated device in python and sent the values to Azure IoT-Hub.

## Storage

I chose to store the messages from the device in a CosmosDB. CosmosDB works great to store simple telemetry messages from a device in cases that doesn't require a relational database. It's also easy to integrate with IoT Hub and Azure Functions. I chose to use the standard API which is a uses SQL-like queries to get data from the database, because of the easy syntax and good documentation.

## Functions

I have two functions inside one function app. The first one triggers on a every new message in the IoT Hub and forwards the message to CosmosDB. The second one triggers on a HTTP request from the website and sends the contents of the cosmosDB as a response.
I chose to write the Azure functions i C# and develop and testing them locally before pushing them to Azure. I thought about developing them in a different language like Python but in the end I found it more convenient to make them in C#.

## Website

## API

Because of restrictions of certain API:s I chose to call the API:s from the backend of the website, instead of from a Azure Function. This is because some of the API:s didn't allow any retention of data, and I didn't want to risk anything by saving the data in the database. I could have used an azure function to call the with either a timing trigger or HTTP Request trigger, but since that would only mean an extra step instead of just calling it directly from the website backend.
## Future