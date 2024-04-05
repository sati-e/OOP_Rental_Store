from abc import ABC, abstractmethod
import random


# creating class
class RentalStore(ABC):
    count = 0   # counter
    rental_list = []    # creating list to store the numbers of records
    rental_numbers = set()

    @classmethod
    def get_people_count(cls):
        return cls.count

    @classmethod
    def get_rental_list(cls):
        return cls.rental_list

    # creating attributes
    def __init__(self, title, director, return_date, rental_price=15):
        self.rental_price = rental_price
        self.title = title
        self.director = director
        self.return_date = return_date
        self.generate_rental_number()   # random number for books
        RentalStore.count += 1  # counter
        RentalStore.rental_list.append(self)    # list store

    @abstractmethod
    def calculate_penalty(self):
        pass

    # generate a random number for books
    @staticmethod
    def generate_rental_number():
        while True:
            rental_num = random.randrange(1, 1000 + 1)
            if rental_num not in RentalStore.rental_numbers:
                print("Rental Number:", rental_num)
                RentalStore.rental_numbers.add(rental_num)
                return rental_num

    # print
    def __str__(self):
        show_data = f"\nTitle: {self.title} \nDirector: {self.director} " \
                    f"\nRental Number: {self.generate_rental_number()}" \
                    f"\nReturn Date: {self.return_date}"
        return show_data


# creating subclass
class Movies(RentalStore):
    def __init__(self, title, director, return_date, duration):
        super().__init__(title, director, return_date)
        self.duration = duration

    # method to calculate penalty to delays
    def calculate_penalty(self):
        while True:
            extra_days = int(input("Enter the number of extra days: "))
            if extra_days >= 0:
                total_penalty = (5 * extra_days) + self.rental_price
                return total_penalty
            else:
                print("Extra days can't be negative")

    def get_duration(self):
        return self.duration

    def set_duration(self, new_duration):
        self.duration = new_duration

    # print
    def __str__(self):
        return super().__str__() + f"\nDuration: {self.duration}"


# creating subclass
class Series(RentalStore):
    def __init__(self, title, director, return_date, chapters):
        super().__init__(title, director, return_date)
        self.chapters = chapters

    def get_chapters(self):
        return self.chapters

    def set_chapters(self, new_chapters):
        self.chapters = new_chapters

    # method to calculate penalty to delays
    def calculate_penalty(self):
        extra_days = int(input("Extra days: "))
        if extra_days != 0:
            total_penalty = (10 * extra_days) + self.rental_price
            return total_penalty
        else:
            print("No penalties")

    # print
    def __str__(self):
        return super().__str__() + f"\nEpisodes: {self.chapters}"


# testing methods and creating objects
if __name__ == '__main__':
    movie1 = Movies("The Phantom of the Opera", "Joel T. Schumacher", "05/10/2024", 2)
    print(movie1)

    movie_penalty = movie1.calculate_penalty()
    print(f"Loan cost: {movie_penalty}")

    print(f"Movie Duration: {movie1.get_duration()}")

    series1 = Series("Supernatural", "Eric Kripke", "05/15/2024", 15)
    print(series1)

    series_penalty = series1.calculate_penalty()
    print(f"Loan cost: {series_penalty}")

    print(f"Series Episodes: {series1.get_chapters()}")
