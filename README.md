This project is a small, modular ETL pipeline built in Python. Its purpose is to demonstrate how to design a clean, maintainable data workflow that follows common enterprise patterns. The pipeline loads several source files, cleans and transforms the data, validates key fields, and produces a final analytical dataset.

<h2> The codebase is organized into clear layers: </h2>
* extract – reading input files from the configured directory
* transform – cleaning, joining, and preparing the final model
* validation – checking data quality and enforcing basic rules
* load – writing the final output to disk
* logging – capturing the pipeline’s execution details

<h2> How the Pipeline Works </h2>
* Extract - The pipeline reads multiple input files (sales, products, customers, region, reseller). The extractor automatically handles tab‑separated files and reports errors if a file cannot be parsed.
* Transform - The transformation layer merges all datasets into a single model. It also includes cleaning logic, such as converting currency fields from strings (example, $4,049.98) into numeric values and calculating additional metrics like income.
* Validation - The validation module checks for null values in key columns and ensures that numeric fields meet basic conditions. If any rule fails, the pipeline stops and logs the error.
* Load - The final dataset is saved to the output directory defined in the configuration file.

<h2> Scheduling </h2>
On Linux, the pipeline can be scheduled using cron.
Example:
``` 0 6 * * * python /etl/main_etl.py ```
This runs the ETL every day at 06:00.
