from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import ElementNotVisibleException
options = webdriver.ChromeOptions()

import time
import json

CAPTION = """Sat Saheb ji"""
LOCATION = 'Delhi, India'


# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.webdriver import FirefoxProfile
# options.add_argument("--headless")
options.add_argument(r"--user-data-dir=/home/ankit/.config/google-chrome")

#provide the profile name with which we want to open browser

options.add_argument(r'--profile-directory=Profile 2')
#specify where your chrome driver present in your pc

driver = webdriver.Chrome(options=options)



url = "https://www.instagram.com/"
driver.get(url)
actions = ActionChains(driver)

    

def login():
    username = driver.find_element(By.NAME, 'username')
    paswd = driver.find_element(By.NAME, "password")
    login =driver.find_element(By.CSS_SELECTOR, '._acap')

    with open("/home/ankit/.config/paswd/paswd.json" , 'r') as w:
        cred = json.load(w)

    username.send_keys(cred['instagram_sm']['email'])
    paswd.send_keys(cred['instagram_sm']['password'])
    login.click()


def upload_image(image_path):
    time.sleep(1)

    new_post = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a')
    # print(new_post)
    new_post.click()
    time.sleep(2)
                                            # //*[@id="mount_0_0_GD"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input
    # selectFromComputer = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
    # selectFromComputer.click()
    upload = driver.find_element(By.CSS_SELECTOR, 'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xdl72j9.x1iyjqo2.xs83m0k.x15wfb8v.x3aagtl.xqbdwvv.x6ql1ns.x1cwzgcd div.x6s0dn4.x78zum5.x5yr21d.xl56j7k.x1n2onr6.xh8yej3 form input._ac69')
    upload.send_keys(image_path)

    time.sleep(1)

    resize = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xdl72j9.x1iyjqo2.xs83m0k.x15wfb8v.x3aagtl.xqbdwvv.x6ql1ns.x1cwzgcd div.x6s0dn4.x78zum5.x5yr21d.xl56j7k.x1n2onr6.xh8yej3 div.x6s0dn4.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xln7xf2.xk390pu.x5yr21d.xl56j7k.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 div.x6s0dn4.xnz67gz.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xln7xf2.xk390pu.x5yr21d.xl56j7k.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 div.x6s0dn4.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xln7xf2.xk390pu.x5yr21d.xl56j7k.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.x10l6tqk.x1ey2m1c.x17qophe.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1 div div._abfz._abg1 button._acan._acao._acas._aj1-._ap30')
    resize.click()

    time.sleep(1)

    original_size = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xdl72j9.x1iyjqo2.xs83m0k.x15wfb8v.x3aagtl.xqbdwvv.x6ql1ns.x1cwzgcd div.x6s0dn4.x78zum5.x5yr21d.xl56j7k.x1n2onr6.xh8yej3 div.x6s0dn4.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xln7xf2.xk390pu.x5yr21d.xl56j7k.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 div.x6s0dn4.xnz67gz.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xln7xf2.xk390pu.x5yr21d.xl56j7k.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 div.x6s0dn4.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xln7xf2.xk390pu.x5yr21d.xl56j7k.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.x10l6tqk.x1ey2m1c.x17qophe.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xp3fus3.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.xzkaem6.x1hc1fzr.xnn1q72.x154egtw div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x16n37ib.x150jy0e.x1e558r4.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1')
    original_size.click()

    time.sleep(1)
    input('hekko')
    next_button = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ap97 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1qjc9v5.x78zum5.xdt5ytf div._ac76 div.x6s0dn4.x78zum5.x19l4sor.xdt5ytf.x5yr21d.xl56j7k.x1n2onr6.x1guec7k div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xyamay9.x1pi30zi.x1l90r2v.x1swvt13.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37')
    next_button.click()

    time.sleep(1)

    next_button = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ap97 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1qjc9v5.x78zum5.xdt5ytf div._ac76 div.x6s0dn4.x78zum5.x19l4sor.xdt5ytf.x5yr21d.xl56j7k.x1n2onr6.x1guec7k div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xyamay9.x1pi30zi.x1l90r2v.x1swvt13.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37')
    next_button.click()

    time.sleep(1)

    caption = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x15wfb8v.x3aagtl.x6ql1ns.x78zum5.xdl72j9.x1iyjqo2.xs83m0k.x13vbajr.x1ue5u6n div.xhk4uv.x26u7qi.xy80clv.x9f619.x78zum5.x1n2onr6.x1f4304s div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xmz0i5r.xh8midk.x1rife3k div div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.x12lumcd.xdt5ytf.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x6ikm8r.x1odjw0f.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x6s0dn4.x78zum5.x1n2onr6.xh8yej3 div.xw2csxc.x1odjw0f.x1n2onr6.x1hnll1o.xpqswwc.xl565be.x5dp1im.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1w2wdq1.xen30ot.x1swvt13.x1pi30zi.xh8yej3.x5n08af.notranslate')
    caption.send_keys(CAPTION)

    time.sleep(1)

    # location_label = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x15wfb8v.x3aagtl.x6ql1ns.x78zum5.xdl72j9.x1iyjqo2.xs83m0k.x13vbajr.x1ue5u6n div.xhk4uv.x26u7qi.xy80clv.x9f619.x78zum5.x1n2onr6.x1f4304s div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xmz0i5r.xh8midk.x1rife3k div div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.x12lumcd.xdt5ytf.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x6ikm8r.x1odjw0f.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf div._abgh div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 label.x6s0dn4.x5ur3kl.xopu45v.x1bs97v6.xmo9t06.x1j8ye7u.x1rjkts5.x13z9klp.xjc6cxp.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.x78zum5.x1iyjqo2.xg7h5cd.x1qughib.x1sxyh0.x1n2onr6.xjbqb8w.xzd0ubt')
    # # location_label.send_keys(LOCATION)
    # location = driver.find_element(By.CSS_SELECTOR,'input').send_keys(LOCATION)
    # time.sleep(3)
    # location_new = location_label.find_element(By.CSS_SELECTOR,'input')
    # time.sleep(1)
    
    # script = """
    # arguments[0].setAttribute('class', 'x5ur3kl xopu45v x1bs97v6 xmo9t06 x1j8ye7u x1rjkts5 x13z9klp xjc6cxp x178xt8z xm81vs4 xso031l xy80clv x5n08af x1iyjqo2 xvs91rp xklk4pu xdj266r x11i5rnm xat24cr x1mh8g0r x1plvlek xryxfnj x1s3xk63 xlqc9nw x8tigb1 x1ad04t7 x1glnyev xs3hnx8 x7xwk5j x1rheh84 x1ck6gwh x175bfct x1meze4m x10eltez x1qt4tve x1s07b3s x1rvh84u x1iorvi4 xpvbz4a xjkvuk6 xohu8s8 xh8yej3 x1jguvu7 x15aq7wb xygx6cg xrqayxw x1uvtmcs x1ejq31n xd10rxx x1sy0etr x17r0tee xjbqb8w xzd0ubt xwhw2v2');
    # arguments[0].setAttribute('placeholder', 'Add location');
    # arguments[0].setAttribute('spellcheck', 'true');
    # arguments[0].setAttribute('type', 'text');
    # arguments[0].setAttribute('value', 'Delhi, India');
    # arguments[0].setAttribute('style', '--placeholder-color: rgba(232, 229, 227, 0.6) !important; color: rgb(229, 225, 223) !important;');
    # arguments[0].setAttribute('disabled', '');
    # """
    # input('chnage location')
    # # driver.execute_script("document.getElementsByClassName('html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x15wfb8v.x3aagtl.x6ql1ns.x78zum5.xdl72j9.x1iyjqo2.xs83m0k.x13vbajr.x1ue5u6n div.xhk4uv.x26u7qi.xy80clv.x9f619.x78zum5.x1n2onr6.x1f4304s div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.xmz0i5r.xh8midk.x1rife3k div div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.x12lumcd.xdt5ytf.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x6ikm8r.x1odjw0f.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf div._abgh div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 label.x6s0dn4.x5ur3kl.xopu45v.x1bs97v6.xmo9t06.x1j8ye7u.x1rjkts5.x13z9klp.xjc6cxp.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.x78zum5.x1iyjqo2.xg7h5cd.x1qughib.x1sxyh0.x1n2onr6.xjbqb8w.xzd0ubt input.x5ur3kl.xopu45v.x1bs97v6.xmo9t06.x1j8ye7u.x1rjkts5.x13z9klp.xjc6cxp.x178xt8z.xm81vs4.xso031l.xy80clv.x5n08af.x1iyjqo2.xvs91rp.xklk4pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1plvlek.xryxfnj.x1s3xk63.xlqc9nw.x8tigb1.x1ad04t7.x1glnyev.xs3hnx8.x7xwk5j.x1rheh84.x1ck6gwh.x175bfct.x1meze4m.x10eltez.x1qt4tve.x1s07b3s.x1rvh84u.x1iorvi4.xpvbz4a.xjkvuk6.xohu8s8.xh8yej3.x1jguvu7.x15aq7wb.xygx6cg.xrqayxw.x1uvtmcs.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.xjbqb8w.xzd0ubt').getElementsByTagName('value').setAttribute('value', 'Delhi - Heart of India')")
    # driver.execute_script(script, location_new)
    # # driver.execute_script(f"arguments[0].setAttribute('{'value'}', '{'Delhi, India'}')", location_new)
    # # print('changed')
    # time.sleep(0.5)

    # input('changing location')
    # share = driver.find_element(By.CSS_SELECTOR,'html._9dls._ar44.js-focus-visible._aa4d body._ar45.system-fonts--body div.x1n2onr6.xzkaem6 div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.xippug5.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6 div.xs83m0k.x1sy10c2.x1h5jrl4.xieb3on.xmn8rco.x1iy3rx.x1n2onr6 div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe div div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x6ikm8r.x10wlt62.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ap97 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1qjc9v5.x78zum5.xdt5ytf div._ac76 div._ac7b._ac7d div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xyamay9.x1pi30zi.x1l90r2v.x1swvt13.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37')
    # share.click()
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div > div.xdl72j9.x1iyjqo2.xs83m0k.x15wfb8v.x3aagtl.xqbdwvv.x6ql1ns.x1cwzgcd > div.x6s0dn4.x78zum5.x5yr21d.xl56j7k.x1n2onr6.xh8yej3 > div > div:nth-child(2) > div > span")))
    actions.send_keys(Keys.ESCAPE)
    actions.perform()
    input('done file uploader')

