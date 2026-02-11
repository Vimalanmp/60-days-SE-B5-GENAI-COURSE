from playwright.sync_api import sync_playwright
import time

def sa_vs_aus_news():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open Google News (safe)
        page.goto("https://news.google.com/search?q=SA%20vs%20Aus")

        # Give page time to load like a human
        time.sleep(3)

        # Wait for news headlines
        page.wait_for_selector("article h3", timeout=10000)

        headlines = page.locator("article h3").all_text_contents()

        print("\nLatest SA vs Aus News:\n")
        for i, h in enumerate(headlines[:5], 1):
            print(f"{i}. {h}")

        browser.close()

if __name__ == "__main__":
    sa_vs_aus_news()
