import logging

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

FORMAT_STRING = (
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s"
)
formatter = logging.Formatter(FORMAT_STRING)
handler.setFormatter(formatter)

logger.addHandler(handler)
