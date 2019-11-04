from googleads import adwords
import sys

def excluding_domains_gads(adwords_client, domains_to_exclude):
    """Preparing domains set to exclude for Google's API"""
    excluding_api_criteria = []
    customer_negative_criterion_service = adwords_client.GetService(        
    'CustomerNegativeCriterionService', version='v201809')
    
    for item in domains_to_exclude:
        addition = {
            'xsi_type': 'Placement',
            'url': item  
        } 
        excluding_api_criteria.append(addition)

    operations = [{
        'operator': 'ADD',
        'operand': {
            'criterion': criterion
        }
    } for criterion in excluding_api_criteria]

    result = customer_negative_criterion_service.mutate(operations)
    return result


def display_excluded_domains(adwords_client, domains_to_exclude):
    """Displays the results of exclusion"""
    result = excluding_domains_gads(adwords_client, domains_to_exclude)
    for negative_criterion in result['value']:
        print('Placement ID "%s", and type "%s" '
        'was added as negative placement.' % (negative_criterion['criterion']['id'],
                    negative_criterion['criterion']['type']))