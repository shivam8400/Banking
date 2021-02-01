import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("browserinvoke")
class BaseClass:
    pass

    def verifypresence(self, XPATH):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, XPATH)))

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler("lofile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s:%(levelname)s%(name)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger


