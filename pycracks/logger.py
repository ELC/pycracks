import logging

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

format_string = (
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s"
)
formatter = logging.Formatter(format_string)
handler.setFormatter(formatter)

logger.addHandler(handler)
