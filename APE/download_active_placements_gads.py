import sys
import pandas as pd
from googleads import adwords
import io

output = io.StringIO()

def downloading_gads_report(client):
  """Downloads the Google Ads Report
    
        This methods downloads the report into the csv.
        
        You can provide a file object to write the output to sys with sys.stdout 
        to write the report to the screen.
        report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', sys.stdout, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)"""
  report_downloader = client.GetReportDownloader(version='v201809')

  report_query = (adwords.ReportQueryBuilder()
                  .Select('CampaignId', 'CampaignName', 'AdGroupId', 'Impressions', 'Clicks', 'Ctr', 'Conversions',
                          'Cost','Domain')
                  .From('AUTOMATIC_PLACEMENTS_PERFORMANCE_REPORT')
                  .During('LAST_7_DAYS')
                  .Build())

  report_downloader.DownloadReportWithAwql(
      report_query,
      'CSV',
      output,
      skip_report_header=True,
      skip_column_header=False,
      skip_report_summary=False)

  output.seek(0)
  df = pd.read_csv(output)
  df.to_csv("downloaded-active-placements-report.csv")







