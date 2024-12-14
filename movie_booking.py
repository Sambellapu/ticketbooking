def seats(b):
    print("      Screen")
    for i in range(1, 6):
        for a in range(1, 11):
            if (i, a) in dseats[b]:
                print("x", end=" ")
            else:
                print("-", end=" ")

        print("")


def book(m):
    seats(m)
    num = int(input("Enter the number of the of ticket(s) you want "))
    for i in range(num):
        r = int(input("Enter what row you want to sit in "))
        c = int(input("Enter what column you want to sit in "))
        dseats[m].append((r, c))
    seats(m)


dmovies = {1: "Avengers: Endgame", 2: "Avatar 2", 3: "Inside out 2"}
dseats = {}
for i in dmovies:
    dseats[i] = []

while True:
    print("Avalable movies:")
    for i in dmovies:
        print(i, dmovies[i])
    movie = int(input("Enter the movie number you want (0 to exit) "))
    if movie == 0:
        break
    elif movie < 0 or movie > 3:
        print("Invaled input ")
    else:
        book(movie)
