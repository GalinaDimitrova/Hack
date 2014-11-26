import sqlite3
import ast
import cinema_database


class GiveUpError(Exception):
    pass


def show_movies(cursor):
    cursor.execute('''SELECT * FROM movies ORDER BY rating''')
    all_movies = cursor.fetchall()
    for movie in all_movies:
        print(
            '[{}] - {} ({})'.format(movie["id"],
                                    movie["name"],
                                    movie["rating"]))


def available_seats(cursor, cur_projection_id):
    cursor.execute(
        '''SELECT COUNT(projection_id)
        FROM reservations
        WHERE projection_id
        LIKE ?''', (cur_projection_id,))
    counter = cursor.fetchone()
    avail_seats = 100 - counter[0]
    return avail_seats

# def count_reserved_seats(cursor, cur_projection_id):
#     cursor.execute('''SELECT projection_id FROM reservations ''')
#     projections_id = cursor.fetchall()
#     counter = 0
#     for proj_id in projections_id:
#         if proj_id["projection_id"] == cur_projection_id:
#             counter += 1
#     return counter


def show_movie_projections(cursor, movie_id):
    cursor.execute('''SELECT M.name, P.id, P.movie_id, P.type, P.date_time
        FROM movies M
        INNER JOIN projections P
        ON M.id = P.movie_id
        WHERE M.id = ?
        ORDER BY date_time''', (movie_id,))

    projections = cursor.fetchall()

    print('Projections for movie {}:'.format(projections[0]["name"]))
    for projection in projections:
        print('[{}] - {} ({}) - {} spots available'.format(
            projection["id"],
            projection["date_time"],
            projection["type"],
            available_seats(cursor, projection["id"])))


def create_a_matrix():
    matrix = [["."] * 10 for i in range(10)]
    return matrix


def print_matrix(matrix):
    print('  1 2 3 4 5 6 7 8 9 10')
    for i, elem in enumerate(matrix):
        print(i + 1, ' '.join(elem))


def seats_matrix(cursor, projection_id):
    print("Available seats (marked with a dot):")
    matrix = create_a_matrix()

    cursor.execute('''SELECT row, col
        FROM reservations
        WHERE projection_id = ?''',
                   (projection_id,))
    reserved_seats = cursor.fetchall()
    for seat in reserved_seats:
        matrix[seat["row"] - 1][seat["col"] - 1] = 'X'

    return matrix


def check_valid_seat(seat):
    row = seat[0]
    col = seat[1]
    if row > 0 and row <= 10 and col > 0 and col <= 10:
        return True
    else:
        return False


def check_seat(matrix, seat):
    row = seat[0] - 1
    col = seat[1] - 1

    if matrix[row][col] == 'X':
        return False
    else:
        return True


def mark_seat(matrix, seat):
    row = seat[0] - 1
    col = seat[1] - 1
    matrix[row][col] = 'X'
    print_matrix(matrix)
    return matrix


def chosen_movie(cursor, movie_id):
    cursor.execute('''SELECT name FROM movies WHERE id = ?''',
                   (movie_id,))
    movies = cursor.fetchone()
    print(movies["name"])
    return movies["name"]


def chosen_projection(cursor, projection_id):
    cursor.execute('''SELECT date_time, type
        FROM projections
        WHERE id =?''', (projection_id,))
    projection = cursor.fetchone()
    return projection
####################################################


def give_up_command(cursor, conn, command):
    if command == 'give_up' or command == 'exit':
        raise GiveUpError


def reservation_step_1(cursor, conn):
    name = input("Step 1 (User): Choose name> ")

    give_up_command(cursor, conn, name)

    tickets_number = int(input("Step 1 (User): Choose number of tickets> "))
    give_up_command(cursor, conn, tickets_number)
    print("Current movies: ")
    show_movies(cursor)
    return name, tickets_number


def reservation_step_2(cursor, conn):
    movie_id = input("Step 2 (Movies): Choose a movie> ")
    give_up_command(cursor, conn, movie_id)
    show_movie_projections(cursor, movie_id)
    return movie_id


def reservation_step_3(cursor, conn, tickets_number):
    projection_id = input("Step 3 (Projection): Choose a projection> ")
    give_up_command(cursor, conn, projection_id)

    while available_seats(cursor, projection_id) < tickets_number:
        print("There are less available seats than you want!")
        projection_id = input("Step 3 (Projection): Choose a projection> ")
        give_up_command(cursor, conn, projection_id)

    matrix = seats_matrix(cursor, projection_id)
    print_matrix(matrix)
    return projection_id, matrix


