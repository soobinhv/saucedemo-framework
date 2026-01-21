import pytest
import os
import configparser
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# 1. Đọc Config
config = configparser.ConfigParser()
config.read('configurations/config.ini', encoding='utf-8')


@pytest.fixture(scope="function")
def driver(request):
    browser_name = config['app_info']['browser']
    headless_mode = config['app_info'].getboolean('headless')

    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()

        # --- BẮT ĐẦU CẤU HÌNH FIX LỖI POPUP ---

        # 1. Tắt tính năng phát hiện rò rỉ mật khẩu
        options.add_argument("--disable-features=PasswordLeakDetection")

        # 2. Tắt popup "Save Password" và "Change Password"
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2  # Tắt thông báo
        }
        options.add_experimental_option("prefs", prefs)

        # 3. Loại bỏ dòng "Chrome is being controlled by automated test software" (Optional - nhìn cho đẹp)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # --- KẾT THÚC CẤU HÌNH ---

        if headless_mode:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)

    request.node.driver = driver

    yield driver
    driver.quit()


# 2. Hook: Chụp màn hình khi Test Fail
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Lấy driver từ fixture
        driver = getattr(item, "driver", None)
        if driver:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"screenshot_{item.name}_{timestamp}.png"

            # Chụp ảnh và attach vào Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )


# 3. Fixture trả về data config để dùng trong test
@pytest.fixture(scope="session")
def app_config():
    return config