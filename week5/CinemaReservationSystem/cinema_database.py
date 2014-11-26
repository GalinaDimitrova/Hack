import sqlite3


def create_cinema():
    conn = sqlite3.connect("cinema.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # MOVIES
    create_movies_table(cursor)

    add_movie(cursor, conn, "The Hunger Games: Catching Fire", 7.9)
    add_movie(cursor, conn, "Wreck-It Ralph", 7.8)
    add_movie(cursor, conn, "Her", 8.3)

    # PROJECTIONS
    create_projections_table(cursor)

    add_projectoin(cursor, conn, 1, "3D", '2014-04-01 19:10')
    add_projectoin(cursor, conn, 1, "2D", '2014-04-01 19:00')
    add_projectoin(cursor, conn, 1, "4DX", '2014-04-02 21:00')
    add_projectoin(cursor, conn, 3, "2D", '2014-04-05 20:20')
    add_projectoin(cursor, conn, 2, "3D", '2014-04-02 22:00')
    add_projectoin(cursor, conn, 2, "2D", '2014-04-02 19:30')

    # RESERVATIONS
    create_reservations_table(cursor)

    add_reservation(cursor, conn, "RadoRado", 1, 2, 1)
    add_reservation(cursor, conn, "RadoRado", 1, 3, 5)
    add_reservation(cursor, conn, "RadoRado", 1, 7, 8)
    add_reservation(cursor, conn, "Ivo", 3, 1, 1)
    add_reservation(cursor, conn, "Ivo", 3, 1, 2)
    add_reservation(cursor, conn, "Mysterious", 5, 2, 3)
    add_reservation(cursor, conn, "Mysterious", 5, 2, 4)


def create_movies_table(cursor):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            rating FLOAT)''')


def add_movie(cursor, conn, cur_name, cur_rating):
    cursor.execute('''INSERT INTO movies(name, rating)
                    VALUES(?,?)''',
                   (cur_name, cur_rating))

    conn.commit()


def create_projections_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS projections (
                id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            type VARCHAR,
            date_time DATETIME,
            FOREIGN KEY (movie_id) REFERENCES movies(id))''')


def add_projectoin(cursor, conn, cur_movie_id, cur_type, cur_date_time):
    cursor.execute('''INSERT INTO projections(movie_id, type, date_time)
                    VALUES(?,?,?)''',
                   (cur_movie_id, cur_type, cur_date_time))

    conn.commit()


def create_reservations_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations(
            id INTEGER PRIMARY KEY,
            username VARCHAR,
            projection_id INTEGER,
            row INTEGER,
            col INTEGER,
            FOREIGN KEY (projection_id) REFERENCES projections (id))''')


def add_reservation(cursor, conn, cur_username, cur_projection_id, cur_row, cur_col):
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
        VALUES(?,?,?,?)''',
                   (cur_username, cur_projection_id, cur_row, cur_col))

    conn.commit()


def main():
    create_cinema()


if __name__ == '__main__':
    main()
