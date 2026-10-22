CATALOG ="dev"
CDC_SCHEMA ="cdc"
GOLD_SCHEMA = "gold"

BRONZE_TABLE = f"{CATALOG}.{CDC_SCHEMA}.bronze_orders_cdc"
SILVER_TABLE = f"{CATALOG}.{CDC_SCHEMA}.orders_current"
GOLD_TABLE = f"{CATALOG}.{GOLD_SCHEMA}.daily_order_metrics"

LANDING_PATH ="/Volumes/dev/cdc/cdc_landing"