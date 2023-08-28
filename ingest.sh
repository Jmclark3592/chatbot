# Bash script to ingest data
# This involves scraping the data from the web and then cleaning up and putting in Weaviate.
# Error if any command fails
set -e
curl -O https://langchain.readthedocs.io/en/latest/index.html
# wget -r -A.html https://langchain.readthedocs.io/en/latest/
# for curl command, this worked: curl -v -L -O https://langchain.readthedocs.io/en/latest/index.html
python3 ingest.py
