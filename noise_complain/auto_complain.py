from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Noise complaint form:

#https://www1.nyc.gov/apps/311universalintake/form.htm?serviceName=NYPD+Noise+Neighbor

def complain():
    #starts complaint
    driver = webdriver.Firefox()
    driver.get("https://www1.nyc.gov/apps/311universalintake/form.htm?serviceName=NYPD+Noise+Neighbor")
    elem = driver.find_element_by_xpath('//input[@value="START"]')
    elem.send_keys(Keys.RETURN)

    driver.find_element_by_xpath("//select[@name='formFields.Descriptor 1']/option[text()='Loud Music/Party']").click()
    
    
def fill_complaint_form():
    complain()

    
if __name__ == '__main__':
    fill_complaint_form()
