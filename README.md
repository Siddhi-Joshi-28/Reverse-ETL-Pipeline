# Reverse ETL Pipeline (Practice Project)

A hands-on practice project to understand how a **Reverse ETL pipeline** works — moving data *out* of a database (like a data warehouse) and pushing it into an external system (like a CRM), instead of the usual ETL direction (source → warehouse).

Built with **PostgreSQL (pgAdmin4)** as the source and a **mock CRM API (Flask)** as the destination, using static/stable sample data first before moving to live data.

---

## What is Reverse ETL?

- **ETL**: pulls data from operational systems → loads it into a data warehouse/database.
- **Reverse ETL**: pulls data *from* the warehouse/database → pushes it *out* into business tools (CRM, marketing platform, support tool, etc.) so non-technical teams can use it.

This project simulates that second flow.

---

## Architecture

```
PostgreSQL (source)  --extract-->  transform.py  --load-->  Mock CRM API (destination)
   [customers table]                (reshape data)              [Flask app]
```

---

## Project Structure

```
reverse-etl-pipeline/
├── .env                   # DB credentials & API URL (not committed to git)
├── .gitignore
├── requirements.txt
├── README.md
├── config.py               # loads environment variables
├── db/
│   └── source_setup.sql    # creates source table + static sample data
├── extract.py               # pulls data from PostgreSQL
├── transform.py             # reshapes/cleans data for the destination
├── mock_crm_api.py          # fake destination system (simulated CRM)
├── load.py                  # pushes transformed data to the CRM API
└── main.py                  # runs the full pipeline: extract -> transform -> load
```

---

## Prerequisites

- Python 3.9+
- PostgreSQL + pgAdmin4 installed and running
- pip

---

## Setup

### 1. Clone and install dependencies
```bash
git clone https://github.com/yourusername/reverse-etl-pipeline.git
cd reverse-etl-pipeline
pip install -r requirements.txt
```

### 2. Create the source database
- Open pgAdmin4 and create a database named `reverse_etl_demo`.
- Open the Query Tool and run the script in `db/source_setup.sql`. This creates a `customers` table and inserts 5 sample rows.

### 3. Configure environment variables
Create a `.env` file in the project root:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=reverse_etl_demo
DB_USER=postgres
DB_PASSWORD=your_pgadmin_password
CRM_API_URL=http://127.0.0.1:5000/api/customers
```

---

## Running the Pipeline

You need **two terminals**.

**Terminal 1 — start the mock destination (CRM):**
```bash
python mock_crm_api.py
```
This starts a fake CRM at `http://127.0.0.1:5000`. Keep it running.

**Terminal 2 — run the pipeline:**
```bash
python main.py
```
This will:
1. **Extract** all rows from the `customers` table in PostgreSQL.
2. **Transform** each row — builds `full_name`, assigns a `segment` (VIP / Regular / New) based on `total_purchase`, and reshapes fields to match what the CRM expects.
3. **Load** each transformed record into the mock CRM via a POST request.

### Verify it worked
Open in your browser:
```
http://127.0.0.1:5000/api/customers
```
You should see the transformed customer records that were pushed from PostgreSQL.

---

## Running Individual Stages

Each file can also run on its own for learning/debugging:
```bash
python extract.py      # just prints raw rows from the DB
python transform.py    # extracts + transforms, prints the reshaped data
python load.py          # extracts + transforms + pushes to the CRM
```

---

## Transformation Logic

| Source field | Destination field | Rule |
|---|---|---|
| `first_name` + `last_name` | `full_name` | concatenated |
| `total_purchase` | `segment` | ≥10,000 → VIP, ≥1,000 → Regular, else New |
| `total_purchase` | `lifetime_value` | converted to float |
| `customer_id` | `crm_id` | direct mapping |

---

## Roadmap / Next Steps

- [x] Static data pipeline (extract → transform → load) — **current stage**
- [ ] Add logging to a file (`logs/pipeline.log`)
- [ ] Add incremental sync using a `last_synced_at` column (only push new/changed rows)
- [ ] Replace static data with a live/changing data source
- [ ] Add scheduling (e.g. APScheduler or cron) to run the pipeline automatically
- [ ] Replace the mock CRM with a real destination (e.g. Google Sheets API, Slack, or an actual CRM API)

---

## Tech Stack

- **Python** — pipeline logic
- **PostgreSQL** — source database
- **psycopg2** — PostgreSQL driver
- **Flask** — mock destination API
- **python-dotenv** — environment variable management
- **requests** — HTTP calls to the destination

---

## License

This is a personal learning/practice project.