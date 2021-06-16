from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

i_id = 'Enter Email'
pwd = 'Enter password'
class Instagram:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
        self.driver.get("http://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_name("username").send_keys(i_id)
        self.driver.find_element_by_name("password").send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]').send_keys(Keys.RETURN)
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)
        # self.driver.find_elements_by_xpath(f'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')[0].click()

    
    def get_names(self):
        sleep(2)
        self.scroll()
        links = self.scroll_box.find_elements_by_tag_name('a')
        # print(links)
        names = [name.text for name in links if name.text != '']
        print('Enter q for exit or any other to Continue : ')
        if(input() == 'q'):
            return
        self.driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")[0].click()  # close the box
        return names
    
    
    def scroll(self):
        self.box_path = "/html/body/div[4]/div/div/div[2]"
        self.scroll_box = self.driver.find_element_by_xpath(F"{self.box_path}")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, self.scroll_box)
        print("Out of Scroll Loop")

        
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
            if nxt >= len(final):
                break
        
        output = dict(zip(indices,final))
        return output
        
    
    def get_followers(self):
        sleep(2)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{i_id}/followers/')]")[0].click()
        names = self.get_names()
        return names
    
    def get_following(self):
        sleep(2)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{i_id}/following/')]")[0].click()
        names = self.get_names()
        return names
    
    
    
    def remove_unfollowers(self, indices):
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{'{i_id}/following'}')]")[0].click()
        sleep(1)
        self.scroll()
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
        sleep(int(0.9 * len(indices))) # extend sleep as required
        self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")[0].click()  # close the box
        
        
            
    def scroll_once(self):
        sleep(5)
        self.box_path = "/html/body/div[5]/div/div/div[2]"
        self.scroll_box = self.driver.find_element_by_xpath(F"{self.box_path}")
#        last_ht, ht = 0, 1
#        if last_ht
#            last_ht = ht
#            sleep(1)
        ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, self.scroll_box)
        buttons = self.scroll_box.find_elements_by_tag_name('button')
        print(f"Total Entries Scrolled : {len(buttons)}")
        
        
    def brute_followers(self, index_done = 0, client_id = 'thebusiness.mindset'):
        SCROLLS_TODO = 2
        sleep(3)
        self.driver.find_element_by_css_selector("input[type = 'text']").send_keys(client_id)
        sleep(3)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{client_id}')]")[0].click()
        sleep(5)
        self.driver.find_elements_by_xpath(f"//a[contains(@href,'/{client_id}/followers/')]")[0].click()
        sleep(5)
        self.box_path = "/html/body/div[5]/div/div/div[2]"
        self.scroll_box = self.driver.find_element_by_xpath(F"{self.box_path}")
        
        count = 0
        last_ht, ht = 0, 1
        while (last_ht != ht) and count < ((index_done//15)+SCROLLS_TODO): # one scroll has 13.5 results or 14
            print("inloop")
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, self.scroll_box)
            count += 1
        sleep(2)
        links = self.scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        buttons = self.scroll_box.find_elements_by_tag_name('button')
        
        print(f"Total Entries Scrolled : {len(buttons)}")
        names_requested = []
        
        if(input('Press any button to Continue, or "Q" to Exit') == 'q'):
            return
        
        for x in range(index_done, len(buttons)):
            if buttons[x].text == 'Follow':
                buttons[x].click()
                sleep(2)
                if buttons[x].text == 'Following':
                    buttons[x].click()
                    sleep(2)
                    self.scroll_box.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                else:
                    names_requested.append(names[x])
        
        sleep(int(0.3 *SCROLLS_TODO*15))
#        self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")[0].click()  # close the box
        return (client_id, names_requested, len(buttons))
    
    

        
def search_peeps(elem):
    # mybot.driver.find_element_by_css_selector("input[type = 'text']")
    mybot.driver.find_element_by_css_selector("input[type = 'text']").send_keys(elem)
    sleep(2)
    mybot.driver.find_elements_by_xpath(f"//a[contains(@href,'/{elem}')]")[0].click()

            

 
mybot = Instagram()
index_done = 0
client,names_requested,index_done = mybot.brute_followers(index_done, client_id= 'thebusiness.mindset')  






'''DONT TOUCH CODE INSIDE THIS
#mybot.scroll_once()

# followers = mybot.get_followers()
# following = mybot.get_following()
# ego = mybot.get_unfollowers(followers, following)
# print(ego)


#mybot.remove_unfollowers([39,41,45,50,61,80,84,123])
#ind_to_remove = set(ego.keys())
#ind_not_remove = set([20,21,26,58, 73, 77,80,118,121, 141, 147])
'''






         