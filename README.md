Catalys Demo

Step 1: Create Virtual Environment
If we want to isolate our dependencies then we must need to use virtual environment.
For creating virtual environment we use the below commands.
First we install virtualenv library using pip python package installer.
>>pip install virtualenv
then type below command
>> virtualenv env_name
After executing above command virtualenv will be created as given env_name.

Step 2: Install flask
For installing flask web framework, we use below command
>>pip install flask

Above command will install the latest version of Flask framework.

Step 3: Install requests module in python
For installing requests module we use below command
>> pip install requests

Step 4: Create functions to perform actions
After successfully installing all dependencies, we create a function to fetch data from any api,
I already have created Rest api using Flask-Restful for our project. I am using local api created by myself.

When I call fetch_data url then I got users data from my local api which is running on my own machine.
I have printed data got from api as below
Data==================> [{'business_name': 'Toys R Us', 'first_name': 'Administrator', 'fk_business_id': 2, 'fk_role_id': 1, 'id': 1, 'is_active_flag': True, 'last_name': 'Admin', 'role_name': 'Administrator', 'user_email': 'administrator@gmail.com', 'user_mobile': '9896654778', 'user_name': 'administrator'}, {'business_name': 'Toys R Us', 'first_name': 'Offer', 'fk_business_id': 2, 'fk_role_id': 4, 'id': 2, 'is_active_flag': True, 'last_name': 'Financer', 'role_name': 'Financer', 'user_email': 'offerfinancer@gmail.com', 'user_mobile': '8788792703', 'user_name': 'offer_financer'}, {'business_name': 'Automata', 'first_name': 'offer', 'fk_business_id': 3, 'fk_role_id': 3, 'id': 3, 'is_active_flag': True, 'last_name': 'Approver', 'role_name': 'Offer Approver', 'user_email': 'offerapprover@gmail.com', 'user_mobile': '4545454545', 'user_name': 'offer_approver'}, {'business_name': 'Toys R Us', 'first_name': 'offers', 'fk_business_id': 2, 'fk_role_id': 2, 'id': 4, 'is_active_flag': True, 'last_name': 'Ceator1', 'role_name': 'Offer Creator', 'user_email': 'offercreator@gmail.com', 'user_mobile': '5555556654', 'user_name': 'offer_creator'}, {'business_name': 'Sharad_Business', 'first_name': 'sales', 'fk_business_id': 4, 'fk_role_id': 5, 'id': 5, 'is_active_flag': True, 'last_name': 'officer', 'role_name': 'Sales Officer', 'user_email': 'salesofficer@gmail.com', 'user_mobile': '9881755161', 'user_name': 'sales_officer'}]

after that I have called process_data(data) function to perform some action on data, so I have converted first_name and last_name of all users as uppercase latters
[
  {
    "business_name": "Toys R Us",
    "first_name": "ADMINISTRATOR",
    "fk_business_id": 2,
    "fk_role_id": 1,
    "id": 1,
    "is_active_flag": true,
    "last_name": "ADMIN",
    "role_name": "Administrator",
    "user_email": "administrator@gmail.com",
    "user_mobile": "9896654778",
    "user_name": "administrator"
  },
  {
    "business_name": "Toys R Us",
    "first_name": "OFFER",
    "fk_business_id": 2,
    "fk_role_id": 4,
    "id": 2,
    "is_active_flag": true,
    "last_name": "FINANCER",
    "role_name": "Financer",
    "user_email": "offerfinancer@gmail.com",
    "user_mobile": "8788792703",
    "user_name": "offer_financer"
  },
  {
    "business_name": "Automata",
    "first_name": "OFFER",
    "fk_business_id": 3,
    "fk_role_id": 3,
    "id": 3,
    "is_active_flag": true,
    "last_name": "APPROVER",
    "role_name": "Offer Approver",
    "user_email": "offerapprover@gmail.com",
    "user_mobile": "4545454545",
    "user_name": "offer_approver"
  },
  {
    "business_name": "Toys R Us",
    "first_name": "OFFERS",
    "fk_business_id": 2,
    "fk_role_id": 2,
    "id": 4,
    "is_active_flag": true,
    "last_name": "CEATOR1",
    "role_name": "Offer Creator",
    "user_email": "offercreator@gmail.com",
    "user_mobile": "5555556654",
    "user_name": "offer_creator"
  },
  {
    "business_name": "Sharad_Business",
    "first_name": "SALES",
    "fk_business_id": 4,
    "fk_role_id": 5,
    "id": 5,
    "is_active_flag": true,
    "last_name": "OFFICER",
    "role_name": "Sales Officer",
    "user_email": "salesofficer@gmail.com",
    "user_mobile": "9881755161",
    "user_name": "sales_officer"
  }
]

Step 5: Run the application
For running flask application, we need to use command in command line. We can set debug as True if we want to get the errors in program.
>> python main.py

 After executing above command our flask application will run on locally on IP address
 http://127.0.0.1:5000
Now we call endpoint as http://127.0.0.1:5000/fetch_data in browser then we get the processed data
