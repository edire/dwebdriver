# Description

A Python library by Dire Analytics for custom Selenium driver handling.

## Installation

pip install git+https://github.com/edire/dwebdriver.git

## Usage

```python
import dwebdriver

driver = dwebdriver.ChromeDriver()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License

## Updates

08/12/2023 - Moved driver functions to universal tools module. Added use_chromium option.<br>
08/12/2023 - Updated to use webdriver-manager for new chromedriver binaries.<br>
03/29/2023 - Updated ChromeDriver to use --headless=new in order to download reports in headless.<br>
03/24/2023 - Added drop down field selection.<br>
03/19/2023 - Added scroll margin logic.<br>
03/17/2023 - Added logic to accept alert.<br>
02/21/2023 - Added url command in dataframe processing.<br>
01/19/2023 - Added "switch to parent" logic.<br>
01/07/2023 - Updated for deprecated find_element Selenium logic.  Updated to use dataframe copy.  Added switch frame logic to dataframe processing.  Fixed switch frame logic to not look for xpath element.  Added missing colon to if statement.<br>
Updated switch frame logic to look for frame as integer.<br>
12/30/2022 - Added dev-shm usage and window size for docker compatibility.<br>
12/22/2022 - Added window size option to ChromeDriver.<br>
12/21/2022 - Added no_sandbox option when starting ChromeDriver.<br>
12/19/2022 - Updated download directory to current working directory for cross platform functionality.