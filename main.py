import time
from config import settings

from elasticsearch import Elasticsearch

import psycopg2

# Elastic Url
es = Elasticsearch(settings.ES_URL)

# Index name
index = settings.INDEX

# Connect to postgresql
conn = psycopg2.connect(
    host=settings.PG_HOST,
    port=settings.PG_PORT,
    user=settings.PG_USER,
    password=settings.PG_PASSWORD,
    database=settings.PG_DATABASE_NAME
)

cursor = conn.cursor()


# Retreive data from es
# TODO: add timestamp filter

def search_es_insert_pg(index, es):
    print('Searching Es...')
    hits = es.search(index=index, 
                    query={"match_all":{}}, 
                    size=400000)['hits']['hits']
    
    print('Inserting to postgres...')
    for hit in hits:
        source = hit['_source']

        try:
            cursor.execute(
                """INSERT INTO TEST(id,price,brand,model,year,title_status,mileage,color,vin,lot,state,
                country,condition,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (source['id'],source['price'],source['brand'],source['model'],source['year'],
                source['title_status'],source['mileage'],source['color'],source['vin'],source['lot'],
                source['state'],source['country'],source['condition'],source['@timestamp'],)
            )
        except Exception as e:
            print('Error', e)

    conn.commit()
    cursor.close()
    conn.close()
    

start_time = time.time()

print('Operation Started')

search_es_insert_pg(index, es)

end_time = time.time()

print('Operation FInished in : ', end_time - start_time)
