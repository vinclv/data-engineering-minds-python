from sqlalchemy import create_engine
from sqlalchemy import text
from faker import Faker

def get_db_engine():
    return create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'postgres:5432', 'oltp_db'))

while True:
    try:
        db_engine = get_db_engine().connect()
        if db_engine:
            break
    except Exception as e:
        print(f"++++ Retrying connection to the database because of the issue {str(e)}++++")

i = 0
fake = Faker('en_US')
#for i in range(10):
while True:
    print(f"Inserting record number {i+1}")
    user_id = fake.random_int(min=1, max=200)
    amount = fake.random_int(min=1000, max=10000)
    insert_query = f"INSERT INTO oltp.user_transactions (user_id, amount) VALUES ({user_id}, {amount})"
    db_engine.execute(text(insert_query).execution_options(autocommit=True))
    print(f"Completed inserting record number {i+1}")
    i = i + 1

db_engine.close()

