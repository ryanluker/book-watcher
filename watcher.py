import subprocess as s
from playwright.sync_api import sync_playwright

# Setup config by reading the local ini
import configparser
config = configparser.ConfigParser()
config.read("config.ini")


def check_orl_waitlist(page):
    orl_holds_url = "https://orl.bibliocommons.com/v2/holds"
    orl_username = config["orl"]["username"]
    orl_pass = config["orl"]["password"]
    page.goto(orl_holds_url)
    
    # Login if we are redirect'd there
    page.get_by_role("textbox", name="Username or Barcode :").fill(orl_username)
    page.get_by_role("textbox", name="PIN :").fill(orl_pass)
    page.get_by_role("button", name="Log In", description="Log In", exact=True).click()

    # Wait for the holds to load
    page.locator(".cp-holds-list").wait_for(state="visible")

    # Look at the waitlist positions and see if any are in position 1
    queue = page.locator(".cp-holds-list")
    hold_list = queue.locator(".cp-hold-item").all()
    for hold_card in hold_list:
        hold_position = hold_card.locator(".cp-hold-position")
        hold_title = hold_card.locator(".title-content")
        print(hold_title.text_content())
        print(hold_position.text_content())


def check_kobo_wishlist(page):
    pass


def send_desktop_notification(results):
    """Sends a linux desktop notification via notify-send"""
    results_message = ""
    if results:
        if results["kobo_has_deals"]:
            results_message += "Kobo: deals found! \n"
        if results["orl_has_first_positions"]:
            results_message += "ORL: first position reached! \n"
    s.call(["notify-send", "Book Watcher run complete!", results_message])


def main():
    with sync_playwright() as playwright:
        # Setup playwright firefox
        firefox = playwright.firefox
        # Use headed mode and slow mode for human readability
        browser = firefox.launch()
        page = browser.new_page()

        # Perform the checks on ORL and Kobo
        check_result_orl = check_orl_waitlist(page)
        check_result_kobo = check_kobo_wishlist(page)
    
    results = {
        "orl_has_first_positions": False,
        "kobo_has_deals": False
    }
    if check_result_orl:
        result["orl_has_first_positions"] = True
    if check_result_kobo:
        result["kobo_has_deals"] = True

    # Use the native desktop notification system to send the results
    send_desktop_notification(results)


if __name__ == "__main__":
    main()
