def transform_customers(raw_rows):
    """Convert raw DB rows into the shape our destination (CRM) expects."""
    transformed = []

    for row in raw_rows:
        full_name = f"{row['first_name']} {row['last_name']}"

        # simple business rule: segment customers by spend
        if row['total_purchase'] >= 10000:
            segment = "VIP"
        elif row['total_purchase'] >= 1000:
            segment = "Regular"
        else:
            segment = "New"

        transformed.append({
            "crm_id": row["customer_id"],
            "full_name": full_name,
            "email": row["email"],
            "phone": row["phone"],
            "segment": segment,
            "lifetime_value": float(row["total_purchase"]),
            "joined": str(row["signup_date"]),
        })

    print(f"[TRANSFORM] Transformed {len(transformed)} rows")
    return transformed

if __name__ == "__main__":
    from extract import extract_customers
    raw = extract_customers()
    result = transform_customers(raw)
    for r in result:
        print(r)