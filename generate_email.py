first, last, first_initial, last_initial = "", "", "", ""

formats = { "first": "", "last":"", "first_initial":"", "last_initial":""}

companies = {
    "splunk": ["{0[first_initial]}{1[last]}@splunk.com", "{0[first]}.{1[last]}@splunk.com", "{0[first]}@splunk.com"],
    "twilio": ["{0[first_initial]}{1[last]}@twilio.com", "{0[first]}.{1[last]}@twilio.com"],
    "okta": ["{0[first]}.{1[last]}@okta.com", "{0[first_initial]}{1[last]}@okta.com"],
    "paypal": ["{0[first_initial]}{1[last]}@paypal.com", "{0[first]}.{1[last]}@paypal.com"],
    "nvidia": ["{0[first_initial]}{1[last]}@nvidia.com", "{0[first]}{1[last_initial]}@nvidia.com"],
    "autodesk": ["{0[first]}.{1[last]}@autodesk.com"],
    "slack": ["{0[first_initial]}{1[last]}@slack.com"],
    "capital": ["{0[first]}.{1[last]}@capitalone.com"],
    "zendesk": ["{0[first_initial]}{1[last]}@zendesk.com"],
    "square": ["{0[first_initial]}{1[last]}@squareup.com", "{0[first]}{1[last]}@squareup.com", "{0[first]}@squareup.com"],
    "qualcomm": ["{0[first_initial]}.{1[last]}@qualcomm.com"],
    "unity": ["{0[first]}{1[last_initial]}@unity3d.com"],
    "geotab": ["{0[first]}{1[last]}@grabyo.com"],
    "brex": ["{0[first_initial]}{1[last]}@brex.com", "{0[first]}@brex.com"],
    "tophat": ["{0[first]}.{1[last]}@tophat.io", "{0[first]}@tophat.io"],
    "pension": ["{0[first]}_{1[last]}@ottp.com"],
    "interac": ["{0[first_initial]}{1[last]}@interac.com"],
    "wish": ["{0[first]}@wish.com"],
    "zynga": ["{0[first]}{1[last]}@zynga.com"],
    "state": ["{0[first_initial]}{1[last]}@statestreet.com"],
    "qualcomm": ["{0[first_initial]}{1[last]}@qualcomm.com"],
    "vena": ["{0[first_initial]}{1[last]}@venasolutions.com"],
    "coursera": ["{0[first_initial]}{1[last]}@coursera.org"],
    "databricks": ["{0[first]}.{1[last]}@databricks.com", "{0[first]}@databricks.com"],
    "thescore": ["{0[first]}.{1[last]}@thescore.com"],
    "aviva": ["{0[first]}.{1[last]}@aviva.com"],
    "mark43": ["{0[first]}.{1[last]}@mark43.com"],
    "intact": ["{0[first]}{1[last]}@intact.net"],
    "nanoleaf": ["{0[first]}@nanoleaf.me"],
    "wealthsimple": ["{0[first_initial]}{1[last]}@wealthsimple.com", "{0[first]}@wealthsimple.com"],
    "sunlife": ["{0[first]}.{1[last]}@sunlife.com"],
    "coveo": ["{0[first_initial]}.{1[last]}@coveo.com"],
    "publicis": ["{0[first]}.{1[last]}@publicisgroupe.com"],
    "pagerduty": ["{0[first_initial]}{1[last]}@pagerduty.com"],
    "bentley": ["{0[first]}.{1[last]}@bentley.com"],
    "nasdaq": ["{0[first]}.{1[last]}@nasdaq.com"],
    "block": ["{0[first_initial]}{1[last]}@blockandco.com"],
}

def generate_email(name, company):
    clist = company.split(" ")
    emails = []
    for c in clist:
        if companies.get(c):
            new_first = name.split(" ")[0]
            new_last = name.split(" ")[-1]
            new_first_initial = new_first[0]
            new_last_initial = new_last[0]

            formats["first"]=new_first
            formats["last"]=new_last
            formats["first_initial"]=new_first_initial
            formats["last_initial"]=new_last_initial

            for i in companies.get(c):
                email = i.format(formats, formats)
                emails.append(email)
            
            return emails
    
    if len(emails) == 0:
        emails = ["Company not recognized!"]
        return emails
