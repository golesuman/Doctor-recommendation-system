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