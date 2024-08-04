import json

import logging
import logging_loki

# Create log handlers
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)

loki_handler = logging_loki.LokiHandler(
    url="http://localhost:3100/loki/api/v1/push",
    tags={"application": "streamer"},
    version="1",
)

# Create logger
logger = logging.getLogger("my-logger")
logger.setLevel(logging.INFO)

# logger.addHandler(console_handler)
logger.addHandler(loki_handler)

# logger.error(
#     "Something bad happened",
#     extra={"tags": {"service": "streamer"}},
# )
# logger.warning(
#     "Something bad happened but we can keep going",
#     extra={"tags": {"service": "streamer"}},
# )

# logger.info(
#     "Here's Something to read",
#     extra={"tags": {"service": "streamer"}},
# )
# logger.debug(
#     "Something on purpose",
#     extra={"tags": {"service": "streamer"}},
# )
# logger.info(
#     "processed",
#     extra={
#         "tags": {
#             "DQGateName": "Aize",
#             "DQCheckName": "Columns",
#             "DataChunk": "5",
#             "DatasetId": "2d38346a-63ec-4990-a984-10ab40703368",
#             "Subarea": "C",
#             "MetricValue": "73",
#         }
#     },
# )
# Define the path to the JSON file
file_path = "datasets/MOCK_DATA.json"

# counter = 0
# limit = 5
# Read and print each row in the JSON file
with open(file_path, "r") as file:
    data = json.load(file)
    for row in data:
        # Remove unneeded columns
        # row.pop("DQCheckRunDatetime")
        # row.pop("DatasetId")
        row = {key: str(value) for key, value in row.items()}
        message = row.pop("MetricStatus")
        tags = {**row}

        logger.info(
            message,
            extra={"tags": tags},
        )
        # counter += 1
        # if counter > 1:
        #     break
