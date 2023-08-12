
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import os
from . import tools


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
                 , use_chromium = False
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
        if use_chromium:
            super().__init__(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=self.options)
        else:
            super().__init__(service=ChromeService(ChromeDriverManager().install()), options=self.options)

    def driver_command(self, xpath, command, command_value=None):
        tools._driver_command(self, xpath, command, command_value)

    def process_df(self, df_orig, odbc_db=None):
        tools._process_df(self, df_orig, odbc_db)