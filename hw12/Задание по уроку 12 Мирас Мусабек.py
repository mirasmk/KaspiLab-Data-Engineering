#!/usr/bin/env python
import threading, time
import json 
import datetime
import requests
from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer
from kafka.admin import NewTopic


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        a = 'https://itunes.apple.com/search?term=childish-gambino&limit=1'
        b = requests.get(a).json()
        b["created_at"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print(b["created_at"])
        while not self.stop_event.is_set():
            producer.send('hw12', json.dumps(b).encode('utf-8'))
            time.sleep(1)

        producer.close()


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        consumer.subscribe(['hw12'])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():
    # Create 'my-topic' Kafka topic
    try:
        admin = KafkaAdminClient(bootstrap_servers='localhost:9092')

        topic = NewTopic(name='hw12',
                         num_partitions=1,
                         replication_factor=1)
        admin.create_topics([topic])
    except Exception:
        pass

    tasks = [
        Producer(),
        Consumer()
    ]

    # Start threads of a publisher/producer and a subscriber/consumer to 'my-topic' Kafka topic
    for t in tasks:
        t.start()

    time.sleep(1)

    # Stop threads
    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()
