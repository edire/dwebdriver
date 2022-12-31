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

12/30/2022 - Added dev-shm usage and window size for docker compatibility.
12/22/2022 - Added window size option to ChromeDriver.
12/21/2022 - Added no_sandbox option when starting ChromeDriver.
12/19/2022 - Updated download directory to current working directory for cross platform functionality.