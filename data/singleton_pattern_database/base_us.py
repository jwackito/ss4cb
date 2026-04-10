class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to the database...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def get_data(self):
        return "Returning data from unique connection"
