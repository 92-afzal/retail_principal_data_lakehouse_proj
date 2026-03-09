# Azure Databricks Lakehouse Project

## Online Retail Data Pipeline (Bronze • Silver • Gold)

This project demonstrates how to build a modern **data lakehouse
architecture on Azure using Databricks and Unity Catalog**.

The pipeline ingests a raw dataset (`online_retail.csv`), stores it in
**Azure Data Lake Storage Gen2**, and processes it using the **Medallion
Architecture**:

Bronze → Silver → Gold

The project showcases core **data engineering skills**:

• Azure resource provisioning\
• Data lake storage design\
• Unity Catalog governance\
• External storage configuration\
• PySpark data ingestion\
• Delta Lake tables\
• SQL analytics

------------------------------------------------------------------------

# Architecture

                    +-----------------------+
                    |   Source Dataset      |
                    |   online_retail.csv   |
                    +-----------+-----------+
                                |
                                v
                     +-----------------------+
                     | Azure Data Lake Gen2  |
                     |   Storage Account     |
                     +-----------+-----------+
                                 |
                                 v
                           +------------+
                           | Unity      |
                           | Catalog    |
                           +-----+------+
                                 |
                                 v
                           +------------+
                           | Databricks |
                           |  Compute   |
                           +-----+------+
                                 |
                                 v
            +-------------------------------------------+
            | Medallion Architecture                    |
            |                                           |
            | Bronze → Raw Data                         |
            | Silver → Cleaned & Structured Data        |
            | Gold   → Business Aggregations            |
            +-------------------------------------------+

------------------------------------------------------------------------

# Tech Stack

  Technology                     Purpose
  ------------------------------ ----------------------
  Azure Resource Group           Resource management
  Azure Data Lake Storage Gen2   Data storage
  Azure Databricks               Data processing
  Unity Catalog                  Governance
  Delta Lake                     Reliable data format
  PySpark                        Data processing
  SQL                            Analytics queries

------------------------------------------------------------------------

# Dataset

Online Retail Dataset

Columns:

  Column        Description
  ------------- ---------------------
  InvoiceNo     Invoice number
  StockCode     Product code
  Description   Product description
  Quantity      Quantity purchased
  InvoiceDate   Purchase timestamp
  UnitPrice     Item price
  CustomerID    Customer identifier
  Country       Customer country

Derived metric:

Revenue = Quantity \* UnitPrice

------------------------------------------------------------------------

# Azure Storage Structure

Container:

    lakehouse

Folder structure:

    lakehouse/

    bronze/
        online_retail/

    silver/
        retail_clean/

    gold/
        analytics/

------------------------------------------------------------------------

# Databricks Catalog Structure

    retail_dbw

        retail

            bronze_online_retail
            silver_retail_clean
            gold_sales_summary

------------------------------------------------------------------------

# Medallion Architecture

## Bronze Layer

Raw ingestion layer.

Characteristics:

• raw CSV ingestion\
• minimal transformation\
• full historical data

Example:

    retail_dbw.retail.bronze_online_retail

------------------------------------------------------------------------

## Silver Layer

Cleaned dataset.

Typical transformations:

• remove duplicates\
• fix null values\
• correct data types

Example:

    retail_dbw.retail.silver_retail_clean

------------------------------------------------------------------------

## Gold Layer

Analytics-ready data.

Example metrics:

• revenue by country\
• monthly sales trends\
• top products

Example:

    retail_dbw.retail.gold_sales_summary

------------------------------------------------------------------------

# Pipeline Flow

    CSV Dataset
         |
         v
    Bronze Ingestion (PySpark)
         |
         v
    Silver Transformations
         |
         v
    Gold Aggregations
         |
         v
    Analytics / Dashboards

------------------------------------------------------------------------

# PySpark Ingestion Example

``` python
df = spark.read.format("csv")     .option("header","true")     .option("inferSchema","true")     .load("abfss://lakehouse@retailsbucket.dfs.core.windows.net/bronze/online_retail/online_retail.csv")

df.write.format("delta")     .mode("overwrite")     .saveAsTable("retail_dbw.retail.bronze_online_retail")
```

------------------------------------------------------------------------

# Example SQL Query

Top revenue generating countries:

``` sql
SELECT
Country,
SUM(Quantity * UnitPrice) AS Revenue
FROM retail_dbw.retail.silver_retail_clean
GROUP BY Country
ORDER BY Revenue DESC;
```

------------------------------------------------------------------------

# Screenshots Section (for GitHub)

Create folder:

    /images

Recommended screenshots:

• Azure resource group\
• Storage account container structure\
• Databricks cluster setup\
• Unity Catalog configuration\
• Bronze table preview\
• SQL query results

Example:

    ![Architecture](images/architecture.png)

------------------------------------------------------------------------

# 4 Day Project Plan

## Day 1

Azure Setup

• Create Resource Group\
• Create Storage Account\
• Enable Data Lake Gen2\
• Create container\
• Upload dataset

## Day 2

Databricks Setup

• Create Databricks workspace\
• Create compute cluster\
• Enable Unity Catalog\
• Create catalog

## Day 3

Security Configuration

• Create Databricks Access Connector\
• Assign IAM roles\
• Create storage credential\
• Create external location

## Day 4

Data Engineering

• Create schema\
• Create bronze table\
• Ingest CSV data\
• Build silver transformations\
• Create gold analytics tables

------------------------------------------------------------------------

# Learning Outcomes

After completing this project you will understand:

• Azure Data Lake architecture\
• Databricks workspace setup\
• Unity Catalog governance\
• External storage integration\
• PySpark data pipelines\
• Medallion architecture design

------------------------------------------------------------------------

# Future Improvements

Possible upgrades:

• Streaming ingestion using Auto Loader\
• Incremental pipelines\
• Data quality checks\
• Databricks workflows scheduling\
• Power BI dashboards

------------------------------------------------------------------------

# Author

Azure Databricks Lakehouse Project
