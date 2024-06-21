import logging


logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info("This is my new Plugin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")