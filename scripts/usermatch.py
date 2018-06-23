#!/usr/bin/python3

import sys
import csv

usage = "\n This script takes the raw data from password analysis \
and creates files with account and password combination, and also \
all the passwords in a text file for later analysis. \n \
\n You must specify four arguments on the command line:\n \
\t 1. your extracted usernames and hashes file,\n \
\t 2. the hashes file with the cracked passwords,\n \
\t 3. list of employees in csv format,\n \
\t 4. list of non-employee accounts in csv format. \n "

if len(sys.argv) < 5:
    print(usage)
    exit()

userfile = sys.argv[1]
passfile = sys.argv[2]
active_emps = sys.argv[3]
active_non_emps = sys.argv[4]

# Function to create a dictionary from the various data sources.  The
# function requires the following parameters: CSV datafile, delimeter
# used, quote character, item that should be used as the key as
# integer, and item that should be used as the value as integer

def makedict(accounts, delim, quote, k, v):
    with open(accounts, newline='') as f:
        data = csv.reader(f, delimiter=delim, quotechar=quote)
        mydict = {rows[k]:rows[v] for rows in data}
        return mydict

    
# Function takes the discovered passwords and checks against currently
# active accounts.
def liveaccounts(accounts, filename):
    results = open(filename, 'w')
    passwords = open('allpasswords.txt', 'a')
    for passkey in passdict:
        for account in accounts:
            try:
                if passkey == users[account]:
                    results.write(account + ',' + passdict[passkey] + '\n')
                    passwords.write(passdict[passkey] + '\n')
            except:
                KeyError
    results.close()
    passwords.close()

    
    
# Make dictionaries from the input files
users = makedict(userfile, ':', ' ', 0, 1)
passdict = makedict(passfile, ':', ' ', 0, 1)
emps = makedict(active_emps, ',', '"', 0, 3)
non_emps = makedict(active_non_emps, ',', '"', 0, 3)
# The extracted hashes from Active Directory are in the form of
# username:hash.  We want the hash to be the key for both
# dictionaries, so we need to flip the key:value pairs


# Create lists of the accounts with weak passwords that are still
# active in the user directory.  Remove previous version of the file
# first if the script has already been executed.
wipeout = open('allpasswords.txt', 'w') 
wipeout.close()
liveaccounts(emps, "weak-employee-accounts.csv")
liveaccounts(non_emps, "weak-service-accounts.csv")

