from datasets import load_dataset
import pandas as pd
import time
import os

from config import Directory, Config

from src.utils.logger import logger

def load_amazon_reviews():
    logger.info("Starting to load the Amazon Reviews dataset")
    dataset = load_dataset(Config().data_source, Config().product_category, split="full")
    
    # Define the time range for the study period (one month before to one month after)
    before_ai_start = '2023-07-22'
    after_ai_end = '2023-10-21'

    # Convert dates to Unix timestamps
    start_timestamp = int(time.mktime(time.strptime(before_ai_start, '%Y-%m-%d'))) * 1000
    end_timestamp = int(time.mktime(time.strptime(after_ai_end, '%Y-%m-%d'))) * 1000 + 86399000

    logger.info(f"Filtering dataset from {before_ai_start} to {after_ai_end}...")
    logger.info(f"Using Unix timestamps from {start_timestamp} to {end_timestamp}")

    # Filter by time range
    filtered_dataset = dataset.filter(
        lambda example: start_timestamp <= example['timestamp'] <= end_timestamp
    )

    # Convert to list and then DataFrame
    logger.info("Converting filtered dataset to DataFrame...")
    data_list = []
    for item in filtered_dataset:
        data_list.append(item)
        if len(data_list) % 10000 == 0:
            logger.info(f"Processed {len(data_list)} records...")

    df = pd.DataFrame(data_list)
    logger.info(f"Dataset loaded with {len(df)} reviews for the study period")

    logger.info("Writing csv file")
    df.to_csv(os.path.join(Directory.RAW_DATA.value, f"{Config().product_category}.csv"), index=False)
    logger.info("Finished writing csv file")

    return df

if __name__ == "__main__":
    df = load_amazon_reviews()
    print(df.head())
  