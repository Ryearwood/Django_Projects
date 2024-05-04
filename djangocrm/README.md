Basic Django CRM Website to perform CRUD operations on User Accounts.

## Installation

```
> brew install mysql
> brew services restart mysql
> mysql.server start
> mysql_secure_installation
```
 If `Access Denied` issue is raised: 
 
 Check [here for information](https://stackoverflow.com/questions/41645309/mysql-error-access-denied-for-user-rootlocalhost) 
```
# Set password for root user
> sudo mysql -u root -p"
```
 If `venv` not installed, run this before the above.
```
> pip install venv
```
else:
```
> python -m venv venv
> source /venv/bin/activate
> pip install -r requirements
```


> Open and update the password fields in the `djangocrm/settings.py` and the `mydb.py` files respectively, to the password you set up during the mysql installation process.

## Launch Server and Connect MySQL Database

```
> cd ~/djangocrm
> python mydb.py
> python manage.py migrate
> python manage.py runserver
```
Leave Terminal Window Running for persistence as this is a `Local-Only` project.
