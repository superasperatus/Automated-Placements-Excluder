# Pladomate - Automated Placements Excluder 

Pladomate does 4 simple things:
1. Connects to your Google Ads Account and downloads active placements report for the past 7 days 
2. Extracts Domains and sends them to Open Page Rank API for page rank evaluation 
3. Attaches the results of the OPR API with the domain report 
4. Based on the set criteria it sends the domains to be excluded in Google Ads on the Account level

And these allow you to automatically evaluate all the placements where your ads showed in the past 7 days and if they're of low page rank or underperforming - you can exclude them from targeting options on the account level.


## The Pladomate Initializer 

The `Pladomate.py` is just a python/terminal based control file that provides some control and options for the script implementation. 

The future goal is to create a Flask based web app that will do this all in a browser with a nice UI. 


## On the Google Ads Client  

Google Ads Client - User & Account ID is set in the `googleads.yaml` file. 

Pladomate creates the Google Ads client int the `Pladomate.py` file in this line:

`adwords_client = adwords.AdWordsClient.LoadFromStorage()` 

The `LoadFromStorage` method takes the location of `googleads.yaml` as an argument. Empty argument, signifies that the method will search for the `googleads.yaml` file on the default location. 

Get an empty `googleads.yaml` file [here](https://github.com/googleads/googleads-python-lib/blob/master/googleads.yaml).


## On the Google Ads Active Placements Report

The report report definition is found in the `download_active_placements_gads.py`file. 

By default Pladomate downloads several metrics and account details for the past 7 days.

To edit the scope of the report edit the `ReportQueryBuidler()` method. 


## On Open Page Rank API 

OPR API is provided thanks to [DompCop.](https://www.domcop.com/openpagerank/documentation.)

It is the only free API I could find to get some stats on the domains rating and rank. 

I'd like to try and use SEMRush, MOZ or Ahrefs API but all three of them are not available for free. 


## Placements Evaluation criteria 

The whole script is prepared to exclude domains based on the:
1. Domain Page Rank or
2. Performance 

Evaluation criteria that define which domains are to be excluded can be found in the `process_api_results.py` file in `extract_domains_to_exclude` method: 

```
df_extracted = df_with_all_stats.loc[df_with_all_stats['page_rank_decimal'].values <= 4.5]
df_extracted = df_with_all_stats.loc[df_with_all_stats['rank'].values >= 50000]
df_extracted = df_with_all_stats.loc[df_with_all_stats['Impressions'].values > 1500] 
df_extracted = df_with_all_stats.loc[df_with_all_stats['Conversions'].values == 0] 
```

The `df_extracted` is the Pandas dataframe that includes all the downloaded stats from Google Ads and ranks from OPR. 

Any other custom qualification can be added with: 

`df_extracted = df_with_all_stats.loc[df_with_all_stats['ANYTHINGELSE'].values =<> ]`


## Note Placements are Excluded on Account Level

Yes beware, the scripts excludes placements on the Account Level in defined Google Ads client. 

All tweaks, contributions and enhancements are welcomed. 
