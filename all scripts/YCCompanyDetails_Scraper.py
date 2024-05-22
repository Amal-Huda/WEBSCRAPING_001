import asyncio
import os.path
import requests
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import json
from splitedlinks1047each import list2,list4,list3,list1
with open('linksfromall.txt','r')as file:
  all_linkss=file.read()
  linkvalues=all_linkss.split('\n')
print(len(linkvalues))
if not os.path.exists("YCOutput_Json2.json"):
    with open("YCOutput_Json2.json", "w") as f:
        f.write("[")
#scraping data from some urls(list1,list2,list3,list4)
li=list1[776:]
async def main():
    df_to_company=pd.DataFrame(columns=['company','social_profiles','founders'])
    name, tagline, description, location,company_type, industry_tag, web_url,founded_year,teamsize, twitter, facebook, linkedin, cruchbase, founder_twitter, founder_linkedin, founder_description, founders,new_founser_list =[],[],[], [],[], [], [], [], [], [], [], [], [], [], [], [], [], []
    for l in li:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://www.ycombinator.com/"+l,timeout=60000)
            await asyncio.sleep(2)
            print("company :", l)
            html_content = await page.content()
            soup = BeautifulSoup(html_content, "html.parser")
            company_name = soup.find_all('h1', class_='font-extralight')
            Tagline = soup.find('div', class_='text-xl')
            Description = soup.find('p', class_='whitespace-pre-line')
            Batch = ""
            Company_Type = soup.find_all('div', class_='mr-[6px] h-3 w-3 rounded-full bg-green-500')
            Industry_tags = []
            industry_types = soup.find_all('a')
            for i in industry_types:
                if 'industry' in i.get('href'):
                    Industry_tags.append(i.text.strip())
            tags = soup.find_all('div',
                                 class_='yc-tw-Pill rounded-sm bg-[#E6E4DC] uppercase tracking-widest px-3 py-[3px] text-[12px] font-thin')
            Website_URL = soup.find_all('a', class_='mb-2 whitespace-nowrap md:mb-0')
            card = soup.find_all('div', class_='flex flex-row justify-between')
            # print(card)
            carditems = []
            for a in card:
                if a.text and a.text.startswith('Founded:') or a.text.startswith('Team Size') or a.text.startswith('Location'):
                    try:
                        # Attempt to split and extract text
                        text = a.text.split(':')[1].strip()
                        if text:
                            carditems.append(text)
                        else:
                            carditems.append('None')
                    except IndexError:
                        # Handle cases where there's no colon
                        carditems.append('None')
            # print(carditems)
            Founded_Year, Team_size, Location_cmp = carditems[:3]
            # Founded_Year=int(Founded_Year)
            # Team_size=int(Team_size)
            # print(Founded_Year, Team_size, Location_cmp)
            LinkedIn_profile = soup.find('a', class_='inline-block w-5 h-5 bg-contain bg-image-linkedin')
            Twitter_handle = soup.find('a', class_='inline-block w-5 h-5 bg-contain bg-image-twitter')
            Facebookpage = soup.find('a', class_='inline-block w-5 h-5 bg-contain bg-image-facebook')
            Crunchbase_profile = soup.find('a', class_='inline-block w-5 h-5 bg-contain bg-image-crunchbase')
            Founders = soup.find_all('div', class_='flex flex-row items-center gap-x-3')
            Brief = soup.find_all('p', class_='prose max-w-full whitespace-pre-line')
            Founder_linkedin = soup.find_all('a', class_='inline-block h-5 w-5 bg-contain bg-image-linkedin')
            Founder_twitter = soup.find_all('a', class_='inline-block h-5 w-5 bg-contain bg-image-twitter')
            tag = []
            Industry_Type = tags[0].text.strip()
            for t in tags:
                tag.append(t.text.strip())
            founders = []
            for f in Founders:
                if f:
                    Founder_name = f.find("div", class_="font-bold").text.strip()
                    founders.append(Founder_name)
                else:
                    founders.append(None)
            if Founder_linkedin:
                for a in Founder_linkedin:
                    founder_linkedin.append(a['href'])
            else:
                for i in range(len(founders)):
                    founder_linkedin.append('None')
            if Founder_twitter:
                for a in Founder_twitter:
                    founder_twitter.append(a['href'])
            else:
                for i in range(len(founders)):
                    founder_twitter.append('None')
            if Brief:
                for b in Brief:
                    if b.text:
                        founder_description.append(b.text.strip().split('.')[0])
                    else:
                        founder_description.append("None")
            else:
                for i in range(len(founders)):
                    founder_description.append("None")
            founders_list = []
            print(founder_twitter)
            for i in range(len(founders)):
                # print(founders[i])
                founfer_each = {'name': founders[i],
                                'desc': founder_description[i] or None,
                                'linked in': founder_linkedin[i] or None,
                                # 'twitter': founder_twitter[i] or None,
                                # 'twitter':founder_twitter[i] or None
                                }
                # print(founfer_each)
                founders_list.append(founfer_each)
            # print(founders_list)
            name = company_name[0].text.strip()
            tagline = Tagline.text.strip()
            description = Description.text.strip()
            company_type = Industry_Type
            industry_tag = Industry_tags
            web_url = Website_URL[0].text.strip()
            if LinkedIn_profile:
                linkedin = LinkedIn_profile.get('href')
            else:
                linkedin = 'None'
            if Facebookpage:
                facebook = Facebookpage.get('href')
            else:
                facebook = 'None'

            if Twitter_handle:
                twitter = Twitter_handle.get('href')
            else:
                twitter = 'None'

            if Crunchbase_profile:
                cruchbase = Crunchbase_profile.get('href')
            else:
                cruchbase = 'None'
            company_details_list={'name':name or None,'tagline':tagline or None,'description':description or None,'location':Location_cmp,'company_type':company_type or None,'industry_tags':industry_tag or None,'website':Website_URL[0].text.strip() or None,'founded':Founded_Year or None,'team_size':Team_size}
            social_media = {'facebook': facebook, 'twitter': twitter, 'crunchbase': cruchbase, 'linkedin': linkedin}
            print('details collected for :',l)
            new_compny_row = [{'name': name or None, 'Tagline': tagline or None, 'Description': description or None,'Location':Location_cmp,
                               'Company_Type': company_type or None, 'Industry_Tags': industry_tag or None,
                               'WEB Url': Website_URL[0].text.strip() or None,'Founded Year':Founded_Year,'Team size':Team_size, 'social_profiles': social_media or None,'founders':founders_list}]
            new_compny_row2=[{'company':company_details_list,'social_profiles':social_media,'founders':founders_list}]


            # df_to_founder = pd.concat([df_to_founder, pd.DataFrame(new_founder_row)], ignore_index=True)
            df_to_company = pd.concat([df_to_company, pd.DataFrame(new_compny_row2)], ignore_index=True)
            data2={'company':company_details_list,'social_profiles':social_media,'founders':founders_list}
            with open("YCOutput_Json2.json", "a") as f:
                json.dump(data2, f, indent=4)
                if not os.path.getsize("YCOutput_Json2.json") == len(data2) * 4 + 2:  # Assuming 4 spaces per indent
                    f.write(",")

            df_to_company.fillna('Null',inplace=True)

            df_to_company.to_csv('cmp_details_23.csv', index=False)

        await browser.close()




asyncio.run(main())