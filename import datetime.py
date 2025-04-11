import datetime
class Book: 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_info(self): 
        return f"{self.title}, ({self.author}, {self.year})"
    def is_classic(self): 
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        return age > 50
book1 = Book("Джейн Эйр", "Шарлотта Бронте", 1847)
print(book1.get_info())
print(book1.is_classic())

book2 = Book("Мальчик в полосатой пижаме", "Джон Бойн", 2006)
print(book2.get_info())
print(book2.is_classic())