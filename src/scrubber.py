import pandas as pd
import os
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

class ClinicalScrubber:
    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
    
    def scrub_text(self, text):
        #analyse PII
        results = self.analyzer.analyze(text=text, language='en', entitites=["PERSON", "PHONE_NUMBER", "LOCATION"])

        #Replace names with patient and mask phones
        operators = {
            "PERSON": OperatorConfig("replace", {"new_value": "[PATIENT_NAME]"}),
            "PHONE_NUMBER": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 8, "from_end": True}),
            "LOCATION": OperatorConfig("replace", {"new_value": "[LOCATION]"}),
        }

        anonymized = self.anonymizer.anonymize(text=text, analyzer_results=results, operators=operators)
        return anonymized.text
    
    def process(self):
        input_p = os.path.join('data', 'mock_patients.csv')
        output_p = os.path.join('data', 'clean_patients.csv')

        if not os.path.exists(input_p):
            print("error: mock_patients.csv not found! run data_generator.py first.")
            return
        
        df = pd.read_csv(input_p)
        print("Scrubbing PII from clinical notes...")
        df['Scrubbed_Note'] = df['Clinical_Note'].apply(self.scrub_text)

        #GDPR practice of dropping original sensitive columns
        df_clean = df[['Patient_ID', 'Scrubbed_Note']]
        df_clean.to_csv(output_p, index=False)
        print(f"Success! clean data saved to {output_p}")

if __name__ == "__main__":
    scrubber = ClinicalScrubber()
    scrubber.process()