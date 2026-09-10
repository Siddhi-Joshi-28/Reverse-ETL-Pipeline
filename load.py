import requests
from config import CRM_API_URL

def load_to_crm(transformed_rows):
    """Push transformed data to the destination system (our mock CRM API)."""
    success, failed = 0, 0

    for row in transformed_rows:
        try:
            response = requests.post(CRM_API_URL, json=row)
            if response.status_code == 200:
                success += 1
            else:
                failed += 1
                print(f"[LOAD] Failed for {row['full_name']}: {response.text}")
        except requests.exceptions.ConnectionError:
            print("[LOAD] ERROR: Cannot reach CRM API. Is mock_crm_api.py running?")
            return

    print(f"[LOAD] Done. Success: {success}, Failed: {failed}")

if __name__ == "__main__":
    from extract import extract_customers
    from transform import transform_customers

    raw = extract_customers()
    transformed = transform_customers(raw)
    load_to_crm(transformed)