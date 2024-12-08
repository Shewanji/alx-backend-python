seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    offset = 0 #start fetching from the beginning
    while True:
        # Fetch a page of users
        users = paginate_users(page_size, offset)
        
        # If no more users are returned, exit the loop
        if not users:
            break
        
        # Yield the current page of users
        yield users
        
        # Increment the offset by page_size for the next fetch
        offset += page_size
