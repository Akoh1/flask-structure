####Intron Health Take Home Interview

Thank you for taking out time to work on this application. 

To get started, you should familiarize yourself with the structure of this application.

This is a Flask Application. Its HTML files live in the `app/templates` folder and its Javascript and CSS files should live 
in the `app/static` directory. This project uses the `Blueprint` structure provided natively by Flask. 

All Database Model Objects live in the `app/models.py` file. 

All migration files are in the `intron_health_migrations/versions` directory. `Alembic` is the tool used for database migrations. 

`instance/config.py` houses all configurations for this application.  

All required dependencies are in `requirements.txt` file. 

A virtual environment - `venv` - was created for this project as well.
 
####Getting Started
Before you get started, you should execute these exports:
```
export FLASK_APP=application.py;
export APP_SETTINGS=instance.config.IntronConfig;
export FLASK_ENV=development;
```

####Tips
To create a new versioned migration file, run:

```flask db migrate -m <name_of_file>```

To run an database upgrade operation, execute:

```flask db upgrade```

To run an database downgrade operation, execute:

```flask db downgrade```

To start the application, execute:

```flask run```

When you start the application, you can visit http://127.0.0.1:5000/home/all/users to ensure the application started correctly. 

###Instructions
Packaged with this application is a Spreadsheet named `user_unit_tenure.xlsx`. This file contains the name of user,  
the unit(s) they have worked in the past, and the number of years they spent in that unit. 

Also, in the database [`instance/intron_db.db`] (we are using sqlite for this), there is a list of users, their names, 
and their salaries in the `Users` table. 

N.B: The names on the spreadsheet matches the names in the `Users` table.

You are expected to write and design a feature where the spreadsheet is uploaded via an HTML form and its contents are 
written into a new table you shall create. Please, use Alembic and SQLAlchemy for the creation of this table.

The schema of the table should be as follows: 
1. A unique `Id`,
2. The `user_id` from the users table. 
3. The `salary` of this user from the users table.
4. The `unit` this employee has worked on.
5. The `tenure_in_years` this user worked on that unit. 
6. the `datetime` this record was inserted. 

Please, note that on the spreadsheet a user could have served in a unit more than once. When you encounter such a case, 
the summation of years they'd spent in that unit should be calculated and persisted. For example, if user `A` worked in 
`Human Resources` for 2 years, worked in `Customer Support` for 3 years, and then worked in `Human Resources` again for 4 
years, the expected entries for that user will be as follows:

| UserName | Unit | Tenure_in_years|
|-----|-----|-----|
|A| Customer Support | 3 |
|A| Human Resources | 6 |
  

Please, do write unit tests that cover all relevant use cases. And, create a page that displays what you have in the new table. 

In addition, please, design existing and new pages you create with CSS. You can use JavaScript as well; as you see fit.

Send your finished work as a zipped file to `intron@intron.io`. Make sure the Subject of your email is `Intron Health Take Home Interview`.
 
Again, thank you for working on this. 

