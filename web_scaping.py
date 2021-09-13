import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("- incognito")
chromedriver_path = '/Users/dell/Desktop/Opera Browser.lnk"'
def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

brower = create_webdriver
brower.get("https://anilist.co/search/manga/popular")

projects = brower.find_elements_by_xpath("inspect the class of infromaty") #right click on page
project_list = {}
for p in projects:
    prog_name = p.text #Project name
    proj_url = p.find_elements_by_xpath("a")[0].get_attribute('href') #Project url
    project_list[prog_name] = proj_url

brower.quit()

project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

project_df['project_name'] = project_df.index
project_df.columns = ['Project_url', 'progject_name']
project_df =project_df.reset_index(drop=True)

project_df.to_csv('project_list.csv')
