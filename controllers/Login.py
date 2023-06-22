from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Login:

    def  __init__(self, inputs, loginInfo, url):
         """
         inputs: Array contendo os Xpath completos dos inputs login e senha respectivamente
         loginInfo: Array contendo as informações de login e senha respectivamente 
         """
         
         self.inputUser, self.inputPassword = inputs[0], inputs[1]
         self.username, self.password = loginInfo[0], loginInfo[1]
         self.url = url

    def login(self, timeout="5m"):

        """
        timeout: Define quanto tempo a sessão irá durar
        EX: 1m (1 minuto), 1h (1 hora)
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-full-screen")
        chrome_options.add_argument("--kiosk")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
        # Configura as opções do WebDriver para usar o Selenoid
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "111.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "sessionTimeout": timeout,
                "labels":{"manual":"true"},
             
                
            }
        }
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=capabilities,
            options=chrome_options
        )

        user, pwd = self.username, self.password
        driver.get(self.url)
        actions = ActionChains(driver)
        #actions.key_down(Keys.F11)
        #actions.key_up(Keys.F11)
        #actions.key_down(Keys.F12)
        #actions.key_up(Keys.F12)
        #actions.perform()
        username = driver.find_element(By.XPATH, self.inputUser)
        password = driver.find_element(By.XPATH, self.inputPassword)
        username.send_keys(user)
        password.send_keys(pwd)
        password.submit()
        driver.maximize_window()
        driver.fullscreen_window()
        self.sessionId = driver.session_id
        return driver
    
    def getSessionId(self):
        return self.sessionId
