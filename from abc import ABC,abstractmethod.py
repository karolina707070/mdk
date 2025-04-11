from abc import ABC,abstractmethod
class Device(ABC): 
    @abstractmethod
    def turn_on(self): 
        pass 
    @abstractmethod
    def turn_off(self): 
        pass 
class Laptop(Device): 
    def turn_on(self): 
        print("включаем ноутбук")
    def turn_off(self): 
        print("выключаем ноутбук")
class Smartphone(Device): 
    def turn_on(self): 
        print("включаем телефон")
    def turn_off(self): 
        print("выключаем телефон")
laptop = Laptop()
smartphone = Smartphone()

laptop.turn_on()
laptop.turn_off()

smartphone.turn_on()
smartphone.turn_off()