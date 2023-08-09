from playwright.sync_api import Playwright, sync_playwright
from random_username.generate import generate_username
import random

#config
proxy_username = "proxy username"
proxy_password = "proxy password"
referall_id = "your referall id"


def run(playwright: Playwright, server) -> None:
    browser = playwright.firefox.launch(proxy={
        "server": server,
        "username": proxy_username,
        "password": proxy_password 
    })
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://lmwr.com/?ref={referall_id}")
    page.get_by_placeholder("Enter email address").click()
    email = f"{generate_username()[0].lower()+str(random.randint(1,1000))}@m3ta.tech"
    print(email)
    page.get_by_placeholder("Enter email address").fill(email)
    page.get_by_role("button", name="Join Waitlist & Enter Challenge").click()

    context.close()
    browser.close()


with open("proxies.txt", "r") as f:
    proxies = f.read().strip().split("\n")

with sync_playwright() as playwright:
    for server in proxies:
        try:
            print(server)
            run(playwright, server)
        except:
            pass
