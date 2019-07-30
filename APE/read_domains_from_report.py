import pandas as pd

def read_downloaded_domains():
    """This method just reads the domains from the file and adds them to a new file extracted-domains.csv"""
    read_domains = pd.read_csv("downloaded-active-placements-report.csv", usecols=['Domain'])
    read_domains.to_csv("extracted-domains.csv")


