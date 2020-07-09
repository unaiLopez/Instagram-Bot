from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        login_button = driver.find_element_by_xpath("//p[@class='izU2O']/a")
        login_button.click()
        time.sleep(3)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        user_pass_elem = driver.find_element_by_xpath("//input[@name='password']")
        user_pass_elem.clear()
        user_pass_elem.send_keys(self.password)
        user_pass_elem.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))
        like = 0
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.find_element_by_xpath("//button/span[@aria-label='Me gusta']").click()
                like += 1
                print("Likes: " + str(like) + " ||| Hashtag: " + hashtag)
                time.sleep(3)
            except Exception as e:
                time.sleep(3)
                print("Like not available.")

if __name__ == "__main__":

    instagramAccount = InstagramBot('your_user', 'your_password')
    instagramAccount.login()

    hashtags = ['tattoo', 'ink', 'art', 'tattos', 'photography', 'tattoworld', 'tattoer', 'tattoed', 'inked']
    [instagramAccount.like_photos(tag) for tag in hashtags]

    instagramAccount.closeBrowser()
