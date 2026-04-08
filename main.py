import time

from Sensoren import Batterie
from motors import deathrun

def main():
    print("===Testmode ===")
    spi, cs, chan0, chan1, chan2, chan3 = Batterie.initmcp()

    Batterie.read_ampere(chan0)
    Batterie.read_voltage(chan1)
    time.sleep(0.5)
    deathrun.deathrun(5,True,25)
    Batterie.deinitmcp(spi,cs)



if __name__ == '__main__':
    main()