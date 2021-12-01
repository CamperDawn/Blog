# Blog
Blog project for the INFORMATORIO

Installation step
-

powershell terminal
```powershell
pip install virtualenv
mkdir Proyecto-TPF
cd .\Proyecto-TPF\
git clone [url_repositorio]
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
cd .\Server\
touch .env
```
bash terminal
```bash
pip install virtualenv
mkdir Proyecto-TPF
cd Proyecto-TPF/
git clone [url_repositorio]
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
cd Server/
touch .env
```
To close the virtual environment do `deactivate`

Create a database schema called `'blog'`  
.env file configuration:
```
DEBUG=True
SECRET_KEY=[THE SECRET KEY TO THE PROJECT]
PORT_DB=[YOUR DB PORT]
USER_DB=[YOUR DB USERNAME]
PASSWORD_DB=[YOUR DB PASSWORD]
```

Migrations
-

In the Proyect directory
```
cd Server
python manage.py makemigrations
python manage.py migrate
```
