from unittest import result
import mysql.connector 
from mysql.connector import Error
import zmq

print("Server started")

while True:
    try:
        hostname = '127.0.0.1'
        database = "gkb"
        user = "root"
        password = "root"

        #Establising connection with database
        connection = mysql.connector.connect(host= hostname,
                                            database=database,
                                            user=user,
                                            password = password)

        cursor = connection.cursor()

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")

        message = socket.recv()

        #print(type(message))
        #print(message.decode('UTF-8'))

        order_id = message.decode('UTF-8')

        print("order recieved and ID is " + order_id)
        #Building query
        query = "SELECT Reference, OrderStatus, ReceivedDate FROM orders WHERE AccountNo=" + str(order_id)

        cursor.execute(query)

        #fetchone for now, fetchall gets all the records. 
        results = cursor.fetchall()
        
        for i in range(len(results)):
            results[i] = "&&".join(map(str, results[i]))
        #string_res = str(results[0]) + "." + str(results[1]) + "." + str(results[2])
        string_res = ".".join(map(str, results))
    
    except Exception as e:
        socket.send_string("error occured")
        print(e)
        print("------------------------------------------------------------\n")

    #print(type(results[0]))
    else:
        socket.send_string(string_res)
        print("sent back string ")
        print("------------------------------------------------------------\n")
    
    finally:
        connection.close()




