import logging
from .basic_selenium_actions import take_screenshot

logging.basicConfig(
    filename='automation.log',
    level = logging.INFO,
    format ='%(asctime)s - %(levelname)s - %(message)s'
)

def continue_on_failure(driver, function, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e: 
        logging.error(e)
        take_screenshot(driver)   
        
def ignore_erorr(driver, function, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e: 
        logging.info(e)   
        take_screenshot(driver)

def expect_error(driver, func, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.info("Expected error occured:", str(e))
        take_screenshot(driver)
    else:
        raise AssertionError("Expected error not raised.")        
    take_screenshot(driver)
