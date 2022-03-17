import asyncio
import os
import subprocess

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

profile_path = os.path.expandvars(
    "C:\\Users\\Admin\\Desktop\\Tor Browser\\Data\\Browser\\profile.default"
)
options = Options()
options.set_preference("profile", profile_path)
service = Service(
    # os.path.expandvars(r"%USERPROFILE%\Desktop\Tor Browser\Browser\firefox.exe"),
    # executable_path=GeckoDriverManager().install()
    executable_path="C:\\Users\\Admin\\Desktop\\Tor Browser\\Browser\\firefox.exe"
)

options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "127.0.0.1")
options.set_preference("network.proxy.socks_port", 9050)
options.set_preference("network.proxy.socks_remote_dns", False)


def main():
    try:
        driver = Firefox(service=service, options=options)
        driver.get("http://check.torproject.org")
        driver.save_screenshot("screenshot.png")
    except Exception as e:
        print(e, type(e))
    


if __name__ == "__main__":
    main()