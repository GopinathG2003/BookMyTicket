# Movie class to represent each movie
class Movie:
    def __init__(self, title, available_seats):
        self.title = title
        self.available_seats = available_seats

    def book_seat(self, num_seats):
        if self.available_seats >= num_seats:
            self.available_seats -= num_seats
            return True
        else:
            return False

# Cinema class to manage movies and bookings
class Cinema:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, available_seats):
        movie = Movie(title, available_seats)
        self.movies[title] = movie

    def display_movies(self):
        print("\nAvailable Movies:")
        for title, movie in self.movies.items():
            print(f"{title}: {movie.available_seats} seats available")

    def book_ticket(self, title, num_seats):
        if title in self.movies:
            movie = self.movies[title]
            if movie.book_seat(num_seats):
                print(f"Booking confirmed for {num_seats} ticket(s) to '{title}'.")
                print(f"{movie.available_seats} seats remaining.")
            else:
                print(f"Sorry, only {movie.available_seats} seat(s) available for '{title}'.")
        else:
            print(f"Sorry, the movie '{title}' is not available.")

# Booking system to interact with the user
class BookingSystem:
    def __init__(self):
        self.cinema = Cinema()

    def initialize_movies(self):
        # Add some movies to the cinema
        self.cinema.add_movie("The Matrix", 50)
        self.cinema.add_movie("Inception", 75)
        self.cinema.add_movie("Interstellar", 60)
        self.cinema.add_movie("The Dark Knight", 40)

    def start(self):
        self.initialize_movies()
        while True:
            self.cinema.display_movies()
            choice = input("\nWould you like to book a ticket? (yes/no): ").lower()
            if choice == 'no':
                print("Thank you for using the movie ticket booking system!")
                break
            elif choice == 'yes':
                title = input("Enter the movie name: ")
                num_seats = int(input("Enter the number of tickets: "))
                self.cinema.book_ticket(title, num_seats)
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

# Run the movie ticket booking system
if __name__ == "__main__":
    booking_system = BookingSystem()
    booking_system.start()
