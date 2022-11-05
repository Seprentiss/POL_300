import web_scrape
from gradescope_utils.autograder_utils.decorators import weight,partial_credit,number
import unittest
from bs4 import BeautifulSoup
import pandas as pd
import requests

class TestCases(unittest.TestCase):
    @weight(100)
    def test_web_scrape(self):
        print("running test setup")
        base_df = pd.DataFrame(columns=["Year", "District", "Amount", "Candidates", "Average"])

        for i in range(1, 101):

            url = "https://ballotpedia.org/Indiana_House_of_Representatives_District_" + str(i)

            page = requests.get(url)

            if (page.status_code != 200):
                print("Error: Not able to obtain web page!")
                continue

            soup = BeautifulSoup(page.content, 'lxml')
            table = soup.find("table", class_="cftable bptable")

            df = pd.read_html(str(table), header=1, index_col=False)[0]
            df['District'] = i
            df.drop(df.tail(1).index, inplace=True)
            base_df = pd.concat([base_df, df], ignore_index=True)

        base_df['State'] = "Indiana"
        base_df['Chamber'] = "House of Representatives"

        columnsTitles = ['Amount', 'Average', 'Chamber', 'Candidates', 'District', 'State', 'Year']
        correct_df = base_df.reindex(columns=columnsTitles)

        print("test setup complete")

        error = "Data Frames Don't Match!"



        self.assertTrue(correct_df.equals(web_scrape.collectCampaignContributions()), msg=error)

if __name__ == '__main__': unittest.main(argv=[''], exit=False)