#Information about the models

##For Data entry
allways use unknown lowercase where unknown is to be used


**Box** required

**Folder-number** required

**foldername_short** required

**foldername_fulll** required

**doc_id**required

**filename** required

**author**
1.If there is an organization do not use any ; or , 
2.If someone doesn't have a first name enter 'unknown' as first - e.g. "Boal, unknown"
3.If someone doesn't have a surname enter second name as unknown - e.g. "unknown, Elena"
4.If someone has name is not known at all enter unknown 

**title**required

**date** if unknown write none

**first_page** required

**last_page** required

**metadata_added** not in models

**doc_type** if unknown write "unknown"

**recipients** 

1.If there is an organization do not use any ; or , 
2.If someone doesn't have a first name enter 'unknown' as first - e.g. "Boal, unknown"
3.If someone doesn't have a surname enter second name as unknown - e.g. "unknown, Elena"
4.If someone has name is not known at all enter unknown 

**cced**
1.If there is an organization do not use any ; or , 
2.If someone doesn't have a first name enter 'unknown' as first - e.g. "Boal, unknown"
3.If someone doesn't have a surname enter second name as unknown - e.g. "unknown, Elena"
4.If someone has name is not known at all enter unknown 

**notes** max character 191

##Box
Has a number 


##Folder
Folder names is currently coded assuming all names are unique. The folder name is the column 
'foldername_short' in the csv


## Document
Must have a title


##Date
If the first number isn't '19' the date is not recorded


##Author
1. Looks for ; in field 
2. If there is no colon then there is one name 
3. If there is no comma it interprets it as an organisation
4. Initials are interpreted as one first name



###Page
takes the filename as a string
page number


##3Organization 
Must have a name
Doesn't need a Location

###Text
There is no data to put in text yet