# login()
upload_image(r"/home/ankit/Downloads/449753547_867256125427317_5961908611794714846_n.jpg")



print('file uploaded')

# selectFromComputer = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.).is_displayed()
# print(selectFromComputer)
# element = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="mount_0_0_4n"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div/div[1]/div/div/svg/line[1]')) 


# <input autocomplete="off" class="x5ur3kl xopu45v x1bs97v6 xmo9t06 x1j8ye7u x1rjkts5 x13z9klp xjc6cxp x178xt8z xm81vs4 xso031l xy80clv x5n08af x1iyjqo2 xvs91rp xklk4pu xdj266r x11i5rnm xat24cr x1mh8g0r x1plvlek xryxfnj x1s3xk63 xlqc9nw x8tigb1 x1ad04t7 x1glnyev xs3hnx8 x7xwk5j x1rheh84 x1ck6gwh x175bfct x1meze4m x10eltez x1qt4tve x1s07b3s x1rvh84u x1iorvi4 xpvbz4a xjkvuk6 xohu8s8 xh8yej3 x1jguvu7 x15aq7wb xygx6cg xrqayxw x1uvtmcs x1ejq31n xd10rxx x1sy0etr x17r0tee xjbqb8w xzd0ubt" placeholder="Add Location" spellcheck="true" type="text" value="" name="creation-location-input">
# <input autocomplete="off" class="x5ur3kl xopu45v x1bs97v6 xmo9t06 x1j8ye7u x1rjkts5 x13z9klp xjc6cxp x178xt8z xm81vs4 xso031l xy80clv x5n08af x1iyjqo2 xvs91rp xklk4pu xdj266r x11i5rnm xat24cr x1mh8g0r x1plvlek xryxfnj x1s3xk63 xlqc9nw x8tigb1 x1ad04t7 x1glnyev xs3hnx8 x7xwk5j x1rheh84 x1ck6gwh x175bfct x1meze4m x10eltez x1qt4tve x1s07b3s x1rvh84u x1iorvi4 xpvbz4a xjkvuk6 xohu8s8 xh8yej3 x1jguvu7 x15aq7wb xygx6cg xrqayxw x1uvtmcs x1ejq31n xd10rxx x1sy0etr x17r0tee xjbqb8w xzd0ubt xwhw2v2" placeholder="Add location" spellcheck="true" type="text" value="Delhi, India" name="creation-location-input" style="--placeholder-color: rgba(232, 229, 227, 0.6) !important; color: rgb(229, 225, 223) !important;" disabled="">