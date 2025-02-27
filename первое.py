class Office:           #определение класса кабинет
    def __init__(self, ZavOffice, square):      #создание констуктора с параметрами зав кабинета и площадь
        self.__ZavOffice = ZavOffice  #объявление и присваивание поля класса приватный атрибут
        self.__square = square    #объявление и присваивание поля класса приватный атрибут
    def get_ZavOffice(self): 
        return self.__ZavOffice 
    def set_ZavOffice(self, ZavOffice):  
        self.__ZavOffice = ZavOffice
    def get_square(self):    
        return self.__square 
    def set_square(self, square):    
        self.__square = square 
office1 = Office("Иванов Иван Иванович", 40) 
print("Кабинет 1:")
print("Заведующий первого кабинета: ", office1.get_ZavOffice())
print("Площадь первого кабинета: ", office1.get_square())
office2 = Office("Петров Петр Петрович", 67) 
print("Кабинет 2:")
print("Заведующий второго кабинета: ", office2.get_ZavOffice())
print("Площадь второго кабинета: ", office2.get_square())