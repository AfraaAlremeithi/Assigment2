class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

    def display_info(self):
        print("\nArtwork details:")
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Date of creation: {self.date_of_creation}")
        print(f"Historical significance: {self.historical_significance}")
        print(f"location: {self.location}")


class Visitor:
    def __init__(self, name, age, nationality, category=""):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.category = category

    def display_info(self):
        print("\nVisitor details:")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"nationality: {self.nationality}")


class Ticket:
    def __init__(self, visitor, exhibition, Standard_price):
        self.visitor = visitor
        self.exhibition = exhibition
        self.Standard_price = Standard_price #i got the standard price from the louvre website

    def calculate_price(self):
        ticket_price = self.Standard_price

        if 18 <= self.visitor.age <= 60 and self.visitor.category not in ["teacher", "student", "senior"]:
            ticket_price = self.Standard_price
        else:
            ticket_price = 0  #free ticket for categories ("teacher", "student", "senior")

        return ticket_price #if your not in the categories the code will calculate the price

    def apply_vat(self, price):
        return price * 1.05  # Apply 5% VAT

    def display_receipt(self):
        ticket_price = self.calculate_price()
        final_price = self.apply_vat(ticket_price)

        print("\nTicket receipt:")
        print(f"visitor: {self.visitor.name}")
        print(f"exhibition: {self.exhibition}")
        print(f"standard price: {self.Standard_price}")
        print(f"Final price: {final_price}")


class Exhibition:
    def __init__(self, name, location, duration):
        self.name = name
        self.location = location
        self.duration = duration

    def display_info(self):
        print("\nExhibition details:")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration} days")

class Tour:
    def __init__(self, guide, date, visitorGroup):
        self.guide = guide
        self.date = date
        self.visitorGroup = visitorGroup

    def display_info(self):
        print("\nTour details:")
        print(f"Guide: {self.guide}")
        print(f"Date: {self.date}")
        print(f"group: {self.visitorGroup}")

class SpecialEvent:
    def __init__(self, name, location, duration, price):
        self.name = name
        self.location = location
        self.duration = duration
        self.price = price

    def display_info(self):
        print("\nEvent details:")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration} hours")
        print(f"Price: {self.price}")

#objects example
art1 = Artwork("Starry Night", "Vincent van gogh", "1889", "impressionist painting", "Gallery 1")
art1.display_info()

v1 = Visitor("Afraa Alremeithi", 19, "Emarati")
v1.display_info()

exhib1 = Exhibition("Letters of Light", "exhibition hall 2", 25) #exhibition name was from the louvre website
exhib1.display_info()

ticket1 = Ticket(v1, exhib1.name, 63)
ticket1.display_receipt()

t1 = Tour("Khalid", "25-02-2024", "Group 3")
t1.display_info()

special_E1 = SpecialEvent("light show", "Outdoor space", 15, 150)
special_E1.display_info()
