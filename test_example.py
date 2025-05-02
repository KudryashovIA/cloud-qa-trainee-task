import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ExampleDotComTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Настройка WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.wait = WebDriverWait(cls.driver, 5)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_example_redirect(self):
        driver = self.driver
        wait = self.wait

        driver.get("https://example.com")
        # Проверка заголовка
        self.assertIn("Example", driver.title, "заголовок страницы не содержит 'Example'")

        # Поиск ссылки и проверка текста

        ''' 
        В стандартном CSS нет возможности напрямую искать элементы по текстовому содержимому, но есть возможность в XPath:

        link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'More information')]")))

        Поэтому поиск по CSS-селектору, содержащему текст "More information" представлен ниже
        '''
        
        link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='https://www.iana.org/domains/example']")))
        self.assertIn("More information", link.text, "Ссылка не содержит текст 'More information'")
        link.click()

        # 4. Проверка редиректа
        self.assertEqual(driver.current_url, "https://www.iana.org/domains/example",
            "Перешли на страницу с URL отличным от 'https://www.iana.org/domains/example'"
        )

if __name__ == "__main__":
    unittest.main()
