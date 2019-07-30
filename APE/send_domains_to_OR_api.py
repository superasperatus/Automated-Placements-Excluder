import pandas as pd 
from pandas.io.json import json_normalize 
import requests
import json


def domains_to_list():
    """This static methods reads the domains from the report and adds them to the list"""
    read_domains = pd.read_csv("downloaded-active-placements-report.csv", usecols=['Domain'])
    domains_list = read_domains["Domain"].tolist()
    while ' --' in domains_list: domains_list.remove(' --') 
    return domains_list    

def send_domains_to_OPR_df(opr_api_key):
    """This method sends domains to OPR APi and stores them into a dataframe."""
    domains_to_check = domains_to_list()
    headers = {'API-OPR': '%s' % opr_api_key}
    api_result_df = pd.DataFrame(None)    
    for item in domains_to_check:
        url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + item
        request = requests.get(url, headers=headers)
        api_result = request.json()
        api_result_norm = json_normalize(api_result, 'response')
        api_result_df = api_result_df.append(api_result_norm)

    api_result_df.sort_values(by='page_rank_decimal', ascending = False)
    
    api_result_df.rename(columns={'domain':'Domain'}, inplace=True)
    api_result_df = api_result_df.astype({'page_rank_decimal': float,
                                      'rank': float,
                                      'page_rank_integer': float})

    return api_result_df
