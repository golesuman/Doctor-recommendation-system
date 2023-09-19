# Doctor Recommendations System
## Steps for Running the Project
- Clone the project repository first
- Go to the project directory and do the following.
- Make the docker image of the project using the following command:

    ```
    sudo docker build -t backend:latest -f Dockerfile .
    ```
- Run the following command to run the project

    ```
    sudo docker run -p 8000:8000  backend:latest  
    ```

- Send POST Request to this endpoint
    ```
    http://0.0.0.0:8000/api/recommend-doc
    ```
- Sample Input
    ```
    {
        "symptoms" : "leg pain with difficulty to walk"
    }
    ```
- Sample Output
    ```
   {
    "data": 
        [
            {
            "Osteoarthristis": "Rheumatologist"
            },
            {
            "Arthritis": "Rheumatologist"
            }
        ]
    }
    ```


# To run it without docker container on local machine
* Notice Your python version should be 3.8.x
1. python3.8 -m venv venv
2. Activate your virtual environment
3. pip install -r requirements.txt
4. python -m spacy download en_core_web_md
5. python -m pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_md-0.5.1.tar.gz
6. cd HospitalManagement
7. python manage.py runserver

- Send POST Request to this endpoint
    ```
    http://0.0.0.0:8000/api/recommend-doc
    ```
- Sample Input
    ```
    {
        "symptoms" : "leg pain with difficulty to walk"
    }
    ```
- Sample Output
    ```
   {
    "data": 
        [
            {
            "Osteoarthristis": "Rheumatologist"
            },
            {
            "Arthritis": "Rheumatologist"
            }
        ]
    }
    ```