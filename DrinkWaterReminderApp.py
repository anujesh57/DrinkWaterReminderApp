import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title= "PLEASE DRINK WATER NOW",
            message= "Drink more water. Your skin, your hair, your mind and body will thank you.",
            app_icon= "",
            timeout=10
        )
        time.sleep(60*60)

