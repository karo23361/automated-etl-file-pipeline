# Automated ETL File Pipeline

This project is a small, modular ETL pipeline built in Python. Its purpose is to demonstrate how to design a clean, maintainable data workflow that follows common enterprise patterns. The pipeline loads several source files, cleans and transforms the data, validates key fields, and produces a final analytical dataset.

<h2> The codebase is organized into clear layers: </h2>

- extract – reading input files from the configured directory

- transform – cleaning, joining, and preparing the final model

- validation – checking data quality and enforcing basic rules

- load – writing the final output to disk

- logging – capturing the pipeline’s execution details

<h2> How the Pipeline Works </h2>

- Extract - The pipeline reads multiple input files (sales, products, customers, region, reseller). The extractor automatically handles tab‑separated files and reports errors if a file cannot be parsed.

- Transform - The transformation layer merges all datasets into a single model. It also includes cleaning logic, such as converting currency fields from strings (example, $4,049.98) into numeric values and calculating additional metrics like income.

- Validation - The validation module checks for null values in key columns and ensures that numeric fields meet basic conditions. If any rule fails, the pipeline stops and logs the error.

- Load - The final dataset is saved to the output directory defined in the configuration file.

<h2> Databricks Automation </h2>
The pipeline can also be automated in a Databricks environment.
The project repository is connected to Databricks Repos, and a small notebook is used to trigger the Python ETL script. A Databricks Job executes this notebook on a defined schedule, providing orchestration, logging, and monitoring.

<img width="1022" height="592" alt="image" src="https://github.com/user-attachments/assets/38892f47-bd32-4d77-90a1-e488bc3bde44" />


Setup includes:

- Databricks Repo containing the ETL project

- Lightweight notebook that installs dependencies and runs the main Python script

- Databricks Job configured to execute the notebook

- Daily schedule (for example, 06:00)

- Access to input and output directories stored in Databricks Volumes

This approach demonstrates how a local Python ETL can be operationalized in a cloud environment using Databricks Workflows, without the need for additional compute services or external schedulers.
