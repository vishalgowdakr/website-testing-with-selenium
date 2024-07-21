from typing import List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from pydantic import BaseModel
from selenium.webdriver.firefox.webdriver import WebDriver

class LoginInput(BaseModel):
    login: Optional[str]
    password: Optional[str]

class LoginOutput(BaseModel):
    msg: str

class LoginTestCase(BaseModel):
    name: str
    input: LoginInput
    expected_output: LoginOutput

class LoginTest():
    def test(self):
        test_cases: List[LoginTestCase] = [
            LoginTestCase(
                name="Null Email",
                input=LoginInput(
                    login=None,
                    password=None
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Invalid Email",
                input=LoginInput(
                    login="notanemail@email",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Unregistered email",
                input=LoginInput(
                    login="yodaki1370@furnato.com",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Registered email and null password",
                input=LoginInput(
                    login="vishalgowda096@gmail.com",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Registered email and invalid password",
                input=LoginInput(
                    login="vishalgowda096@gmail.com",
                    password="helloworld",
                ),
                expected_output=LoginOutput(
                    msg=f"This password is incorrect.\nForgot / Reset password?"
                )
            ),
            LoginTestCase(
                name="Registered email and valid password",
                input=LoginInput(
                    login="vishalgowda096@gmail.com",
                    password="passWord0",
                ),
                expected_output=LoginOutput(
                    msg="Success"
                )
            ),
            LoginTestCase(
                name="Null Username",
                input=LoginInput(
                    login=None,
                    password=None
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Invalid Username",
                input=LoginInput(
                    login="notanusername@-1",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Unregistered username",
                input=LoginInput(
                    login="vishalgowdakrrrrr",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Registered username and null password",
                input=LoginInput(
                    login="vishalgowdakr",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="All fields are required"
                )
            ),
            LoginTestCase(
                name="Registered username and invalid password",
                input=LoginInput(
                    login="vishalgowdakr",
                    password="helloworld",
                ),
                expected_output=LoginOutput(
                    msg=f"This password is incorrect.\nForgot / Reset password?"
                )
            ),
            LoginTestCase(
                name="Registered username and valid password",
                input=LoginInput(
                    login="vishalgowdakr",
                    password="passWord0",
                ),
                expected_output=LoginOutput(
                    msg="Success"
                )
            ),
        ]
        driver = webdriver.Firefox()
        driver.get("https://chess.com/login")
        for tc in test_cases:
            print(f"Running test case: {tc.name}")
            self.login(tc, driver)
        driver.close()

    def login(self, tc: LoginTestCase, driver: WebDriver):
        if tc.name == "Null username":
            driver.get("https://chess.com/login")
        if tc.input.login != None:
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/form/div[1]/div/div/input").clear()
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/form/div[1]/div/div/input").send_keys(tc.input.login)
        if tc.input.password != None:
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/form/div[2]/div/div/input").clear()
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/form/div[2]/div/div/input").send_keys((tc.input.password))
        driver.find_element(by=By.ID, value="login").click()
        if (tc.name == "Registered username and valid password" or tc.name == "Registered email and valid password"):
            if driver.current_url != "https://www.chess.com/home":
                print(driver.current_url)
            driver.get("https://www.chess.com/logout")
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/span/form/button").click()
            driver.get("https://www.chess.com/login")
            return
        else:
            output = driver.find_element(by=By.CLASS_NAME, value="authentication-login-error").text
        if output != tc.expected_output.msg:
            print("Expected Message: "+tc.expected_output.msg+f"\nActual Message: "+output)


test = LoginTest()
test.test()
