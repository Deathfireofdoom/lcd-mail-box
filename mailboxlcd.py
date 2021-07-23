from time import sleep
from rpi_lcd import LCD




def display_message(message, times=5):
    lcd = LCD()
    msg = message['message']
    signedby = message['signedby']

    msg = 16*" " + msg

    if len(signedby) > 14:
        words = msg.split()
        signedby_compact = f"{words[0][0]}. {' '.join(words[1:])}"
        lcd.text(f"- {signedby_compact}", 2)
    else:
        lcd.text(f"- {signedby}", 2)
    
    for _ in range(times):
        for x in range(len(msg) ):
            display_text = msg[x: x+16]
            lcd.text(display_text, 1)
            sleep(0.2)
    lcd.clear()