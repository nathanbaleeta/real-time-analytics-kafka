import uuid
from faker import Faker

fake = Faker()

def get_registered_patient():
    return {
        "patient_id": str(uuid.uuid4()),
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.date()
    }

if __name__ == "__main__":
    get_registered_patient()
