from APE.send_domains_to_OR_api import send_domains_to_OPR_df
import pandas as pd

def attach_OPR_metrics_to_original_file(opr_api_key):
    """Attaches OPR Metrics to original Google Ads Report"""
    api_result_df = send_domains_to_OPR_df(opr_api_key)
    ads_report_df = pd.read_csv('downloaded-active-placements-report.csv')
    df_merge = pd.merge(api_result_df, ads_report_df, on='Domain', how='outer')
    df_merge.sort_values(by='page_rank_decimal', ascending = False)
    delete_total_row = df_merge[df_merge['Domain'] == ' --'].index
    df_merge.drop(delete_total_row, inplace=True)
    df_merge.to_csv('active-placements-plus-domains-stats.csv')
    return df_merge
    
def extract_domains_to_exclude(opr_api_key):
    """Extracts Domains that are qualified to be excluded. Qualifiers for exclusion are set below in the dataframe"""
    df_with_all_stats = attach_OPR_metrics_to_original_file(opr_api_key)        
    df_extracted = df_with_all_stats.loc[df_with_all_stats['page_rank_decimal'].values <= 4.5]
    df_extracted = df_with_all_stats.loc[df_with_all_stats['rank'].values >= 50000]
    df_extracted = df_with_all_stats.loc[df_with_all_stats['Impressions'].values > 1500] #optional for impression based optimization
    df_extracted = df_with_all_stats.loc[df_with_all_stats['Conversions'].values == 0] #optional for conversion based optimization
    #df_extracted = df_with_all_stats.loc[df_with_all_stats['ANYTHINGELSE'].values =<> ] #placeholder for any other qualification
    df_extracted.to_csv('REVIEW-domains-stats-that-will-be-excluded.csv')
    domains_to_exclude = df_extracted['Domain']
    return domains_to_exclude
    
                                  

