from bs4 import BeautifulSoup
import pandas as pd
import requests


def collectCampaignContributions():
    # Fill in the correct state
    state = "Indiana"
    # Fill in the correct state chamber. (Lower chamber of Indiana)
    chamber = "House of Representatives"

    print("running collectCampaignContributions")

    base_df = pd.DataFrame(columns=["Year", "District", "Amount", "Candidates", "Average"])

    for i in range(1, 101):


        url = "https://ballotpedia.org/Indiana_House_of_Representatives_District_" + str(i)
        print(url)
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

    base_df['State'] = state
    base_df['Chamber'] = chamber

    columnsTitles = ['Amount', 'Average', 'Chamber', 'Candidates', 'District', 'State', 'Year']
    correct_df = base_df.reindex(columns=columnsTitles)

    correct_df.to_csv("Indiana-House-of-Representatives-Campaign-Contributions")
    return correct_df

print(collectCampaignContributions())