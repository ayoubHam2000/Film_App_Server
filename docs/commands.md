## commands ##

pip3 install virtualenv
python3 -m venv env_name
source env/bin/activate
deactivate

## github ##

git init 
git remote add origin [URL]
git add .
git commit -m "first commit"
git push -u origin master

git branch -M main

git log --oneline
git checkout -b [branch] [6e559cb]

git branch -m ayoub Main
git fetch origin
git branch -u origin/Main Main
git remote set-head origin -a

-- Create the branch on your local machine and switch in this branch :
$ git checkout -b [name_of_your_new_branch]
-- Push the branch on github :
$ git push origin [name_of_your_new_branch]
-- You can see all the branches created using :
$ git branch -a
-- Delete a branch on your local filesystem :
$ git branch -d [name_of_your_new_branch]
-- Delete the branch on github :
$ git push origin :[name_of_your_new_branch]

**merge branch with master**
git checkout [branch]
git merge master


## django ##
pip install django
django-admin startproject [projectName] [path]

py manage.py migrate => sync the models with the data base
py manage.py makemigrations => create the shema
py manage.py migrate --run-syncdb
py manage.py createsuperuser
py manage.py dbshell
py manage.py shell
py manage.py startapp appName

py manage.py migrate your_app zero
py manage.py migrate --fake <app-name> zero
py manage.py makemigrations <app-name>
py manage.py migrate <app-name>

pip install -r  requirement.txt
