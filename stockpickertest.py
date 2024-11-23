from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()

driver.get("https://github-pages.senecapolytechnic.ca/sed500/Labs/Lab4/StockPicker.html")

#testing RE-01.3
def test_company_symbol():
    symbol = driver.find_element(By.ID, "symbol")
    symbol.clear()
    symbol.send_keys("NKE")
    time.sleep(2)
    assert symbol.get_attribute("value") == "NKE", "Company Symbol Test Failed"
    symbol.clear()
    print("Company Symbol Test Executed Successfully")

# Test RE-01.5
def test_category_selection():
    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("income-statement")
    time.sleep(2)
    assert category_select.first_selected_option.get_attribute("value") == "income-statement", "Category selection failed."
    print("Category Selection Test Executed Successfully")
    
# Test RE-01.6
def test_submit_query():
    submit_button = driver.find_element(By.ID, "submit")
    symbol = driver.find_element(By.ID, "symbol")
    category_select = Select(driver.find_element(By.ID, "category"))
    
    symbol.send_keys("GOOG")
    category_select.select_by_value("income-statement")
    submit_button.click()
    time.sleep(2)  

    data_div = driver.find_element(By.ID, "data")
    assert len(data_div.text) > 0, "Submit query failed."
    print("Submit Query Test Executed Successfully")
    
# Test RE-01.7
def test_reset_functionality():
    reset_button = driver.find_element(By.ID, "reset")
    symbol = driver.find_element(By.ID, "symbol")
    category_select = Select(driver.find_element(By.ID, "category"))
    
    symbol.send_keys("AMZN")
    category_select.select_by_value("income-statement")
    reset_button.click()
    time.sleep(2)

    assert symbol.get_attribute("value") == "", "Symbol input reset failed."
    assert category_select.first_selected_option.get_attribute("value") == "income-statement", "Category reset failed."
    print("Reset Functionality Test Executed Successfully")


# Test RE-02.2
def test_stock_screener_category_selection():
    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("stock-screener")

    stock_screener_select = Select(driver.find_element(By.ID, "stock-screener"))
    stock_screener_select.select_by_value("betaMoreThan")
    assert stock_screener_select.first_selected_option.get_attribute("value") == "betaMoreThan", "Stock screener category selection failed."
    print("Stock Screener Category Selection Test Executed Successfully")

# Test RE-02.3
def test_stock_screener_value_input():

    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("stock-screener")


    screener_value_input = driver.find_element(By.ID, "stock-screener-value")
    screener_value_input.clear()
    screener_value_input.send_keys("2000000")
    
    assert screener_value_input.get_attribute("value") == "2000000", "Stock screener value input failed."
    print("Stock Screener Value Input Test Executed Successfully")
    
# Test RE-03
def test_data_display_section_after_query():
    category_select = Select(driver.find_element(By.ID, "category"))
    submit_button = driver.find_element(By.ID, "submit")
    symbol = driver.find_element(By.ID, "symbol")
    category_select.select_by_value("income-statement")
    symbol.clear()
    symbol.send_keys("AAPL")
    submit_button.click()
    time.sleep(2) 

    data_div = driver.find_element(By.ID, "data")
    assert len(data_div.text) > 0, "Data display section failed to populate after query."
    print("Data Display Section After Query Test Executed Successfully")

# Test RE-08
def test_reset_returns_to_default_ui():
    symbol = driver.find_element(By.ID, "symbol")
    symbol.send_keys("AAPL")
    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("cash-flow-statement")
    
    reset_button = driver.find_element(By.ID, "reset")
    reset_button.click()
    time.sleep(1)  
    
    # Verify defaults
    assert symbol.get_attribute("value") == "", "Symbol input reset to default failed."
    assert category_select.first_selected_option.get_attribute("value") == "income-statement", "Category reset to default failed."
    print("Reset Returns to Default UI Test Executed Successfully")




try:
    test_company_symbol()
    test_category_selection()
    test_submit_query()
    test_reset_functionality()
    test_stock_screener_category_selection()
    test_stock_screener_value_input()
    test_data_display_section_after_query()
    test_reset_returns_to_default_ui()
    print("All tests passed.")
    
except Exception as e:
    print(e)
finally:
    driver.quit()