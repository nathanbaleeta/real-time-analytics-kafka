
import json
import time
from confluent_kafka import Producer

from data import get_registered_patient

producer_config = {
    "bootstrap.servers": "localhost:9092",
}

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")


producer = Producer(producer_config)


if __name__ == "__main__":
    while 1 == 1:
        registered_patient = get_registered_patient()
        value = json.dumps(registered_patient).encode("utf-8")
        producer.produce(
            topic="patients",
            value=value,
            callback=delivery_report
        )
        time.sleep(5)

        producer.flush()