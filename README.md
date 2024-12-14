# ticketbooking
Movie ticket booking system simulates ticket booking experience
# Movie Ticket Booking System

This repository contains a Python program that simulates a movie ticket booking system. The project is designed to provide a simple and interactive experience for users to book tickets, view available seats, and calculate their total bill. Below are the details and instructions for using the program.

## Features

- **Movie Selection**: Users can choose from a list of available movies.
- **Seat Availability**: Seats are displayed in a visual pattern, showing booked (X) and available seats.
- **Booking**: Users can select how many tickets they want to book and choose specific seats.
- **Billing**: The total cost of the tickets is displayed at the end.
- **Continuous Operation**: The program runs until the user chooses to exit.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-ticket-booking.git
   cd movie-ticket-booking
   ```
2. Run the program:
   ```bash
   python movie_booking.py
   ```

## Usage

1. **Choose a Movie**:
   - The program will display a list of movies.
   - Enter the number corresponding to the movie you want to watch.

2. **View Seats**:
   - A seating chart will be displayed, showing available seats and already booked seats (marked as `X`).

3. **Book Tickets**:
   - Enter the number of tickets you want to book.
   - Choose specific seats from the seating chart.

4. **View Total Bill**:
   - Once tickets are booked, the program calculates and displays the total cost.

5. **Exit the Program**:
   - You can exit the program by selecting the appropriate option.

## Example

Here is an example of how the program works:

```
Welcome to the Movie Ticket Booking System!

Available Movies:
1. Movie A
2. Movie B
3. Movie C

Enter the number of the movie you want to watch: 1

Seating Chart:
O O O O
O X O O
O O O O

Enter the number of tickets you want to book: 2
Choose your seats (e.g., 1A, 1B): 1A, 2C

Updated Seating Chart:
X O O O
O X O O
O X O O

Your total bill is $20.
```

## Program Details

- **Movies and Prices**:
  - The program includes a predefined list of movies and their ticket prices.
  - You can customize the list by modifying the code.

- **Seating Chart**:
  - Seats are represented in a grid pattern.
  - Available seats are shown as `O`.
  - Booked seats are marked as `X`.

- **Nested Loops**:
  - The seating chart is displayed using nested loops for dynamic updates.

## Future Improvements

- Add user authentication for personalized booking history.
- Include an option to cancel tickets.
- Support for multiple screens or showtimes.
- Enhanced UI using a graphical interface.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Arun, for inspiring the idea of this project.
- Python community, for the tools and resources.

---

Happy Booking! :movie_camera:
