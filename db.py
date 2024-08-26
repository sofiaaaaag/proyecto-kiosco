import sqlite3

miDB = sqlite3.connect("miDB.db")
cursor = miDB.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS producto (id_producto INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS venta (id_venta INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS proveedor (id_proveedor INTEGER PRIMARY KEY, empresa, fecha ,precio , producto )")
cursor.execute("CREATE TABLE IF NOT EXISTS reporter(id_reporter INTEGER PRIMARY KEY, id_producto, id_venta, id_proveedor, FOREIGN KEY (id_producto) REFERENCES producto (id_producto) FOREIGN KEY (id_venta) REFERENCES venta (id_venta) FOREIGN KEY (id_proveedor) REFERENCES proveedor (id_proveedor) ) ")

cursor.execute("INSERT INTO proveedor (empresa , fecha , precio , producto) VALUES('Rosita','1/7/24','$1000','gaseosas')")

miDB.commit()
