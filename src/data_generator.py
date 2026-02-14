import pandas as pd
from faker import Faker
import os

fake = Faker('en_GB')

def generate_clinical_data(num_records=50):
    print(f"Generating {num_records} UK clinical records...")
    data = []

    for _ in range(num_records):
        name = fake.name()
        city = fake.city()
        phone = fake.phone_number()

        #mocking a clinical note that contains sensitive information
        note = f"Patient {name} from {city} (Contact: {phone}) shows symptoms of {fake.word()}."

        data.append({
            "Patient_ID": fake.uuid4()[:8],
            "Full_name": name,
            "Contact_Number": phone,
            "Clinical_Note": note
        })
    
    #save to the data folder
    df = pd.DataFrame(data)
    output_path = os.path.join('data', 'mock_patients.csv')
    df.to_csv(output_path, index=False)
    print(f"Success! raw data saved to: {output_path}")

if __name__ == "__main__":
    generate_clinical_data(50)