import rasterio
import numpy as np
import logging

def calculate_ndvi_statistics(tif_file):
    try:
        with rasterio.open(tif_file) as src:
            data = src.read(1) / 10000
            return {
                "mean_ndvi": float(np.mean(data)),
                "min_ndvi": float(np.min(data)),
                "max_ndvi": float(np.max(data))
            }
    except Exception as e:
        logging.error("NDVI calculation failed: %s", e)
        raise