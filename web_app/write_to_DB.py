import geopandas as gpd
import psycopg2
from sqlalchemy import create_engine

def write2db(input,output):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="web_db")
        connection.autocommit = True
        cursor = connection.cursor()

        query = """
                INSERT INTO transform_data(input_1, input_2, input_3, output_1, output_2, output_3)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
        cursor.execute(query, (input[0], input[1], input[2], output[0], output[1], output[2]))
       
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


#Sample input and output
input = [56,21,37]
output = [45,55,67]

write2db(input,output)


