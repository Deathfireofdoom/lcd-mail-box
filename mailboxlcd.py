from time import sleep
#from rpi_lcd import LCD




def display_message(message, times=5):
    lcd = LCD()
    msg = message['message']
    signedby = message['signedby']

    msg = 16*" " + msg + 16*" "

    lcd.text(f"- {signedby}", 2)
    
    for _ in range(times):
        for x in range(len(msg) + 16 ):
            display_text = msg[x: x+16]
            lcd.text(display_text, 1)
            sleep(0.5)
    lcd.clear()