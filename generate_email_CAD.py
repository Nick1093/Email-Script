first, last, first_initial, last_initial = "", "", "", ""

formats = { "first": "", "last":"", "first_initial":"", "last_initial":""}

companies = {
    "datadog": ["{0[first]}.{1[last]}@datadoghq.com"],
    "microsoft": ["{0[first]}.{1[last]}@microsoft.com"],
    "google": ["{0[first_initial]}{1[last]}@google.com"],
    "salesforce": ["{0[first_initial]}{1[last]}@salesforce.com"],
    "td": ["{0[first]}.{1[last]}@td.com"],
    "shopify": ["{0[first]}.{1[last]}@shopify.com"],
    "spotify": ["{0[first]}.{1[last_initial]}@spotify.com", "{0[first]}@spotify.com"],
    "amazon": ["{0[last]}.{1[first_initial]}@amazon.com", "{0[first]}.{1[last]}@amazon.com"],
    "rbc": ["{0[first]}.{1[last]}@rbc.com"],
    "scotiabank": ["{0[first]}.{1[last]}@scotiabank.com"],
    "qualcomm": ["{0[first_initial]}.{1[last]}@qualcomm.com"],
    "robinhood": ["{0[first]}.{1[last]}@robinhood.com", "{0[first]}@robinhood.com"],
    "grabyo": ["{0[first]}@grabyo.com"],
    "siltronic": ["{0[first]}.{1[last]}@siltronic.com"],
    "cisco": ["{0[first_initial]}.{1[last]}@cisco.com"],
    "hashicorp": ["{0[first_initial]}.{1[last]}@hashicorp.com", "{0[first]}@hashicorp.com"],
    "genentech": ["{0[first]}{1[last]}@gene.com", "{0[first]}.{1[last]}@gene.com", "{0[first]}{1[last_initial]}@gene.com", "{0[first_initial]}{1[last]}@gene.com"],
    "qualtrics": ["{0[first]}{1[last_initial]}@qualtrics.com", "{0[first_initial]}{1[last]}@qualtrics.com"],
    "linkedin": ["{0[first_initial]}{1[last]}@linkedin.com"],
    "paypal": ["{0[first_initial]}{1[last]}@paypal.com", "{0[first]}.{1[last]}@paypal.com"],
    "docusign": ["{0[first]}.{1[last]}@docusign.com"],
    "bloomberg": ["{0[first_initial]}{1[last]}@bloomberg.net"],
    "lyft": ["{0[first_initial]}{1[last]}@lyft.com", "{0[first]}@lyft.com", "{0[first]}.{1[last]}@lyft.com"],
    "databricks": ["{0[first]}.{1[last]}@databricks.com", "{0[first]}@databricks.com"],
    "tangerine": ["{0[first_initial]}{1[last]}@tangerine.ca"],
    "square": ["{0[first]}{1[last]}@squareup.com", "{0[first_initial]}{1[last]}@squareup.com", "{0[first]}@squareup.com"],
    "nintendo": ["{0[first]}.{1[last]}@nintendo.com"],
    "snap": ["{0[first_initial]}{1[last]}@snap.com", "{0[first]}.{1[last]}@snap.com", "{0[first]}@snap.com"],
    "league": ["{0[first_initial]}{1[last]}@league.com", "{0[first]}@league.com"],
    "wealthsimple": ["{0[first_initial]}{1[last]}@wealthsimple.com", "{0[first]}@wealthsimple.com"],
    "uber": ["{0[first]}@uber.com", "{0[first_initial]}{1[last]}@uber.com", "{0[first]}{1[last_initial]}@uber.com"],
    "bmo": ["{0[first]}.{1[last]}@bmo.com"]
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
