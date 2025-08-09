import yaml
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Yaml logic
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Setup Chrome options
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# Start undetected Chrome driver
driver = uc.Chrome(options=options)

try:
    driver.get("https://www.popmart.com/us/user/login?redirect=%2Faccount")

        # Wait for Cloudflare "Just a moment..." to finish
    while "Just a moment..." in driver.title or "Checking your browser" in driver.page_source:
        print("🛡️t Waiting through Cloudflare screen...")
        time.sleep(2)

    # Wait for and click "United States" on the region modal
    united_states_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'United States')]"))
    )   
    driver.execute_script("arguments[0].click();", united_states_button)
    print("✅ Clicked United States")

    # Wait for cookies button and click "ACCEPT"
    accept_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'ACCEPT')]"))
    )   
    driver.execute_script("arguments[0].click();", accept_btn)
    print("✅ Clicked ACCEPT")



   # Wait for email input field
    sample_email = data['email']
    email_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
    )   
    email_input.clear()
    email_input.send_keys(sample_email)
    print("📧 Email input successful")

    checkbox = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//label[contains(@class, "ant-checkbox-wrapper")]/span/input[@type="checkbox"]'))
)
    driver.execute_script("arguments[0].click();", checkbox)
    print("✅ Checkbox clicked.")
 

    continue_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CONTINUE')]"))
    )   
    driver.execute_script("arguments[0].click();", continue_btn)
    print("continued")


    sample_password = data['password']
    password_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "password"))
    )   
    password_input.clear()
    password_input.send_keys(sample_password)
    print("password input success")

    sign_in_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'SIGN IN')]"))
    )
    driver.execute_script("arguments[0].click();", sign_in_btn)
    print("sign in clicked")



    # wedpage for item
    
    # Open the target product page
    driver.get('https://www.popmart.com/us/products/2491/HACIPUPU-Rolling-Time-Machine-Series-Figures')



    # Wait for and click "ADD TO BAG"
    add_to_bag_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'ADD TO BAG')]"))
    )
    driver.execute_script("arguments[0].click();", add_to_bag_btn)
    print("🛒 Added to bag")


    # Go to cart page directly
    cart_url = "https://www.popmart.com/us/largeShoppingCart"
    driver.get(cart_url)
    print("🛍️ Navigated to cart page")

    # Click CHECK OUT
    check_out_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CHECK OUT')]"))
    )
    driver.execute_script("arguments[0].click();", check_out_btn)
    print("✅ Proceeded to checkout")

    #TEST SIGN IN LOGIC TO SEE IF WORK

    # Wait for email input field

    # Wait for email input field
    sample_email = data['email']
    email_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
    )   
    email_input.clear()
    email_input.send_keys(sample_email)
    print("📧 Email input successful")

    checkbox = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//label[contains(@class, "ant-checkbox-wrapper")]/span/input[@type="checkbox"]'))
)
    driver.execute_script("arguments[0].click();", checkbox)
    print("✅ Checkbox clicked.")
 

    continue_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CONTINUE')]"))
    )   
    driver.execute_script("arguments[0].click();", continue_btn)
    print("continued")


    sample_password = data['password']
    password_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "password"))
    )   
    password_input.clear()
    password_input.send_keys(sample_password)
    print("password input success")

    sign_in_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'SIGN IN')]"))
    )   
    driver.execute_script("arguments[0].click();", sign_in_btn)
    print("sign in clicked")

     # Click CHECK OUT
    check_out_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CHECK OUT')]"))
    )
    driver.execute_script("arguments[0].click();", check_out_btn)
    print("✅ Proceeded to checkout")
    
    # Select all

    select_all = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".index_checkbox__w_166"))
    )
    driver.execute_script("arguments[0].click();", select_all)
    print("hit select all")

    #Proceed to pay btn
    proceed_to_pay_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'PROCEED TO PAY')]"))
    )
    driver.execute_script("arguments[0].click();", proceed_to_pay_btn)
    print("proceed to pay clicked")


except Exception as e:
    print("❌ Error encountered:", e)
    input("Press Enter to exit...")

finally:
    time.sleep(10)
    driver.quit()
