"""
Initiliazing the Excluder 

"""
from googleads import adwords

adwords_client = adwords.AdWordsClient.LoadFromStorage()
#The Google Ads client is defined within the googleads.yaml file from a default location. 

opr_api_key = 'k4o0gkwgwg8w840scg40w4kg0kk80gk884ssgkkw'

class ValidationError(Exception):
    def __init__(self, message, errors):
       super().__init__(message)
       self.errors = errors

"""
What follows is some kind of control flow. The methods are found in the APE Folder. 
Remove the if and inputs if you want to run everything automatically.
"""

first_choice = input("Are you ready to run the excluder (Y/N): ")

if first_choice in ['y', 'Y']:
    second_choice = input('Ready to download active placements from your Google Ads Account? ')
else:
    raise ValidationError("Why did you run this in the first place!?", "Error: Need confirmation to continue!")
    
    
if second_choice  in ['y', 'Y']:
    from APE.download_active_placements_gads import downloading_gads_report
    downloading_gads_report(adwords_client)
    print("\n -- SUCCESS: Check your working folder for the 'Active Placements Report.csv' file  \n")
else:
    raise ValidationError("This will not work if you dont connect to your Google Ads Account!?", "Error: Need confirmation to continue!")

third_choice = input("\n Please check the domains and stats and press Y when ready to proceed. ")

if third_choice  in ['y', 'Y']:
    from APE.read_domains_from_report import clean_report
    clean_report()
    from APE.read_domains_from_report import read_downloaded_domains
    read_downloaded_domains()
    print("\n -- SUCCESS: The domains are now extracted! Check the 'Extracted Placements.csv' file!  \n")
else: 
    raise ValidationError("You'll have to redo all steps when you're ready to finish this!", "Error: Need confirmation to continue!")
    
forth_choice = input('\n When ready press Y to send them to Open Page Rank API and retrieve page ranks. Ready? \n')

if forth_choice in ['y', 'Y']:
    from APE.send_domains_to_OR_api import domains_to_list, send_domains_to_OPR_df
    
    domains_to_list()
    send_domains_to_OPR_df(opr_api_key)

    from APE.process_api_results import attach_OPR_metrics_to_original_file, extract_domains_to_exclude
    
    attach_OPR_metrics_to_original_file(opr_api_key)
    
    print("\n -- SUCCESS: The domain stats have been returned and attached to the file 'REVIEW Placements plus Page Ranks Stats.csv'! Review it. \n")
else: 
    raise ValidationError("You'll have to redo all steps when you're ready to finish this!", "Error: Need confirmation to continue!")

fifth_choice = input('\n Ready to see which domains are selected to be excluded (Y/N)? \n **The domains qualifications are set in process_api_result.py file. Proceeding will create a file with domains to exclude and print them out in the terminal. Ready? ')

if fifth_choice  in ['y', 'Y']:
    print('Domains to exclude: %s' % extract_domains_to_exclude(opr_api_key))
else:
    raise ValidationError("Tweak your qualifications and redo all steps if need be.", "Error: Need confirmation to continue!")

sixth_choice = input('\n Ready to send the above domains to Google Ads & Exclude them (Y/N): ')

if sixth_choice  in ['y', 'Y']:
    domains_to_exclude = extract_domains_to_exclude(opr_api_key)
    domains_to_exclude = domains_to_exclude.values.tolist()

    from APE.send_domains_exclude_gads_api import excluding_domains_gads, display_excluded_domains
    excluding_domains_gads(adwords_client, domains_to_exclude)

    print('\n -- SUCCESS: The placements have been excluded in Google Ads! Check the file "Placements Qualified for Exclusion.csv" for details!')

    print('\n \n -- -- And thats it. Double Check Google Ads account that these have been indeed excluded! \n \n')    

else:
    raise ValidationError("When you're ready for the final step you'll have to redo all of them again!", "Error: Need confirmation to continue!")
