from selenium import webdriver

# Launch the browser and navigate to the web page
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Find the web element using XPath
element = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')

# Get the location of the element
location = element.location

# Get the size of the element
size = element.size

# Calculate the coordinates relative to the screen
x = location['x'] + size['width'] / 2
y = location['y'] + size['height'] / 2

# Print the coordinates
print(f"X: {x}, Y: {y}")

# Close the browser
driver.quit()
