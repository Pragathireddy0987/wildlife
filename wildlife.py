import time
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import RPi.GPIO as GPIO
import blynklib
from twilio.rest import Client
import adafruit_dht
import board

# ================= GPIO SETUP =================
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin definitions
TRIG = 20
ECHO = 21
PIR = 26
TOUCH = 17
BUZZER = 12
LED = 16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(TOUCH, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(BUZZER, GPIO.LOW)
GPIO.output(LED, GPIO.LOW)

# ================= DHT SENSOR =================
dht = adafruit_dht.DHT11(board.D4)

# ================= BLYNK =================
BLYNK_AUTH = "YY6YDeaWjR0sdeoDSb_Q-xcpr8eTt0ID"
blynk = blynklib.Blynk(BLYNK_AUTH)

# ================= EMAIL =================
EMAIL_SENDER = "abc@gmail.com"
EMAIL_PASSWORD = "jyqnjfbokzealohm"
EMAIL_RECEIVER = "nmnq26@gmail.com"

# ================= WHATSAPP (TWILIO) =================
TWILIO_SID = "ACeea924457a61b1a5a8c79bb3a2976b23"
TWILIO_AUTH = "8ab317baa1168c4efd19195efa6b6767"
WHATSAPP_FROM = "whatsapp:+14155238886"
WHATSAPP_TO = "whatsapp:+911234567890"

client = Client(TWILIO_SID, TWILIO_AUTH)

# ================= FLAGS =================
alert_sent = False   # prevents repeat alerts
# ================= FUNCTIONS =================
def send_email():
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = "🚨 Wildlife Alert"

        body = "Touch sensor activated.\nImmediate attention required."
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent")
    except Exception as e:
        print("Email error:", e)

def send_whatsapp():
    try:
        msg = client.messages.create(
            body="🚨 Wildlife Alert! Touch sensor activated.",
            from_=WHATSAPP_FROM,
            to=WHATSAPP_TO
        )
        print("WhatsApp SID:", msg.sid)
        print("WhatsApp Status:", msg.status)
    except Exception as e:
        print("WhatsApp error:", e)



# ================= MAIN LOOP =================
print("Wildlife Alert System Ready")
def alert_actions():
    GPIO.output(LED, GPIO.HIGH)   # LED ON
    GPIO.output(BUZZER, GPIO.HIGH)  # Buzzer ON

    send_email()
    send_whatsapp()

    GPIO.output(LED, GPIO.LOW)    # LED OFF immediately after sending
    time.sleep(5)                 # Buzzer will still sound for 5 seconds
    GPIO.output(BUZZER, GPIO.LOW) # Buzzer OFF

while True:
    blynk.run()

    touch_state = GPIO.input(TOUCH)

    # ---- TOUCH PRESSED ----
    if touch_state == GPIO.HIGH and not alert_sent:
        print("Touch detected")

        GPIO.output(LED, GPIO.HIGH)
        GPIO.output(BUZZER, GPIO.HIGH)

        threading.Thread(target=send_email).start()
        threading.Thread(target=send_whatsapp).start()

        alert_sent = True

    # ---- TOUCH RELEASED ----
    if touch_state == GPIO.LOW:
        GPIO.output(LED, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.LOW)
        alert_sent = False

    # ---- DHT TO BLYNK ----
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        if temperature is not None and humidity is not None:
            blynk.virtual_write(0, temperature)
            blynk.virtual_write(1, humidity)
    except:
        pass

    time.sleep(0.5)