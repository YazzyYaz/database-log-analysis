import psycopg3
import bleach

DBNAME = "news"

def run_query(query_command):
    """Runs the query on the database"""
    connection = psycopg3.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query_command)
    data = cursor.fetchall()
    connection.close()
    return data

def get_popular_article():
    """Get top 3 most popular articles"""
    query_command = "SELECT * from popular_posts LIMIT 3"
    query_data = run_query(query_command)
    return query_data

def get_popular_authors():
    """Get top 3 most popular authors"""
    query_command = "SELECT * from popular authors LIMIT 3"
    query_data = run_query(query_command)
    return query_data

def find_anomaly():
    """Gets date where 1% of requests return error"""
    query_command = "SELECT day FROM error_log WHERE error_percent > 1.0"
    query_data = run_query(query_command)
    return query_data
