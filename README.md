
# CRUD Task

This assignment is to perform the CRUD operations i.e, Create, Read, Update, Delete.
## Summary

In this assignment we have used MySQL database where `.sql` script file is present corresponding to the `crudproject` folder.

Import it to your MySQL database.




## Python (Run locally)

Create a Virtual Environment within the `crudproject` folder:

```bash
  python -m venv venv
```


Activate the Virtual Environment:

```bash
    venv/Scripts/activate
```


Install the given requirements.txt using cmd:

```bash
    pip install -r requirements.txt
```

After the installation get completed, Start the server:

```bash
    python manage.py runserver
```


Run the server locally on browser:

```bash
    http://127.0.0.1:8000/show
```

## Explaination

After the server get run successfully you can see the details present in the table having columns: `Title, Description, Status, Edit (with icon), Delete (with icon)`

- Add Task
On Top right corner I have added `Add Task` button on which it will pop up modal with `fields (Title, Description, Status (dropdown))` in it, that will help us to add new task that we are showing in table.


- Edit Task
On Edit icon button we can update any field if required using the ID

- Delete Task
On Delete icon button we can delete any row using the ID

