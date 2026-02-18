Human–wildlife conflict is a major issue in farms, forest borders, and rural areas.
This project provides a smart monitoring solution that detects animal intrusion and immediately alerts authorities or landowners.

When the touch sensor is triggered:

🔔 Buzzer turns ON

💡 LED turns ON

📧 Email alert is sent

📱 WhatsApp alert is sent using Twilio

🌡 Temperature & Humidity data sent to Blynk app

🛠 Hardware Components Used

🖥 Raspberry Pi

👆 Touch Sensor

🔥 DHT11 Temperature & Humidity Sensor

👀 PIR Motion Sensor

📡 Ultrasonic Sensor

🔔 Buzzer

💡 LED

Jumper Wires

💻 Software & Technologies Used

🐍 Python

RPi.GPIO

Blynk IoT

Twilio API (WhatsApp Alerts)

SMTP (Email Alerts)

Adafruit DHT Library

⚙️ Working Principle

The system continuously monitors the Touch Sensor.

When an animal touches the protected area:

LED & Buzzer activate.

Email alert is sent.

WhatsApp alert is sent via Twilio.

Temperature and humidity data from DHT11 are uploaded to the Blynk Cloud.

The system resets automatically after the touch is released.

🔌 GPIO Pin Configuration
Component	GPIO Pin
TRIG	20
ECHO	21
PIR	26
Touch Sensor	17
Buzzer	12
LED	16
DHT11	GPIO 4
📱 Alert System
📧 Email Alert

Uses Gmail SMTP

Sends instant wildlife detection message

📲 WhatsApp Alert

Implemented using Twilio WhatsApp API

Sends real-time notification message

📊 Blynk Dashboard

Displays:

Temperature (Virtual Pin V0)

Humidity (Virtual Pin V1)

🚀 How to Run the Project

Install Required Libraries:

pip install RPi.GPIO blynklib twilio adafruit-circuitpython-dht


Enable I2C and required interfaces on Raspberry Pi.

Update credentials in the code:

Blynk Auth Token

Email ID & Password

Twilio SID & Auth Token

WhatsApp numbers

Run the program:

python wildlife.py

📸 Future Enhancements

Add Camera module for image capture

Add AI-based animal detection

Solar-powered system

SMS alert integration

Cloud database logging

🎯 Applications

Farms & Agricultural fields

Forest Border Areas

Village Outskirts

Wildlife Research Monitoring

Highway Animal Crossing Zones
