from playwright.async_api import async_playwright
import asyncio

boldedTitle = []

async def main():
    
    async with async_playwright() as pw:
        
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.espn.com/mlb/player/splits/_/id/39572")
        section = await page.query_selector("table")
        data = await page.query_selector("#fittPageContainer > div.pageContent > div > div:nth-child(5) > div > div > div.ResponsiveWrapper > section > div > div.ResponsiveTable.ResponsiveTable--fixed-left.player-splits-table")
        text = await section.inner_text()
        data = await data.inner_text()
        boldedTitle = text
        boldedTitle.split(" ")
        # If the title is in caps then we can remove it
        print(boldedTitle)
        # section_data = await section.inner_text()
        # print(section_data)
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
    
