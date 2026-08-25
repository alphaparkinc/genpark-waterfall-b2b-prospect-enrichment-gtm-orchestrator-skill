from client import WaterfallB2bProspectEnrichmentGtmOrchestratorClient

def main():
    client = WaterfallB2bProspectEnrichmentGtmOrchestratorClient()
    res = client.run_waterfall_enrichment_flow('stripe.com', 'Head of AI Partnerships')
    print('GTM Campaign: ' + res['campaign_id'] + ' for ' + res['target_domain'])
    print('Decision Makers: ' + str(res['verified_decision_makers_found']) + ' (Email Deliverability: ' + str(res['work_email_deliverability_rate_pct']) + '%)')
    print('Providers: ' + ', '.join(res['waterfall_providers_queried']) + ' | CRM Synced: ' + str(res['crm_hubspot_salesforce_synced']))

if __name__ == '__main__':
    main()
