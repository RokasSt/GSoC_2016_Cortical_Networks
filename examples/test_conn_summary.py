import json



if __name__=="__main__":


   with open("Traub_conn_data.json",'r') as json_conn:
        conn_data=json.load(json_conn)
        print conn_data[0]['type']
