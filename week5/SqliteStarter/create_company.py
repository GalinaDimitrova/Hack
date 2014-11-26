import sqlite3


def create_table(conn, cursor):

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            monthly_salary FLOAT,
            yearly_bonus FLOAT,
            position VARCHAR)''')

    cursor.execute('''INSERT INTO company(
        id, name, monthly_salary, yearly_bonus, position)
                    VALUES(?,?,?,?,?)''',
                   (1, 'Ivan Ivanov', 5000, 10000, 'Software Developer'))

    cursor.execute('''INSERT INTO company(
        id, name, monthly_salary, yearly_bonus, position)
                    VALUES(?,?,?,?,?)''',
                   (2, 'Rado Rado', 500, 0, 'Technical Support Intern'))

    cursor.execute('''INSERT INTO company(
        id, name, monthly_salary, yearly_bonus, position)
                    VALUES(?,?,?,?,?)''',
                   (3, 'Ivo Ivo', 10000, 10000, 'CEO'))

    cursor.execute('''INSERT INTO company(
        id, name, monthly_salary, yearly_bonus, position)
                    VALUES(?,?,?,?,?)''',
                   (4, 'Petar Petrov', 3000, 1000, 'Marketing Manager'))

    cursor.execute('''INSERT INTO company(
        id, name, monthly_salary, yearly_bonus, position)
                    VALUES(?,?,?,?,?)''',
                   (5, 'Maria Georgieva', 8000, 10000, 'COO'))

    conn.commit()


def list_employees(cursor):
    all_rows = cursor.execute('''SELECT id, name, position FROM company''')

    for row in all_rows:
        print('{} - {} - {}'.format(row["id"], row["name"], row["position"]))


def monthly_spending(cursor):
    cursor.execute(
        '''SELECT  SUM(monthly_salary) AS monthly_spending FROM company''')
    result = cursor.fetchone()

    return result["monthly_spending"]


def yearly_spending(cursor):
    yearly_spending = 0
    yearly_spending += 12 * monthly_spending(cursor)
    return yearly_spending


def add_employee(cursor, conn):
    new_id = input("id> ")
    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")

    cursor.execute('''INSERT INTO company(
        id, name, monthly_salary, yearly_bonus, position)
                    VALUES(?,?,?,?,?)''',
                   (new_id, name, monthly_salary, yearly_bonus, position))

    conn.commit()


def delete_employee(cursor, conn,  empl_id):
    cursor.execute('''DELETE FROM company WHERE id = ?''', (empl_id,))

    conn.commit()


def update_employee(cursor, conn, empl_id):
    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")

    cursor.execute('''UPDATE company
        SET  name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
        WHERE id = ?''',
                   (name, monthly_salary, yearly_bonus, position, empl_id,))

    conn.commit()


def main():
    conn = sqlite3.connect("create_company.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    command = input("Enter a command> ")
    lst = command.split(" ")
    while lst[0] != "exit":
        if lst[0] == "list_employees":
            list_employees(cursor)
        if lst[0] == "monthly_spending":
            print(monthly_spending(cursor))
        if lst[0] == "yearly_spending":
            print(yearly_spending(cursor))
        if lst[0] == "add_employee":
            add_employee(cursor, conn)
        if lst[0] == "update_employee":
            update_employee(cursor, conn, lst[1])
        if lst[0] == "delete_employee":
            delete_employee(cursor, conn, lst[1])
        command = input("Enter a command> ")
        lst = command.split(" ")


if __name__ == '__main__':
    main()
