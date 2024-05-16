import pytest
from library.basic_selenium_actions import *


@pytest.fixture(scope="session")
def setup(request):
    driver = open_browser("https://www.saucedemo.com/")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
        
    yield driver    
    driver.close()