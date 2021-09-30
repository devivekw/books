import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# Selenium initalization
driver = webdriver.Chrome(ChromeDriverManager().install())

for i in range(1,74):

    driver.get(f'https://image.slidesharecdn.com/solutionmanualofoperatingsystembysilberschatzgalvinandgagne-160530051851/95/solution-manual-of-operating-system-concepts-by-abraham-silberschatz-peter-baer-galvin-greg-gagne-{i}-638.jpg?cb=1580673965')
    with open(f'{i}.jpeg', 'wb') as file:
        #identify image to be captured
        img = driver.find_element_by_xpath('/html/body/img')
        #write file
        file.write(img.screenshot_as_png)
