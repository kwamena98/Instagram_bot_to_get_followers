from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
import pandas as pd
from time import sleep, strftime



bot=webdriver.Chrome('')#your chrome directory
bot.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
email=bot.find_element_by_name('username')
password=bot.find_element_by_name('password')

email.clear()
password.clear()

email.send_keys('')#Please put your username or email or phone number here
password.send_keys('')# please put your password here
password.send_keys(Keys.RETURN)
time.sleep(6)


home=bot.find_element_by_class_name('_8-yf5')
home.click()

ui.WebDriverWait( bot ,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
time.sleep(5)






hashtag_list = ['']#please put the hashtags here please use commas to separate it

prev_user_list = []
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    bot.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    

    username = bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]').text
            
    if username not in prev_user_list:
                # If we already follow, do not unfollow
        if bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    
                bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                time.sleep(10)
                new_followed.append(username)
                followed += 1

                    # Liking the picture
                button_like = bot.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > svg').click()
                    

                # button_like.click()
                time.sleep(4)
                likes += 1

                #     sleep(randint(18,25))

                #     Comments and tracker
                #     comm_prob = randint(1,10)
                #     print('{}_{}: {}'.format(hashtag, x,comm_prob))
                #     if comm_prob <= 5:

                bot.find_element_by_class_name("Ypffh").click()
                time.sleep(4)
                comment_box = bot.find_element_by_class_name("Ypffh")
                
                                # if (comm_prob  > 1):
                comment_box.send_keys('If you see this comment follow for follow back')
                comments += 1   

                comment_box.send_keys(Keys.ENTER)
                sleep(5)

                # Next picture
                bot.find_element_by_link_text('Next').click()
                
                    
                time.sleep(10)
        else:
                bot.find_element_by_link_text('Next').click()
                sleep(randint(20,26))

    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        # except:
        #     continue


for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
















        

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 



