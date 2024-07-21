from typing import List, Optional
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pydantic import BaseModel

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
                    msg="This password is incorrect"
                )
            ),
            LoginTestCase(
                name="Unregistered email",
                input=LoginInput(
                    login="yodaki1370@furnato.com",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="This password is incorrect"
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
                    msg="This password is incorrect"
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
                    msg="This password is incorrect"
                )
            ),
            LoginTestCase(
                name="Unregistered username",
                input=LoginInput(
                    login="vishalgowdakrrrrr",
                    password=None,
                ),
                expected_output=LoginOutput(
                    msg="This password is incorrect"
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
                    msg="This password is incorrect"
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
        for tc in test_cases:
            print(f"Running test case: {tc.name}")
            output: LoginOutput = self.login(tc.input)

    def login(self, input: LoginInput):
        driver = webdriver.Chrome()
        driver.get("https://chess.com/login")
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/form/div[1]/div/div/input").send_keys(input.login)
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/form/div[2]/div/div/input").send_keys((input.password))
