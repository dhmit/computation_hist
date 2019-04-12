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
1. Author name is inputted as Last (Suffix), First M.
1. If there is more than one author, separate them by ;
1. If there is an organization do not use any ; or , in the name
1. If there are letterheads indicating an organization, ex: Naval War College, please include 
that organization in the author field
1. If someone doesn't have a first name enter 'unknown' as first - e.g. "Boal, unknown"
1. If someone doesn't have a surname enter second name as unknown - e.g. "unknown, Elena"
1. If someone has name is not known at all enter unknown 

**title** required

**date** if unknown write nothing

**first_page** required

**last_page** required

**metadata_added** not in models

**doc_type** if unknown write "unknown"

**recipients** 

1. Name is listed as Last (Suffix.), First M.
1. Separate multiple recipients by semicolon.
1. If there is an organization do not use any ; or , in the name
1. If someone doesn't have a first name enter 'unknown' as first - e.g. "Boal, unknown"
1. If someone doesn't have a surname enter second name as unknown - e.g. "unknown, Elena"
1. If someone has name is not known at all enter unknown 

**cced**
1. If there is an organization do not use any ; or , 
1. If someone doesn't have a first name enter 'unknown' as first - e.g. "Boal, unknown"
1. If someone doesn't have a surname enter second name as unknown - e.g. "unknown, Elena"
1. If someone has name is not known at all enter unknown 

**notes** max character 191 - leave blank don't write none

##Box
Has a number 


##Folder
1. Folder name is the same name of the pdf file, **excluding** the raw and one of the connecting 
underscores. Ex: the foldername_short for "1_05_raw_morse_corr.pdf" should be "morse_corr".
1. Folder names is currently coded assuming all names are unique. The folder name is the column 
'foldername_short' in the csv


## Document
Must have a title


##Date
If the first number isn't '19' the date is not recorded


##Author
1. Looks for ; in field 
1. If there is no semi-colon then there is one name 
1. If there is no comma it interprets it as an organisation
1. Initials are interpreted as one first name



###Page
takes the filename as a string
page number


###Organization 
Must have a name
Doesn't need a Location

###Text
There is no data to put in text yet