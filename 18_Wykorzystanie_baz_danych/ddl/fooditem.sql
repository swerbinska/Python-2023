SET search_path TO public ;

# ten plik importowalismy do oprogramowania pgAdmin do naszej bazy danych


CREATE TABLE IF NOT EXISTS public.fooditem   #to do pozycji 15 tworzy nam tabele
(
    id SERIAL NOT NULL PRIMARY KEY,
    name character varying(64)  NOT NULL,
    price NUMERIC(6, 2)  NOT NULL
);

INSERT INTO fooditem(name, price) VALUES ('Pizza', 23.0); #nie musimy podawac id bo jest jako serial zdefiniowane czyli bedzie kolejne numery
INSERT INTO fooditem(name, price) VALUES ('Sushi', 60.0);
INSERT INTO fooditem(name, price) VALUES ('Pasta', 40.0);


CREATE TABLE IF NOT EXISTS public.customer #teraz tworzymy tabele klientów do 25 linijki
(
    id SERIAL NOT NULL PRIMARY KEY,
    name character varying(64)  NOT NULL
);

INSERT INTO customer(name) VALUES ('Michal');
INSERT INTO customer(name) VALUES ('Ala');


CREATE TABLE IF NOT EXISTS public.orders #to kolejna tabela - zamówienia
(
    id SERIAL NOT NULL PRIMARY KEY,
    customer_id INT NOT NULL, #relacja jeden do wielu
    created_at TIMESTAMPTZ DEFAULT Now(),
    CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customer(id) #tu wlasnie ta relacja ze klucz klienta jest foreign króty odnosi sie do klucza kastomer id
);

INSERT INTO orders(customer_id) VALUES (1); #wkladamy zamowienia
INSERT INTO orders(customer_id) VALUES (2);

CREATE TABLE IF NOT EXISTS public.orders_item #definiujemy jakie moga byc rodzaje produktow w zamowieniach
(
    id SERIAL NOT NULL PRIMARY KEY,
    orders_id INT NOT NULL,
    fooditem_id INT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT Now(),
    CONSTRAINT fk_orders FOREIGN KEY(orders_id) REFERENCES orders(id), #i tu znowu tworzylismy relacje pomiedzy rodzajem produktu a zamowieniem id
    CONSTRAINT fk_fooditem FOREIGN KEY(fooditem_id) REFERENCES fooditem(id)
);


INSERT INTO orders_item(orders_id, fooditem_id) VALUES (1,1);
INSERT INTO orders_item(orders_id, fooditem_id) VALUES (1,2);
INSERT INTO orders_item(orders_id, fooditem_id) VALUES (2,3);
