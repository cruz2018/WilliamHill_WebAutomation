import unittest
from selenium import webdriver

class Willian(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        # Deleting all cookies, making sure cookie 'cdb' is not present initially
        # cls.driver.delete_all_cookies()

    def test_cookies_added(self):
        cookies_name = 'cdb'
        url_es = "https://sports.williamhill.es/betting/es-es"
        # url_en = "https://sports.williamhill.com/betting/en-gb"

        ### 1. OPEN "http://sports.williamhill.com/betting/en-gb' ###
        print(' 1. OPEN https://sports.williamhill.es/betting/es-es  ')
        self.driver.get(url_es)
        self.driver.implicitly_wait(10)

        ### 2. ASSERT PRESENCE OF COOKIE NOTICE POP-UP ###
        print(' 2. ASSERT PRESENCE OF COOKIE NOTICE POP-UP  ')
        popup = self.driver.find_element_by_class_name('cookie-disclaimer')
        assert popup.is_displayed()
        print('       The cookie notice pop-up is displayed: ', popup.is_displayed())
        button = self.driver.find_element_by_class_name("cookie-disclaimer__button")
        assert button.is_displayed()

        cookies_before = self.driver.get_cookies()
        #cdb_cookie_before = self.driver.get_cookie('cdb')
        #print('Is there a cdb cookie before the cookie button is clicked: ', cdb_cookie_before is not None)
        #assert cdb_cookie_before is None

        assert self.driver.get_cookie('cdb') is None

        ### 3. CLOSE COOKIE NOTICE  ###
        print(' 3. CLOSE COOKIE NOTICE ')
        button.click()
        cookies = self.driver.get_cookies()
        #print(' The number of cookies after cookie button is clicked is: ', len(cookies))

        ### 4. ASSERT PRESENCE OF CDB COOKIE  ###
        print(' 4. ASSERT PRESENCE OF CDB COOKIE ')
        #print((len(cookies) - len(cookies_before) >= 1))
        assert (len(cookies) - len(cookies_before) >= 1)
        #  print('       The number of cookies after cookie button is clicked increased: ',  (len(cookies) - len(cookies_before) >= 1))
        cdb_cookie = self.driver.get_cookie('cdb')
        assert cdb_cookie is not None
        #print('       Is there a cdb cookie after the cookie button is clicked: ', cdb_cookie is not None)
        print('       The new cookie added is: ', cdb_cookie)

    def tearDown(cls):
        cls.driver.quit()
        print('TEST PASSED')









