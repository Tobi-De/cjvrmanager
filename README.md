Cjvr_manager
=====



Cjvr_manager is a WebApp built using the Django Framework.



Detailed documentation is in the "docs" directory.



Running the project on the local server
---------------------------------------

1. Create a new virtual environnement for the project.
  
  * Using conda
    
      ```
      conda create --name cjvr -y
      ```
  
  * Using the virtual environnement manager provide with python3
    
    Run this commande from the project root
    
    ```
    python3 -m venv venv
    ```
    
2. Activate the virtual environnement.
    
    * Using conda
    
      ```
      conda activate cjvr
      ```
      
    * Using venv
  
      ```
      source venv/bin/activate
      ```      

3.  Install requirements.
    
    From the project root run: `
    
    ```
    pip install -r requirements.txt
    ```

4. Run this to create the Cjvr_manager migrations.
  
  ```
  python manage.py makemigrations cjvr
  python manage.py makemigrations users
  ``` 

5. Run to apply migrations to the database.

  ```
  python manage.py migrate
  ``` 

6. For testing purpose create fake data

    when populating data to the database for the first time, run this from the
    project root: 
    
    ```
    python manage.py populate_database
    ```
    
    Use these commands to add specific type of the data to the database :
    
    ```
    1-python manage.py create_aggressions fakedata.json
    
    2-python manage.py create_plaintiffs fakedata.json 
   
    3-python manage.py create_victims fakedata.json
    
    4-python manage.py create_testimonies fakedata.json 
    
    5-python manage.py set_victims_aggression 
    ```
    
    Note: some commands can't be executed without running others(refer to the order)

7. Start the development server with `python manage.py runserver`

8. Visit http://127.0.0.1:8000 to visit the WebApp.

