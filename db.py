import pymysql
# from pymysql.cursors import DictCursor
from config import host, user, password, db_name
from pymysql.cursors import DictCursor

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Super connect")
    print("#" * 20)

    try:
        # cursor = connection.cursor()

        with connection.cursor() as cursor:
            # create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT,"  \
            create_table_query = "CREATE TABLE IF NOT EXISTS `users`(id int AUTO_INCREMENT,"  \
                                 " name varchar(55)," \
                                 " password varchar(10)," \
                                 " email varchar(33), PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            print("We create table")

        with connection.cursor() as cursor:
            insert_query1 = "INSERT INTO `users` (name, password, email) VALUES ('Lol', 'qwerty', 'lol@gmail.com');"
            insert_query2 = "INSERT INTO `users` (name, password, email) VALUES ('Крутяк', 'секрет', 'xxx@gmail.com');"
            cursor.execute(insert_query2)
            cursor.execute(insert_query1)
            connection.commit()

        with connection.cursor() as cursor:
            update_query = "UPDATE `users` SET name = 'MegaLol' WHERE name = 'Lol';"
            cursor.execute(update_query)
            connection.commit()

        with connection.cursor() as cursor:
            delete_query888 = "DELETE FROM `users` WHERE password = 'секрет';"
            cursor.execute(delete_query888)
            connection.commit()


        with connection.cursor() as cursor:
            select_from_user = "SELECT * FROM `users`; "
            cursor.execute(select_from_user)
            row = cursor.fetchall()
            for row in row:
                print(row)
            print("#" * 20)

    finally:
        connection.close()

except Exception as ex:
    print("WOOOOOOOOOOOOOOOOOW")
    print(ex)