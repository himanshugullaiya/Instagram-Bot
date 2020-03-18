from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Instagram:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
        self.driver.get("http://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_name("username").send_keys("himanshugullaiya@gmail.com")
        self.driver.find_element_by_name("password").send_keys("Hunny@123!")
        self.driver.find_element_by_xpath('//button[@type="submit"]').send_keys(Keys.RETURN)
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{'himanshugullaiya'}')]")[0].click()

    
    def get_unfollowers(self, followers, following):
#        followers = set(self.get_followers())
#        following = self.get_following()
        followers = set(followers)
        following_set = set(following)
        
        
        mutual = followers & following_set
        final = list(following_set - mutual)
        final.sort(key = lambda i: following.index(i))
        
        indices = []
        nxt = 0
        for x in range(len(following)):
            if final[nxt] == following[x]:
                indices.append(x)
                nxt += 1
        
        output = dict(zip(indices,final))
        return output
        
    
    def get_followers(self):
        sleep(2)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{'himanshugullaiya/followers'}')]")[0].click()
        names = self.get_names()
        return names
    
    def get_following(self):
        sleep(2)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{'himanshugullaiya/following'}')]")[0].click()
        names = self.get_names()
        return names
    
    def get_names(self):
        sleep(2)
        self.box_path = "/html/body/div[4]/div/div[2]"
        self.scroll_box = self.driver.find_element_by_xpath(F"{self.box_path}")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, self.scroll_box)
        links = self.scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")[0].click()  # close the box
        return names
    
    def remove_unfollowers(self, indices):
        sleep(2)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{'himanshugullaiya/following'}')]")[0].click()
#        try:
#            buttons = self.scroll_box.find_elements_by_tag_name('button')
#        except:
        sleep(2)
        self.box_path = "/html/body/div[4]/div/div[2]"
        self.scroll_box = self.driver.find_element_by_xpath(F"{self.box_path}")

        buttons = self.scroll_box.find_elements_by_tag_name('button')   
        
        count = 0
        for x in range(len(indices)):
            buttons[indices[x] - count].click()
            sleep(1)
            self.scroll_box.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
            sleep(2)
            
    def brute_followers(self, client_id):
        client_id = 'samyukth18'
        mybot.driver.find_element_by_css_selector("input[type = 'text']").send_keys(client_id)
        mybot.driver.find_elements_by_xpath(f"//a[contains(@href,'/{client_id}')]")[0].click()
        mybot.driver.find_elements_by_xpath(f"//a[contains(@href,'/{client_id}/following/')]")[0].click()
        
        
        
            
        
            
        
 
mybot = Instagram()
followers = mybot.get_followers()
following = mybot.get_following()
ego = mybot.get_unfollowers(followers, following)
print(ego)
#mybot.remove_unfollowers([8,10,12,37,48])
 

         
#{1:'abhiiiii_28' , 4:'rahulbeniwal_300' , 6:'divyasharma0505' , 8:'namrata.valecha' , 9:'arjun_joon' , 10:'_jain_lakshay' , 12:'himanshupanwar07' , 13:'iamgunjankataria' , 14:'sharad6578' , 16:'rachit7994' , 17:'adityaxrajput' , 21:'eshita.mann' , 27:'ishan.shivanand' , 28:'shiv_yog' , 35:'ayu.shittin.me' , 38:'verma__nandni' , 45:'shobhna_barua' , 55:'praneshnrocks' , 57:'ravi_sanwal' , 70:'bhavyanshsrivastava' , 71:'mensutra' , 89:'jenn__dennis' , 90:'paulpavitra' , 91:'__rocketman___' , 93:'sadhguru' , 94:'jayshetty' , 95:'entrepreneurmindset.official' , 106:'spiritual.healers' , 111:'verma_kajal7'}
##
##
#driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
#driver.get("http://www.instagram.com")
#sleep(2)
#driver.find_element_by_name("username").send_keys("himanshugullaiya@gmail.com")
#driver.find_element_by_name("password").send_keys("Hunny@123!")
#driver.find_element_by_xpath('//button[@type="submit"]').send_keys(Keys.RETURN)
#sleep(2)
#driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#
#driver.find_elements_by_xpath(f"//a[contains(@href,'/{'himanshugullaiya'}')]")[0].click()
#sleep(1)
#
#
#def ttry():
#    global driver
#    driver.find_elements_by_xpath(f"//a[contains(@href,'/{'himanshugullaiya/following'}')]")[0].click()
#    sleep(1)
#    box_path = "/html/body/div[4]/div/div[2]"
#    scroll_box = driver.find_element_by_xpath(F"{box_path}")
#    last_ht, ht = 0, 1
#    while last_ht != ht:
#        last_ht = ht
#        sleep(1)
#        ht = driver.execute_script("""
#            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
#            return arguments[0].scrollHeight;
#            """, scroll_box)
#    links = scroll_box.find_elements_by_tag_name('a')
#    return (scroll_box,links)
#
#
##names = [name.text for name in links if name.text != '']
#
##scroll_box.find_elements_by_xpath("//a[contains(@href,'/{'himanshugullaiya'}')]"))
##a = links[3]
##a.text
#
#scroll_box,links = ttry()
##driver.execute_script("window.history.go(-1)")
#
#bts = scroll_box.find_elements_by_tag_name('button')
#rmv_shvg = bts[1]
#rmv_shvg.click()
#scroll_box.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()