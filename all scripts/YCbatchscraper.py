#extracting batches and stored into a file
import asyncio
import requests
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import pickle
import re

batches=[]
allbatches=[]
async def main():
  async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()

    await page.goto("https://www.ycombinator.com/companies")
    await page.wait_for_load_state("networkidle")

    for x in range(1, 3):
      await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
      print("Scrolling:", x)
      await asyncio.sleep(1)
      html_content = await page.content()
      soup = BeautifulSoup(html_content, "html.parser")
      batchnames = soup.find_all("span", class_='_label_99gj3_225')
      batches = [span.get_text(strip=True) for span in batchnames]
      # allbatches.append(batches)
    await browser.close()
    Batchvalues=[]
    print(len(batchnames))
    for a in batches:
      print(a)
    print(len(batches))
    Batchvalues=[batch for batch in batches if batch.startswith(('S','W'))]
    print(Batchvalues)
    new_allbatches=Batchvalues[:-10]

    new_allbatches.pop(0)
    print(new_allbatches)
    print(len(new_allbatches))
    with open("batches.txt", "w") as file:
      file.writelines("\n".join(new_allbatches))
    soup_file = 'soup_data.pkl'
    with open(soup_file, 'wb') as f:
      pickle.dump(soup, f)


asyncio.run(main())

