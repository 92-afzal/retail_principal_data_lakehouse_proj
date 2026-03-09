# --------------------------------------------------
# Storage Configuration
# --------------------------------------------------

STORAGE_ACCOUNT = "retailsdbw"
CONTAINER = "lakehouse"

BASE_PATH = f"abfss://{CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net"


# --------------------------------------------------
# Catalog & Schemas (Unity Catalog)
# --------------------------------------------------

CATALOG = "dbw_retails"

BRONZE_SCHEMA = f"{CATALOG}.bronze"
SILVER_SCHEMA = f"{CATALOG}.silver"
GOLD_SCHEMA = f"{CATALOG}.gold"
MONITORING_SCHEMA = f"{CATALOG}.monitoring"


# --------------------------------------------------
# Data Lake Paths
# --------------------------------------------------

PATHS = {
    "raw": f"{BASE_PATH}/raw",

    "bronze_eventhub": f"{BASE_PATH}/bronze/eventhub",
    "bronze_files": f"{BASE_PATH}/bronze/files",

    "silver": f"{BASE_PATH}/silver/online_retail",

    "gold_customer": f"{BASE_PATH}/gold/customer",
    "gold_product": f"{BASE_PATH}/gold/product",
    "gold_country": f"{BASE_PATH}/gold/country",

    "monitoring": f"{BASE_PATH}/monitoring"
}


# --------------------------------------------------
# Streaming Checkpoints
# --------------------------------------------------

CHECKPOINTS = {
    "bronze_eventhub": f"{PATHS['bronze_eventhub']}_checkpoint",
    "bronze_files": f"{PATHS['bronze_files']}_checkpoint",
    "silver": f"{PATHS['silver']}_checkpoint"
}


# --------------------------------------------------
# Delta Tables
# --------------------------------------------------

TABLES = {

    # Bronze
    "bronze_eventhub": f"{BRONZE_SCHEMA}.eventhub_transactions",
    "bronze_files": f"{BRONZE_SCHEMA}.file_transactions",

    # Silver
    "silver": f"{SILVER_SCHEMA}.online_retail_transactions",

    # Gold
    "gold_customer": f"{GOLD_SCHEMA}.customer_revenue",
    "gold_product": f"{GOLD_SCHEMA}.product_performance",
    "gold_country": f"{GOLD_SCHEMA}.country_sales"
}


# --------------------------------------------------
# Monitoring Table
# --------------------------------------------------

MONITORING_TABLE = f"{MONITORING_SCHEMA}.pipeline_metrics"