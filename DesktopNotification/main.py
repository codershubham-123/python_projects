# Program to remind for drink water

import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Drink more water.",
            message = "Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
            # app_icon = "DesktopNotification\icon.png", 
            timeout = 10,
        )
# It will give notification after one hour
        time.sleep(60*60)