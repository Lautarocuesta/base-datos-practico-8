import mysql.connector
# Establecer conexión
mydb = mysql.connector.connect(
host="lbsvzgmk3cbvvo7kj4bv6-mysql.services.clever-cloud.com",
user="uecthfdb0qn8ywtr",
password="N83AhOhayzJEFuibLCeJs",
database="bsvzgmk3cbvvo7kj4bv6"
)
# Crear un cursor
mycursor = mydb.cursor()
# Ejecutar consulta
mycursor.execute("SELECT * FROM mi_tabla")
# Obtener resultados
resultados = mycursor.fetchall()
# Iterar sobre los resultados
for fila in resultados:
    print(fila)
# Cerrar conexión
mydb.close()