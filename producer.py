
import json
import time
from confluent_kafka import Producer

from data import get_registered_patient

producer_config = {
    "bootstrap.servers": "localhost:9092",
}

producer = Producer(producer_config)



if __name__ == "__main__":
    while 1 == 1:
        registered_patient = get_registered_patient()
        value = json.dumps(registered_patient).encode("utf-8")
        producer.produce(
            topic="patients",
            value=value
        )
        time.sleep(5)

    producer.flush()