from extract import extract_customers
from transform import transform_customers
from load import load_to_crm

def run_pipeline():
    print("===== REVERSE ETL PIPELINE START =====")
    raw_data = extract_customers()
    transformed_data = transform_customers(raw_data)
    load_to_crm(transformed_data)
    print("===== REVERSE ETL PIPELINE END =====")

if __name__ == "__main__":
    run_pipeline()