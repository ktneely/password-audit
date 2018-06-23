# Identify the Accounts with Weak Passwords

## Extract active employee and service accounts from Active Directory

This procedure performs two queries against Active directory, extracting 1) a list of active employee accounts and 2) a list of active non-employee accounts in a file called ‘emps.csv’.  The non-employee accounts list includes, but is not limited to, service accounts, contractors, and privileged administrator accounts.  This is saved to non-emps.csv

### PowerShell queries

When the password audit is complete, and it's time to inform the owners of weak passwords that they need to change, extract the currently active accounts from AD.  Queries such as the following will return the results into the files named above.  The exact query may be different, depending upon the properties for your LDAP objects.

```
get-aduser -Filter {(EmployeeID -like "*") -and (enabled -eq $true)} -properties * | Select SAmAccountName,GivenName,Surname,mail,Department |Export-Csv .\emps.csv -NoTypeInformation

get-aduser -Filter {(EmployeeID -notlike "*") -and (enabled -eq $true)} -properties * | Select SAmAccountName,GivenName,Surname,mail,Department |Export-Csv .\non-emps.csv -NoTypeInformation 
```

## Compare active accounts with discovered passwords

This procedure runs a script called usermatch.py (NOTE:  Usermatch is written in python and available in the directory of password tools, and also at https://github.com/ktneely/forensics ) which takes the currently active accounts extracted in the previous step, compares them with the accounts for which weak passwords have been discovered, and then generates a list of accounts that need to change the password.  Weak passwords belonging to inactive accounts are ignored because the account is disabled and cannot be used.

### Execute usermatch.py

`Usermatch.py` takes four arguments on the command line:

1. The extracted usernames and hashes file,

2. the hashes file with the cracked passwords,

3. list of employees extracted from Active Directory, and

4. list of non-employee accounts extracted from Active Directory.

 
Example:

`./usermatch.py ~/passwords/ntpass.out ~/passwords/hashcat.pot ~/passwords/emps.csv ~/passwords/non-emps.csv`

## Force the identified users to change the weak password

Once the accounts with weak passwords have been identified, they need to be changed.  Use whatever is reasonable for your environment to force the changes.


## Analyze the cracked passwords 
