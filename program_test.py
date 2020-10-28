import moteur_ev
import led
import time

led.blink_party()

moteur_ev.motor_start()
time.sleep(10)
moteur_ev.motor_stop()

moteur_ev.ph_start()
time.sleep(10)
moteur_ev.ph_stop()

moteur_ev.conduct_start()
time.sleep(10)
moteur_ev.conduct_stop()
