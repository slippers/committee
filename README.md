# committee

generates a congressional committee report 

### setup

#### clone the project

git clone https://github.com/slippers/committee.git

#### refresh the data
 
git clone https://github.com/unitedstates/congress-legislators

put this script in the scripts folder. execute to refresh

```python

from subprocess import check_call, Popen

scripts = ['house_contacts.py',
'house_websites.py',
'senate_contacts.py',
'committee_membership.py',
'historical_committees.py',
'social_media.py',
'influence_ids.py',
]

for x in scripts:
    donkey = check_call(['python', x])
    print(x, donkey)

```

git clone https://github.com/TheWalkers/congress-legislators

this is where legislators-district-offices.yaml can be found
do not know how it gets generated.

now copy these refreshed yaml files into the committee project folder

* committee-membership-current.yaml
* legislators-current.yaml
* committees-current.yaml
* legislators-district-offices.yaml

#### execute the extract.py

python extract.py

this will compose a new dataset from the yaml files.  convert into markdown and then translate into html.

delete report.pickle to compose the data again.
