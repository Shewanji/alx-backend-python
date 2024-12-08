seed = __import__('seed')

# Generator function to stream user ages
def stream_user_ages():
    try:
        
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            yield row['age']  
        cursor.close()
    except Exception as err:
        print(f"Error: {err}")
    finally:
        connection.close()
    
# Function to calculate the average age
def calculate_average_age():
    
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No data to calculate average.")
        return
    average_age = total_age / count
    print(f"Average age of users: {average_age}")