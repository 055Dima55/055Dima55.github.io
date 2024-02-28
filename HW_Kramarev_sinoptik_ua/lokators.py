url = "https://ua.sinoptik.ua/"

# By.XPATH
Search_area = "//input[contains(@id,'search_city')]"
# Search_area: Шукає поле введення для пошуку міста.
Language_switcher = "//a[contains(@title,'погода в Киеве')]"
# Language_switcher: Шукає перемикач мови для погоди в Києві.
Days_switcher = "//div[@id='bd4']"
# Days_switcher: Шукає блок з перемикачем днів.
Number_days_switch = "//a[@href='//ua.sinoptik.ua/погода-київ/10-днів']"
# Number_days_switch: Шукає посилання на прогноз на 10 днів.
Weather_map = "//a[contains(@class,'otherCity')]"
# Weather_map: Шукає посилання на карту погоди для інших міст.

# By.CSS
Search_area_1 = "input#search_city"
Language_switcher_2 = "div#sLang"
Days_switcher_3 = "div#bd4"
Number_days_switch_4 = "a.menu-item"
Weather_map_5 = "a.otherCity"
