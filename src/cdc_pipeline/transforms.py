from pyspark.sql import DataFrame
from pyspark.sql.functions import to_date, count, sum as _sum

def aggregate_by_status(df : DataFrame)-> DataFrame:
    retun (
        df.WithColumn("order_date", to_date("updated_at"))
        .groupBy("order_date", "status")
        .agg(
            count("*").alias("order_count"), 
            _sum("amount").alias("total_amount")
        )
    )