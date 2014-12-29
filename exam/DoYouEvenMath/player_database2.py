
def create_player(cursor):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS players (
            username VARCHAR PRIMARY KEY,
            score INTEGER)''')


def add_player(cursor, conn, cur_name, cur_score):
    cursor.execute('''INSERT OR REPLACE INTO players(username, score)
                    VALUES(?,?)''',
                   (cur_name, cur_score))

    conn.commit()


def update_score(cursor, conn, player_name, new_score):
    cursor.execute('''UPDATE players
                        SET score = ?
                        WHERE username LIKE ?
                        '''.format(new_score, player_name))

    conn.commit()


def highscore(cursor):
    cursor.execute('''SELECT username, score
                    FROM players
                    ORDER BY score DESC
                    LIMIT 10''')
    highscores = cursor.fetchall()

    for i, h_score in enumerate(highscores):
        print(
            '{}. {} - score: {}'.format(i + 1,
                                        h_score["username"],
                                        h_score["score"]))


# def check_if_player_exists(cursor, cur_name):
#     cursor.execute('''SELECT EXISTS(SELECT score
#                         FROM players
#                         WHERE username LIKE ?
#                         .format(cur_name))''')
