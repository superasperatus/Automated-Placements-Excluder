"""
Initiliazing the Excluder 

"""
from googleads import adwords

adwords_client = adwords.AdWordsClient.LoadFromStorage()
#The Google Ads client is defined within the googleads.yaml file from a default location. 

opr_api_key = 'k4o0gkwgwg8w840scg40w4kg0kk80gk884ssgkkw'

"""
What follows is some kind of control flow. The methods are found in the APE Folder. 
Remove the if and inputs if you want to run everything automatically.
"""

first_choice = input("Are you ready to run the excluder (Y/N): ")

if "y" or 'Y' in first_choice:
    second_choice = input('Ready to download active placements from your Google Ads Account? ')
else:
    print('Why did you run this in the first place then!? ')
    
if "y" or 'Y' in second_choice:
    from APE.download_active_placements_gads import downloading_gads_report
    downloading_gads_report(adwords_client)
    print("\n -- SUCCESS: Check your working folder for the Automatic placements report.csv file  \n")
else:
    print('This will not work if you dont connect to your Google Ads Account!')

third_choice = input("\n Please check the domains and stats and press Y when ready to proceed. ")

if "y" or 'Y' in third_choice:
    from APE.read_domains_from_report import clean_report
    clean_report()
    from APE.read_domains_from_report import read_downloaded_domains
    read_downloaded_domains()
    print("\n -- SUCCESS: The domains are now extracted! Check the extracted-domains.csv file!  \n")
else: 
    print("You'll have to redo all steps when you're ready to finish this!")

forth_choice = input('\n When ready press Y to send them to Open Page Rank API and retrieve page ranks. Ready? \n')

if 'y' or 'Y' in forth_choice:
    from APE.send_domains_to_OR_api import domains_to_list, send_domains_to_OPR_df
    domains_to_list()
    send_domains_to_OPR_df(opr_api_key)

    from APE.process_api_results import attach_OPR_metrics_to_original_file, extract_domains_to_exclude
    attach_OPR_metrics_to_original_file(opr_api_key)
    
    print('\n -- SUCCESS: The domain stats have been returned and attached to the file active-placements-plus-domains-stats! Review it. \n')
else: 
    print("You'll have to redo all steps when you're ready to finish this!")

fifth_choice = input('\n Ready to see which domains are selected to be excluded (Y/N)? \n **The domains qualifications are set in process_api_result.py file. Proceeding will create a file with domains to exclude and print them out in the terminal. Ready? ')

if 'y' or 'Y' in fifth_choice:
    print('Domains to exclude: %s' % extract_domains_to_exclude(opr_api_key))
else:
    print('Tweak your qualifications and redo all steps if need be.')

sixth_choice = input('\n Ready to send the above domains to Google Ads & Exclude them (Y/N): ')

if 'y' or 'Y' in sixth_choice:
    domains_to_exclude = extract_domains_to_exclude(opr_api_key)
    domains_to_exclude = domains_to_exclude.values.tolist()

    from APE.send_domains_exclude_gads_api import excluding_domains_gads, display_excluded_domains
    excluding_domains_gads(adwords_client, domains_to_exclude)

    print('\n -- SUCCESS: The placements above have been excluded in Google Ads: %s' % display_excluded_domains(adwords_client, domains_to_exclude))

    print('\n \n -- -- And thats it. Double Check Google Ads account that these have been indeed excluded! \n \n')    

else:
    print("When you're ready for the final step you'll have to redo all of them again!")