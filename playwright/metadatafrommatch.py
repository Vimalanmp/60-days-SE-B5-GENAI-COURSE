from playwright.sync_api import sync_playwright, TimeoutError

def sa_vs_aus_news_with_metadata():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open Google News search
        page.goto(
            "https://news.google.com/search?q=SA%20vs%20Aus",
            wait_until="domcontentloaded"
        )

        article_xpath = '//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[1]/c-wiz/div/div[1]/div[1]/a'

        try:
            # Wait for the first article using XPath
            page.wait_for_selector(f"xpath={article_xpath}", timeout=15000)

        except TimeoutError:
            print("❌ First article not loaded with given XPath.")
            browser.close()
            return

        # Locate the article
        first_article = page.locator(f"xpath={article_xpath}")

        # Extract headline text
        headline_text = first_article.inner_text()
        print(f"\n📰 Opening article: {headline_text}\n")

        # Click the article
        first_article.click()
        page.wait_for_load_state("domcontentloaded")

        # ---- METADATA EXTRACTION ----
        def get_meta(selector):
            el = page.locator(selector)
            return el.get_attribute("content") if el.count() > 0 else None

        metadata = {
            "Page Title": page.title(),
            "Meta Description": get_meta("meta[name='description']"),
            "Meta Keywords": get_meta("meta[name='keywords']"),
            "OG Title": get_meta("meta[property='og:title']"),
            "OG Description": get_meta("meta[property='og:description']"),
            "OG URL": get_meta("meta[property='og:url']")
        }

        print("===== ARTICLE METADATA =====")
        for k, v in metadata.items():
            print(f"{k:18}: {v}")
        print("============================")

        browser.close()

if __name__ == "__main__":
    sa_vs_aus_news_with_metadata()
