import do_you_even_math
import player_database2
import sqlite3


def main():
    conn = sqlite3.connect("player.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    player_database2.create_player(cursor)


    print('Welcome to the "Do you even math?" game!')
    print('Here are your options:')
    print('start')
    print('highscores')
    command = input()
    if command == 'highscores':
        player_database2.highscore(cursor)
    elif command == 'start':
        username = input("Input your username: ")
        counter = 1

        while True:
            expression, result = do_you_even_math.make_expression()
            print("Question #{}".format(counter))
            print("What is the answer to: {}".format(expression))
            answer = float(input())
            if answer == result:
                print('Correct!')
                counter += 1
            else:
                score = (counter - 1)*2
                print('Incorrect! Ending game. Your score is: {}'.format(
                    score))
                print('The answer was: {}'.format(result))
                player_database2.add_player(cursor, conn, username, score)
                return False
    else:
        print('Incorrect input!')

if __name__ == '__main__':
    main()
