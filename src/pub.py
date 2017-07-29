from confluent_kafka import Producer
import json

with open('data/data.json') as data_file:    
    mydata = json.load(data_file)

p = Producer({'bootstrap.servers': '192.168.99.100:9092'})
for data in mydata:
    airline = data['airline']
    data['airline_alias'] = airline['alias']
    data['airline_iata'] = airline['iata']
    data['airline_id'] = airline['id']
    data['airline_name'] = airline['name']
    data.pop('airline')
    data.pop('_id')
    print('Producing Kafka Message: %s' % data)
    p.produce('topic_json', json.dumps(data))
p.flush()

