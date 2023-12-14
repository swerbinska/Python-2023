import psycopg2

connect_string = "dbname=my_database user=my_user password=secret host=127.0.0.1" #to jest info z jakiej bazy ma brac dane; wazne my tu mamy haslo na widoku ale nie powinno tak byc , nie trzymamy hasel w ghicie

stmt = """"
SELECT * from orders
join orders_item on orders_item.orders_id = orders.id
join fooditem on fooditem.id = orders_item.fooditem_id where customer_id=1
"""
stmt2 = 'SELECT COUNT(*) from fooditem;'
with psycopg2.connect(connect_string) as connection: #łączymy się funkcją with po to aby jesli pojawia się błędy to polaczenie zostanie zamkniete, wiec zawsze z withem otwieramy polaczenie do baz danych 
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) from fooditem;') #w tym zadaniu chcemy polaczyc sie z baza i policzyc ile bylo fooditemow
        result = cursor.fetchall() #pobiez dane z bazy danych 
        for row in result: #i kolejne wiersze sa wyciagane 
            print (row)
    except psycopg2.Error as e:
        print(e)