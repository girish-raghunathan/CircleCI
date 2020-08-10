import psycopg2
import unittest

# This class encapsulates the application configurations.
class AppConfig:
    # Class Members.

    def __init__(self):
        self.str_db_server = "weather-data.cbx9czxh1e7y.ap-south-1.rds.amazonaws.com"
        self.str_database = "weather_data"
        self.str_db_user = "postgres"
        self.str_db_user_password = "Casio80#"


# This class encapsulates the city entity.
class City:

    # Constructor.
    def __init__(self):
        self.db_config = AppConfig()

        self.city_list = []
        self.obj_db_connection = psycopg2.connect(
            host= self.db_config.str_db_server,
            database=self.db_config.str_database,
            user=self.db_config.str_db_user,
            password=self.db_config.str_db_user_password
        )

    # get the list of cities.
    def get_cities(self):
        # Declare a cursor.

        cities_cur = self.obj_db_connection.cursor()

        # Execute the query and fetch the cities.
        cities_cur.execute("SELECT city_name,state,country FROM city")

        self.city_list = cities_cur.fetchall()

        for indx in range(0,len(self.city_list)):
            print(self.city_list[indx])

        cities_cur.close()
        # Finally, close it.
        self.obj_db_connection.close()


class TestSuite(unittest.TestCase):

    def test_country_count(self):
        cities = City()
        cities.get_cities()
        self.assertEqual(len(cities.city_list), 1005)

    def test_check_for_city(self):
        cities = City()
        cities.get_cities()
        for indx in range(0,len(cities.city_list)):
            self.assertEqual(cities.city_list[0][0],'Chennai')
            break

if __name__ == '__main__':
    unittest.main()