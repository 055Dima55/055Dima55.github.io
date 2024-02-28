url = "https://ua.sinoptik.ua/"

# By.XPATH
Search_area = "//input[contains(@id,'search_city')]"
Language_switcher = "//a[contains(@title,'погода в Киеве')]"
Language_switcher_1 = Language_switcher.encode('utf-8')
Days_switcher = "//div[@id='bd4']"
Number_days_switch = "//a[@href='//ua.sinoptik.ua/погода-київ/10-днів']"
Number_days_switch_1 = Number_days_switch.encode('utf-8')
Weather_map = "//a[contains(@class,'otherCity')]"

# By.CSS
Search_area_1 = "input#search_city"
Language_switcher_2 = "div#sLang"
Days_switcher_3 = "div#bd4"
Number_days_switch_4 = "a.menu-item"
Weather_map_5 = "a.otherCity"
