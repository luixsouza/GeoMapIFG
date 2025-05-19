from services.auth_service import get_oauth_session
from services.data_service import request_data
from services.file_service import extract_tar_file, save_to_json
from services.ndvi_service import calculate_ndvi_statistics
from models.polygon import POLYGON_COORDINATES
from config import TAR_FILE, EXTRACT_PATH, TIF_FILE, JSON_FILE

def get_evalscript():
    return """
    //VERSION=3
    function setup() {
        return {
            input: [{ bands: ["S2", "S3"] }],
            output: [
                { id: "default", bands: 1, sampleType: "INT16" },
                { id: "ndvi_image", bands: 3, sampleType: "AUTO" }
            ]
        }
    }
    function evaluatePixel(sample) {
        let NDVI = index(sample.S3, sample.S2);
        const viz = ColorGradientVisualizer.createWhiteGreen(-0.1, 1.0);
        return {
            default: [NDVI * 10000],
            ndvi_image: viz.process(NDVI)
        }
    }
    """

def build_payload():
    return {
        "input": {
            "bounds": {
                "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/4326"},
                "geometry": {"type": "Polygon", "coordinates": [POLYGON_COORDINATES]}
            },
            "data": [{
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z"
                    },
                    "orbitDirection": "DESCENDING"
                }
            }]
        },
        "output": {
            "width": 512,
            "height": 512,
            "responses": [{
                "identifier": "default",
                "format": {"type": "image/tiff"}
            }]
        },
        "evalscript": get_evalscript()
    }

def main():
    try:
        oauth = get_oauth_session()
        payload = build_payload()
        if request_data(oauth, payload):
            extract_tar_file(TAR_FILE, EXTRACT_PATH)
            stats = calculate_ndvi_statistics(TIF_FILE)
            save_to_json(stats, JSON_FILE)
    except Exception as e:
        import logging
        logging.error("Unhandled exception: %s", e)

if __name__ == "__main__":
    main()