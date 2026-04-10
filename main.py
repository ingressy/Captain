import time
import threading

from Sensoren import ADC
from Motor import motors
from Comm import Comm

def main():
    print("===Testmode ===")
    adc = ADC.ADC()
    t1 = threading.Thread(target=Comm.connHandler, args=(adc))
    t1.start()
    t2 = threading.Thread(target=Comm.udpHandler)
    t2.start()

    print(adc.get_ampere(0))
    print(adc.get_12voltage(1))


    print("===Dreht Motoren in 5Sek!===")
    time.sleep(5)

    motors.vorwaerts(30, 100)


    # adc.de_ADC()
    print("===Testmode fertig!===")

if __name__ == '__main__':
    main()