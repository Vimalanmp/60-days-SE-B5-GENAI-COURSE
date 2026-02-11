from playwright.sync_api import sync_playwright, TimeoutError
from datetime import datetime

def minorilabs_full_data_to_txt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ✅ FIXED HERE
        page.goto(
            "https://minorilabs.com/",
            wait_until="domcontentloaded",
            timeout=30000
        )

        page.wait_for_timeout(2000)

        # ---------- METADATA ----------
        def get_meta(selector):
            el = page.locator(selector)
            return el.get_attribute("content") if el.count() > 0 else "Not Found"

        metadata = {
            "Page Title": page.title(),
            "Meta Description": get_meta("meta[name='description']"),
            "Meta Keywords": get_meta("meta[name='keywords']"),
            "OG Title": get_meta("meta[property='og:title']"),
            "OG Description": get_meta("meta[property='og:description']"),
            "OG URL": get_meta("meta[property='og:url']")
        }

        # ---------- MENU NAV ----------
        try:
            page.hover("text=What We Do")
            page.click("text=Digital Marketing")
            page.wait_for_url("**digital-marketing**", timeout=15000)

            digital_marketing_text = page.locator("main").inner_text()

        except TimeoutError:
            digital_marketing_text = "Digital Marketing page not found."

        browser.close()

        # ---------- WRITE FILE ----------
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write("MINORI LABS – WEBSITE DATA REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Extracted On: {datetime.now()}\n\n")

            f.write("📌 WEBSITE METADATA\n")
            f.write("-" * 30 + "\n")
            for k, v in metadata.items():
                f.write(f"{k}: {v}\n")

            f.write("\n📌 DIGITAL MARKETING PAGE CONTENT\n")
            f.write("-" * 30 + "\n")
            f.write(digital_marketing_text)

        print("✅ Done. Data saved to data.txt")

if __name__ == "__main__":
    minorilabs_full_data_to_txt()
