from app.database import engine
# testing connection to supabase
try:
    connection = engine.connect()
    print("Connected successfully!")
    connection.close()

except Exception as e:
    print("Connection failed:")
    print(e)