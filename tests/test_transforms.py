import pytest
from pyspark.sql import SparkSession
from cdc_pipeline.transforms import aggregate_by_status

@pytest.fixture(scope="module")
def spark() -> SparkSession:
    return SparkSession.builder.getOrCreate()


def test_aggregate_by_status_groups_correctly(spark):
    data =  [
                ("2025-01-15 09:00:00", "shipped", 10.0),
                ("2025-01-15 14:30:00", "shipped", 20.0),
                ("2025-01-15 16:00:00", "delivered", 30.0),
            ]
    df =spark.createDataFrame(data, ["updated_at", "status", "amount"])
    result = aggregate_by_status(df)
    result = aggregate_by_status(df)
    rows = result.collect()

    assert len(rows) == 2
    shipped_row = next(row for row in rows if row["status"] == "shipped")
    assert shipped_row["order_count"] == 2
        