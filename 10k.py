import os, re, pyperclip, pprint

revregex = re.compile(r"revenue recognition\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*\n+.*", re.IGNORECASE) #compile creates a match object, BUT if you use multiple () it creates tuples. Right now, this matches to the next /n, find out logic?
text = r'''CRITICAL ACCOUNTING POLICIES
Our previous discussion and analysis of our financial condition and results of operations are based upon our Consolidated
Financial Statements, which have been prepared in accordance with accounting principles generally accepted in the United
States of America. The preparation of these financial statements requires us to make estimates and judgments that affect
the reported amounts of assets, liabilities, revenues and expenses and related disclosure of contingent assets and liabilities.
Note 1 — Summary of Significant Accounting Policies in the accompanying Notes to the Consolidated Financial Statements describes
the significant accounting policies and methods used in the preparation of our Consolidated Financial Statements.
We believe the estimates, assumptions and judgments involved in the accounting policies described below have the greatest
potential impact on our Consolidated Financial Statements, so we consider these to be our critical accounting policies and
estimates. Management has reviewed and discussed these critical accounting policies with the Audit & Finance Committee of the Board of Directors.
These policies require that we make estimates in the preparation of our Consolidated Financial Statements as of a given date.
Because of the uncertainty inherent in these matters, actual results could differ from the estimates we use in applying the
critical accounting policies. Within the context of these critical accounting policies, we are not currently aware of any reasonably
likely events or circumstances that would result in materially different amounts being reported.

REVENUE RECOGNITION
On June 1, 2018, we adopted Accounting Standards Update (ASU) No. 2014-09, Revenue from Contracts with Customers (Topic 606),
using the modified retrospective method of adoption. Prior to fiscal 2019, amounts have not been restated and continue to be reported in accordance with our
historical accounting policies. Our revenue recognition policies under Topic 606 are described

2020 FORM 10-K 46


Table of Contents


in the following paragraphs and references to prior period policies under Accounting Standard Codification Topic 605 — Revenue Recognition,
are included below in the event they are substantially different.
Revenue transactions associated with the sale of NIKE Brand footwear, apparel and equipment, as well as Converse products, comprise a single
performance obligation, which consists of the sale of products to customers either through wholesale or direct to consumer channels. We satisfy
the performance obligation and record revenues when transfer of control has passed to the customer, based on the terms of sale. A customer is
considered to have control once they are able to direct the use and receive substantially all of the benefits of the product. Transfer of control
passes to wholesale customers upon shipment or upon receipt depending on the country of the sale and the agreement with the customer. Control
passes to retail store customers at the time of sale and to substantially all digital commerce customers upon shipment. Prior to fiscal 2019,
 the requirements for recognizing revenue were met upon delivery to the customer. The transaction price is determined based upon the invoiced
 sales price, less anticipated sales returns, discounts and miscellaneous claims from customers. Payment terms for wholesale transactions depend
 on the country of sale or agreement with the customer and payment is generally required within 90 days or less of shipment to or receipt by the
 wholesale customer. Payment is due at the time of sale for retail store and digital commerce transactions.
As part of our revenue recognition policy, consideration promised in our contracts with customers is variable due to anticipated reductions such
as sales returns, discounts and miscellaneous claims from customers. We estimate the most likely amount we will be entitled to receive and record
an anticipated reduction against Revenues, with an offsetting increase to Accrued liabilities at the time revenues are recognized. The estimated
cost of inventory for product returns is recorded in Prepaid expenses and other current assets on the Consolidated Balance Sheets. Prior to fiscal
2019, reserve balances were reported net of the estimated cost of inventory for product returns and recognized within Accounts receivable, net for
wholesale transactions and Accrued liabilities for our direct to consumer business, on the Consolidated Balance Sheets.
The provision for anticipated sales returns consists of both contractual return rights and discretionary authorized returns. Provisions for post-invoice
sales discounts consist of both contractual programs and discretionary discounts that are expected to be granted at a later date.
Estimates of discretionary authorized returns, discounts and claims are based on (1) historical rates, (2) specific identification of outstanding
returns not yet received from customers and outstanding discounts and claims and (3) estimated returns, discounts and claims expected but not yet
finalized with customers. Actual returns, discounts and claims in any future period are inherently uncertain and may differ from estimates recorded.
If actual or expected future returns, discounts or claims were significantly different than reserves established, a reduction or increase to net
revenues would be recorded in the period in which such determination was made.
Refer also to Note 1 — Summary of Significant Accounting Policies and Note 16 — Revenues for additional information in the accompanying Notes
to the Consolidated Financial Statements.'''

matches = [] #this is a list
for groups in revregex.findall(text): #in each of the match object's findall(text) iterations, find the string of every match
    revmatch = groups #set revmatch to be the counter variable
    matches.append(revmatch) #adds items to the end of a list
#finalstr = ''.join(matches)
#print(finalstr)

mo1 = revregex.search(text) #seach returns a match object of the first match, this might be better?
pprint.pp(mo1.group())
