import asyncio
import requests
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import pickle
import re
with open('batches.txt', 'r') as file:
    totalbatches = file.read()
    # print(totalbatches)
    batchvalues=totalbatches.split('\n')

async def main():
  total_links = []
  async with async_playwright() as p:
      browser = await p.chromium.launch(headless=False)
      page = await browser.new_page()
      for tb in batchvalues:
        await page.goto("https://www.ycombinator.com/companies?batch="+tb)
        # await page.wait_for_load_state("networkidle")
        print("batch ",tb)
        await asyncio.sleep(2)
        for x in range(1, 25):
          await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
          print("Scrolling:", x)
          await asyncio.sleep(1)
          html_content = await page.content()
          soup = BeautifulSoup(html_content, "html.parser")
          links=soup.find_all('a',class_ = '_company_99gj3_339')
          all_links = [link['href'] for link in links]
          # total_links = total_links + all_links
          total_links.extend(all_links)
  await browser.close()

  print(total_links)
  print(len(total_links))
  with open("linksfromallbatches.txt", "w") as file:
      file.writelines("\n".join(total_links))

asyncio.run(main())