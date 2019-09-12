import pandas as pd

def clean_report():
    clean_report_df = pd.read_csv("Automatic placements report.csv", header=None)
    clean_report_df = clean_report_df.rename(columns=clean_report_df.iloc[2])
    clean_report_df = clean_report_df.iloc[3:]
    clean_report_df = clean_report_df.iloc[:35]
    clean_report_df.to_csv("Automatic placements report.csv")
    
def read_downloaded_domains():
    """This method just reads the domains from the file and adds them to a new file extracted-domains.csv"""
    #read_domains = pd.read_csv("Automatic placements report.csv", usecols=['Domain']) - for my own API; bellow for Downloaded Report from Google Ads
    
    read_domains = pd.read_csv("Automatic placements report.csv", usecols=['Placement'])
    read_domains.to_csv("Extracted placements.csv")


