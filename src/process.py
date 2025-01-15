import logging
import pandas as pd

logger = logging.getLogger(__name__)

def save_to_csv(data, output_path):
 
    if not data:
        logger.warning()
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    logger.info(f"Data saved to {output_path} (rows: {len(df)})")
    