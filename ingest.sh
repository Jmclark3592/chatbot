# Bash script to ingest data
# This involves scraping the data from the web and then cleaning up and putting in Weaviate.
# Error if any command fails
set -e
curl -O https://langchain.readthedocs.io/en/latest/index.html

python3 ingest.py
