<h3>Models Writeup</h3>
DJango models are used to define the structure of stored data (in this case, the database of historical documents). They
form the means through which the Django web application can store and manage data. This writeup details my thoughts on 
which models could/should be built for the database, and how their structures could be defined.\
\
<b>We will want to have separate models for every object or group of related data.\
\
Some obvious models</b>

* Person
* Document
    * Fields:
        * Author
        * Title
        * Filename
        * Associated people (people mentioned in the document's content, people that it was sent to if it's a message of some
        kind, etc).
        * Tags? Some sort of keyword list that has to do with the content. This would allow database users to find documents
         associated

<b>Other possible models:</b> We could also use models to represent selection options (ways to categorize the documents).
* The type of document -- memos, proposal, budget, letter, etc.
* Year
* Author (different from 'people' because a document can be associated with a Person through the content as well).


<b>Things to think about for each model:</b>
* The model name
* Field names and types
* Methods and return types
* Relationships between the models
    * Their multiplicities
        * A document can have one or many associated authors while an author can have zero or many associated documents.
        * A document can have zero or many associated people (based on the content) while a Person can have zero or many associated documents

