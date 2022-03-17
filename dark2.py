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
    # executable_path="C:\\Users\\Admin\\Desktop\\Tor Browser\\Browser\\firefox.exe"
    executable_path="C:\\Users\\Admin\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe"
)

options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "127.0.0.1")
options.set_preference("network.proxy.socks_port", 9050)
options.set_preference("network.proxy.socks_remote_dns", False)


async def main():
    async def cleanup():
            
            print(torexe.pid)
            torexe.kill()
            driver.quit()

    try:
        # https://stackoverflow.com/a/62686067/8608146
        torexe = subprocess.Popen(
            os.path.expandvars(
                "C:\\Users\\Admin\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe"
            )
        )
        driver = Firefox(service=service, options=options)
        driver.get("http://exchangehd5455aori4qvrwhyno4ul7xrz4foy6qwga3olnbclp5f4qd.onion")
        driver.save_screenshot("screenshot.png")
    except Exception as e:
        print(e, type(e))
    finally:
        await cleanup()


if __name__ == "__main__":
    asyncio.run(main())