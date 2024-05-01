import asyncio
from bleak import BleakScanner, BleakClient
import struct

CHARACTERISTIC_UUID = "19b10011-e8f2-537e-4f6c-d104768a1214"  # Replace with your characteristic UUID
ACCELEROMETER_UUID = "19b10011-e8f2-537e-4f6c-d104768a1215"
DEVICE_NAME = "Aether's LED"  # Replace with your device's name

async def send_data(client, value):
    await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([value]), response=True)

async def read_data(client):
    try:
        bytesRead = await client.read_gatt_char(ACCELEROMETER_UUID)
        print(bytesRead)
        value = struct.unpack('2f', bytesRead)
        print(value)
    except Exception:
        print(Exception)
    await client.disconnect()

    #print(f"Sensors read : {value}")

async def cycle_data(client):
    print("Performing actions")
    for _ in range(5):  # Send data for about 20 seconds (5 cycles of 4 seconds each)
        await send_data(client, 1)  # Send value of 1
        await asyncio.sleep(2)  # Wait for 2 seconds
        await send_data(client, 0)  # Send value of 0
        await asyncio.sleep(2)  # Wait for 2 seconds
    
    await client.disconnect()

async def scan_and_connect():
    scanner = BleakScanner()
    devices = await scanner.discover()
    for device in devices:
        if device.name == DEVICE_NAME:
            async with BleakClient(device) as client:
                print(f"Connected to device: {device.name}")
                if(client.services):
                    await read_data(client)
                #await cycle_data(client)
                break
        else:
            print(device.name)

asyncio.run(scan_and_connect())
