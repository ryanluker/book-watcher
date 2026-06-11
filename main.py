import subprocess as s
from playwright.sync_api import sync_playwright


def check_orl_waitlist(page):
    orl_holds_url = "https://orl.bibliocommons.com/v2/holds"
    page.goto(orl_holds_url)
    breakpoint()


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
        browser = firefox.launch(headless=False, slow_mo=100)
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
