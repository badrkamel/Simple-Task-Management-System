# Task Management System

### Run the following commands to get started:

```
git clone https://github.com/badrkamel/Simple-Task-Management-System.git
virtualenv env
```
#### Activate the virtual environment

Mac OS / Linux
```source env/bin/activate```

Windows
```.\env\Scripts\activate```

```
cd Simple-Task-Management-System
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# Overview

This project is a small task management.
It was built using Django and DRF and contains the following:

* Allows new accounts registration, login and logout.
* token-based authentication system.
* Each user can create edit delete any of his task.
* Each user can filter through his tasks (eg. Filter to show only uncompleted task).
* Calculate the ratio between complete and incomplete tasks and export it to a file in (CSV, Excel) format.

<a name="table-of-contents"></a>
## [Table of Contents](#table-of-contents)

In order to achieve all of these results, it is necessary to send the **_Authorization: Token_** with each link.

#### Note: Folder screenshots contains images for all operations.

* [Authentication](#auth)
  * Signup ```127.0.0.1:8000/accounts/register/```
  * Login ```127.0.0.1:8000/accounts/login/```
  
* [CRUD Operations](#crud)
  * All Tasks ```127.0.0.1:8000/me/all/```
  * Create Task ```127.0.0.1:8000/tasks/```
  * Retrieve specific task ```127.0.0.1:8000/tasks/id/``` Or ```127.0.0.1:8000/me/id/```
  * Update Task ```127.0.0.1:8000/tasks/id/```
  * Delete Task ```127.0.0.1:8000/tasks/id/```

* [Filter Tasks](#filter)
  * All Completed Tasks ```127.0.0.1:8000/me/completed/```
  * All Incompleted Tasks ```127.0.0.1:8000/me/incompleted/```
  

* [Export Data](#crud)
  * Export as CSV ```127.0.0.1:8000/export/csv/```
  * Export as XLS ```127.0.0.1:8000/export/xls/```
  
[Raseedi]: http://www.raseedi.co/


<a name="auth"></a>
<a name="all-tasks"></a>
<a name="crud"></a>
<a name="filter"></a>
<a name="export"></a>
