
import os
import random
import time
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message


load_dotenv()
#Connection string is stored in a .env file
CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")


TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'


def run_telemetry_sample(client):

    print("Starting to send")

    client.connect()

    while True:
        
        temperature = TEMPERATURE + (random.random() * 15)
        humidity = HUMIDITY + (random.random() * 20)
        msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
        message = Message(msg_txt_formatted)

        print("Sending message: {}".format(message))
        client.send_message(message)
        print("Message sent")
        time.sleep(10)


def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    try:
        run_telemetry_sample(client)
    except KeyboardInterrupt:
        print("stopped by user")
    finally:
        print("Shutting down")
        client.shutdown()

if __name__ == '__main__':
    main()
