=====
Cjvr_manager
=====



Cjvr_manager is a WebApp built using the Django Framework.



Detailed documentation is in the "docs" directory.



Running the project on the local server
---------------------------------------

1. Create a new virtual environnement for the project.
  
  * Using conda
    
    .. code-block:: bash
      conda create --name cjvr -y
  
  * Using the virtual environnement manager provide with python3
    
    Run this commande from the project root
    
    ```
    python3 -m cjvr venv
    ```
    

2. Activate the virtual environnement.
    
    * Using conda
    
      ```
      conda activate cjvr
      ```
      
    * Using venv
  
      ```
      deactivate
      ```
      
3.  Install requirements.
    
    From the project root run: `
    
    ```
    pip install -r requirements.txt
    ```


4. Run this to create the Cjvr_manager migrations.
  
  ```
  python manage.py makemigrations cjvr
  ``` 


5. Run to apply migrations to the database.

  ```
  python manage.py migrate
  ``` 


5. For testing purpose create fake data
    
    From the project root run:
    
    ```
    python manage.py create_aggressions fakedata.json
    
    python manage.py create_plaintiffs fakedata.json
    
    python manage.py create_testimonies fakedata.json
    
    python manage.py set_victims_aggression
    ```


2. Start the development server with `python manage.py runserver`


3. Visit http://127.0.0.1:8000 to visit the WebApp.

