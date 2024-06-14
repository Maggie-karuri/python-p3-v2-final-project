
def get_all_model_1_data():
    from models import execute_query
    query = "SELECT * FROM model_1_table"
    return execute_query(query)

def insert_model_1_data(data):
    from models import execute_query
    query = "INSERT INTO model_1_table (column1, column2, column3) VALUES (?, ?, ?)"
    params = (data['column1'], data['column2'], data['column3'])
    execute_query(query, params)
