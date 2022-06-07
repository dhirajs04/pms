# Project Management System (PMS)

PMS is a RestAPI for managing Projects with milestone and individual tasks assigned to different users.

## Installation

1. clone the Repository
2. Create .env file in the project's root directory.
3. Copy the sample env contents into the .env file and put in the required details
4. Create a Virtual Environment and activate it.
5. Use the following command to install requirements

```python
pip install -r requirements.txt
```
*Note: You may need to replace pip with pip3 for python3.*

- Run the sever using following command
```python
python manage.py runserver
```
*Note: You may need to replace python with python3 for python3.*

#### Things to Note

- Migrations are turned off. Only initial default migrations need to be applied.
```python
python manage.py migrate
```
- To create Db tables, please use the file **db.sql** file in the project's root directory.

## License

[MIT](https://github.com/dhirajs04/pms/blob/master/LICENSE)