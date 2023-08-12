
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from numpy import nan
import os
from time import sleep


class ChromeDriver(Chrome):
    def __init__(self
                 , download_directory = os.getcwd()
                 , headless=True
                 , no_sandbox=False
                 , window_size=None # Docker=1920,1080
                 , allow_popups=False
                 , disable_extensions=False
                 , user_profile=None
                 , user_dir=fr"{os.path.expanduser('~')}\AppData\Local\Google\Chrome\User Data"
                 ):
        self.directory = download_directory
        self.options = ChromeOptions()
        self.options.add_experimental_option('prefs', {'download.default_directory': download_directory})
        if window_size==None:
            self.options.add_argument('--start-maximized')
        else:
            self.options.add_argument(f'--window-size={window_size}')
        self.options.add_argument("--log-level=3")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("--disable-dev-shm-usage")
        if headless==True:
            self.options.add_argument('--headless=new')
        if no_sandbox==True:
            self.options.add_argument('--no-sandbox')
        if allow_popups == True:
            self.options.add_argument("--disable-popup-blocking")
        if disable_extensions == True:
            self.options.add_argument("--disable-extensions")
        if user_profile != None:
            self.options.add_argument(f"--user-data-dir={user_dir}")
            self.options.add_argument(f"--profile-directory={user_profile}")
        super().__init__(service=ChromeService(ChromeDriverManager().install()), options=self.options)

    def driver_command(self, xpath, command, command_value=None):
        if xpath != None:
            element = self.find_element(by='xpath', value=xpath)
            
        if command == 'url':
            self.get(command_value)
        elif command == 'click':
            element.click()
        elif command == 'send_keys':
            element.send_keys(command_value)
        elif command == 'clear':
            element.clear()
        elif command == 'return':
            element.send_keys(Keys.RETURN)
        elif command == 'backspace':
            element.send_keys(Keys.BACKSPACE)
        elif command == 'control':
            element.send_keys(Keys.CONTROL, command_value)
        elif command == 'double_click':
            action = ActionChains(self)
            action.double_click(element).perform()
        elif command == 'scroll':
            self.execute_script("arguments[0].scrollIntoView();", element)
        elif command == 'scroll_margin':
            self.execute_script(f"arguments[0].style.marginTop = '-{command_value}px'", element)
        elif command == 'switch_frame':
            if command_value == 'parent':
                self.switch_to.default_content()
            else:
                try:
                    command_value = int(command_value)
                except:
                    pass
                self.switch_to.frame(command_value)
        elif command == 'accept':
            self.switch_to.alert.accept()
        elif command == 'drop_down':
            for option in element.find_elements(by='tag name', value=('option')):
                if option.text == command_value:
                    option.click()
                    break

    def process_df(self, df_orig, odbc_db=None):
        df = df_orig.copy()
        df.dropna(axis=0, how='all', inplace=True)
        df.replace({nan:None}, inplace=True)
        for i in range(df.shape[0]):
            _pass = False
            command = df['command'].iloc[i]
            command_value_type = df['command_value_type'].iloc[i]
            command_value = df['command_value'].iloc[i]
            post_time_delay = df['post_time_delay'].iloc[i]
            xpath = df['xpath'].iloc[i]

            if command_value_type == 'env':
                command_value = os.getenv(command_value)

            if command_value_type == 'sql':
                command_value = odbc_db.read(command_value).iloc[0, 0]

            if command_value_type == 'python':
                _locals = {}
                exec(command_value, None, _locals)
                command_value = _locals['command_value']

            if command_value_type == 'python_check':
                _locals = locals()
                exec(command_value, globals(), _locals)
                if _locals['true_false'] == True:
                    command_value = _locals['command_value']
                else:
                    _pass = True

            if _pass == False:
                self.driver_command(xpath, command, command_value)
                if post_time_delay != None:
                    sleep(post_time_delay)