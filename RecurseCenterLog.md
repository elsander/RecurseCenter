### Recurse Center Log

##7/6/15:
#SQL project
* fixed outstanding bugs from before RC
* made everything lowercase
* converted times to integers for SQL
* got create statement to work
* added security to SQL commands

##7/7/15:
#SQL project
* got append statement to work
* got program to run with full restaurants file
#workshops: Git!
* installed Magit
* learned about pull requests and merges for Git
* changed default editor to emacs, ediff for merges
#other things
* read book about focusing data science process on questions and
  actionable results, not methods and the dataset itself

##7/8/15:
#SQL project
* tested SQL database, and got it to populate!
* read about possible algorithms
* realized that beta distribution will be difficult to interpret, did
some reading on prediction algorithms
#workshops: blogging with GitHub!
* learned how to make a GitHub pages site with jekyll

##7/9/15:
#SQL project
* Discussed options for analysis of distribution data: seems that
  logistic regression can work for multiple nominal categories, and
  could supplement this by considering results with star rating
  treated as continuous... linear or log odds link?
* Learned how to join tables! Will be useful for setting up a more
complex but simpler to query/interpret database
* Also learned that Yelp structured its data like crap. Refocusing on
implementing database for messy data. PostgreSQL vs SQLite?
* Learned basics of ORM for setting up and querying databases through
  Python. No more painstaking building of strings! Now just
  painstaking building of classes, then simpler times afterward.

#workshops: Git Internals!
* Learned about how Git stores files and changes, and how it thinks
about merges
* Learned about how Git treats remotes/clones (still a little shaky on
  this part)

#other things
* Presentations!
* Submitted no track changes pdf to PLoS, yay for me

##7/10/15:
#Job day: Make your own version control
* Made basic version control in Python
* init, commit, log, checkout, latest, print current, diff
* Next steps: status, print warnings, improve diff to include modified
files
#other things
* updated Git and got Magit running
* read through basic Magit tutorial
* learned about emacs keybindings and made shortcuts in my .emacs!

##Week 2, 7/13/15:
#SQL pairing:
* Got PostGreSQL set up (after much pain and suffering)
* created restaurants database from flattened JSON
* set up skeleton code for more complex schema

##7/14/15:
#SQL pairing:
* Got PostGreSQL configured with virtualenvwrapper, once again
* Got SQL CREATE TABLE to work
* populated restaurants table!
* parsed JSON data for categories, attributes, and restaurants info
* lots of reading about SQLalchemy API!

##7/15/15:
#SQL pairing:
* Learned things about sed, echo, and single vs double quotes in shell
* Single and double quotes treat escapes differently!
* fixed escaping in Yelp JSON
* Added reviews to database too! Database COMPLETE!!!

#Workshop: tmux
* tmux is a tool for windowing in the terminal
* It operates similarly to emacs, but with different keybindings
* Lets you close the terminal but keep memory of the session so it can
  be reopened, even if you have an ssh link!

##7/16/15:
#Prolog:
-go through a tutorial to understand basic syntax and logic
-try writing my own program for a little graph theory problem
-when is Prolog and efficient approach?

#Blogging:
-outline a blog post about SQLalchemy
-consider blog post on Git internals?

#other things
-write up a little thingy about pull requests and git config files, so
I don't forget it all!

##Things to look into at some point:
* https://www.kaggle.com/c/grasp-and-lift-eeg-detection
* https://www.coursera.org/learn/machine-learning/home/info