def reservation_step_4(cursor, conn, tickets_number, matrix):
    seats = []
    for i in range(tickets_number):
        command = input("Step 4 (Seats): Choose a seat {}> ".format(i + 1))
        give_up_command(cursor, conn, command)
        seat = ast.literal_eval(command)

        while check_valid_seat(seat) is False:
            print("Lol.. NO!")
            command = input("Step 4 (Seats): Choose a seat {}> ".format(i + 1))
            give_up_command(cursor, conn, command)
            seat = ast.literal_eval(command)

        while check_seat(matrix, seat) is False:
            print("This seat is already taken!")
            command = input("Step 4 (Seats): Choose a seat {}> ".format(i + 1))
            give_up_command(cursor, conn, command)
            seat = ast.literal_eval(command)

        matrix = mark_seat(matrix, seat)
        seats.append(seat)

    return seats


def reservation_step_5(cursor, conn, movie_id, projection_id, seats, name):
    made_reservation(cursor, movie_id, projection_id, seats)

    command = input("Step 5 (Confirm - type 'finalize') >")
    lst = command.split(" ")
    give_up_command(cursor, conn, lst[0])
    if lst[0] == 'finalize':
        finalize_reservation(cursor, conn, name, projection_id, seats)


def made_reservation(cursor, movie_id, projection_id, seats):
    print("This is your reservation:")
    print("Movie: {}".format(chosen_movie(cursor, movie_id)))
    proj = chosen_projection(cursor, projection_id)
    print('Date and Time: {} ({})'.format(proj["date_time"], proj["type"]))
    print('Seats: {}'.format(seats))


def make_reservation(cursor, conn):
    try:
        name, tickets_number = reservation_step_1(cursor, conn)

        movie_id = reservation_step_2(cursor, conn)

        projection_id, matrix = reservation_step_3(cursor, conn, tickets_number)

        seats = reservation_step_4(cursor, conn, tickets_number, matrix)

        reservation_step_5(cursor, conn, movie_id, projection_id, seats, name)

    except GiveUpError:
        print("Error is here")



def finalize_reservation(cursor, conn, name, projection_id, seats):
    # cursor.execute('''SELECT COUNT(id) as counter FROM reservations''')
    # count_id = cursor.fetchone()
    # id = count_id["counter"]

    for seat in seats:
        row = seat[0]
        col = seat[1]
        #id += 1
        cinema_database.add_reservation(
            cursor, conn, name, projection_id, row, col)
        conn.commit()


def cancel_reservation(cursor, conn, name):
    cursor.execute('''DELETE
        FROM reservations
        WHERE username == ?''',
                   (name,))
    conn.commit()


def menu_help():
    print("1 - show_movies - to view all movies!")
    print(
        "2 - show_movie_projections <movie_id> - to view all movie_projections!")
    print(
        "3 - make_reservation - to make reservation! You may break it by typing give-up!")
    print("4 - give-up - gives up the reservation!")
    print(
        "5 - cancel_reservation <name> - disintegrate given person's reservation!")
    print("6 - help  - show a list of learned spells!")
    print("7 - exit - close Pandora's Box before it's too late!")


def menu_choice(cursor, conn, user_choice):
    valid = ['exit',
             'show_movies',
             'show_movie_projections',
             'make_reservation',
             'give_up',
             'finalize']

    if user_choice not in valid:
        print("Invalid command!")
        return


def menu(cursor, conn):
    command = input("Enter a command> ")
    lst = command.split(" ")
    menu_choice(cursor, conn, lst[0])
    while lst[0] != "exit":
        if lst[0] == "show_movies":
            show_movies(cursor)
        if lst[0] == "show_movie_projections":
            show_movie_projections(cursor, lst[1])
        if lst[0] == "make_reservation":
            make_reservation(cursor, conn)
        if lst[0] == "cancel_reservation":
            cancel_reservation(cursor, conn, lst[1])
        if lst[0] == "help":
            menu_help()

        command = input("Enter a command> ")
        lst = command.split(" ")
        menu_choice(cursor, conn, lst[0])


def main():
    conn = sqlite3.connect("cinema.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("1 - show_movies")
    print("2 - show_movie_projections <movie_id>")
    print("3 - make_reservation")
    print("4 - give-up - gives up the reservation!")
    print("5 - cancel_reservation <name>")
    print("6 - help")
    print("7 - exit")

    menu(cursor, conn)


if __name__ == '__main__':
    main()
