import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '123123')

        sql_manager.cursor.execute('''SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)''', 
            ('Dinko', sql_manager.hash_password("123123")))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')


    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')
######################################################################################

    def test_login_sql_injections(self):
        self.assertFalse(sql_manager.login("'or 1 = 1 --", '123'))
        self.assertFalse(sql_manager.login(" or ""=", '123'))
        self.assertFalse(sql_manager.login('123', " or ""="))
        self.assertFalse(sql_manager.login("105; DROP TABLE clients", '123'))

    def test_strong_password(self):
        self.assertFalse(sql_manager.strong_password("32154", "abc"))               #short
        self.assertFalse(sql_manager.strong_password("321544465454546", "abc"))     #ionly digits
        self.assertFalse(sql_manager.strong_password("abauGHKUGdyla", "abc"))       #only characters
        self.assertFalse(sql_manager.strong_password("123abahdgak", "abc"))         #doesn't have uppercase
        self.assertFalse(sql_manager.strong_password("3215HGAKLGS", "abc"))         #doesn't have lowercase
        self.assertFalse(sql_manager.strong_password("1234abc567A", "abc"))          #usernam is a substring
        self.assertFalse(sql_manager.strong_password("1234abfd567A", "abc"))
        self.assertTrue(sql_manager.strong_password("1234abfd567A!", "abc"))

    def test_hash_password(self):
        hashed_pass = sql_manager.hash_password("12345678")
        self.assertEqual(hashed_pass,"7c222fb2927d828af22f592134e8932480637c0d")

if __name__ == '__main__':
    unittest.main()
