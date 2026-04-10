class ConexionBaseDeDatos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Conexion a la base de datos...")
            cls._instancia = super(ConexionBaseDeDatos, cls).__new__(cls)
        return cls._instancia

    def conseguir_datos(self):
        return "Rertornando datos desde la conexion unica"
