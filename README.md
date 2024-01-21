# Flask-Backend-App

FastAPI
Swagger
Versioning
Decorators
Error Handling
Logging
Async code
Multithreading
Caching
    API calls
    Auth tokens
    Functions
Authentication
Authorization
Rate limitter
Throttling

AWS:
    API gateway
    ELB
    S3
    Lambda
    RDS postgres
    DynamoDB
    Cloudwatch
    Elasticcache
    EKS
    EC2
    SQS
    SNS

Data:
    Pagination
    Multimedia data
    Batch data
    Stream of data

Job scheduling
Testing
    Unit
    Integration
    Automated
    Load balancing

Docker
Kubernetes

ETL pipeline using AWS S3 and Lambda
Helper microservices:
    Java springboot
    C#



Steps to start:
    Development on local machine
        Activate virtual env on win:            venv1\Scripts\activate
        Activate uvicorn:                       python -m uvicorn main:app --reload
        Activate gunicorn on linux:             gunicorn -k uvicorn.workers.UvicornWorker main:app
        Server:                                 http://127.0.0.1:8000
        Swagger docs:                           http://127.0.0.1:8000/docs

    Develpoment on EC2 instance (Linux)
        cd fast_api_server
        source venv2/bin/activate and deactivate


Tasks:
    Manual API hosting and Serverless API hosting on AWS

    Fastapi API on Uvicorn on windows/ Gunicorn on linux in EC2
        Created a linux/unix instance
        Installed python3-pip, python3-virtualenv
        CRUD endpoints
            Decorators for logging, errors, authentication and authorization
    
    Lambda functions
        CRUD endpoints
        Logging triggers
        Error triggers
    
    API gateway connection to Lambda

    Cloudwatch monitoring both EC2 API and API Gateway

    Create S3 bucket with sample data
    Connect S3 to EC2 crud
    Connect S3 to Lamba crud
    
    Connect RDS postrges to Lambda
    Connect DynamoDB to Lambda
    
    Connect RDS postrges to EC2
    Connect DynamoDB to EC2
    
    Connect ELB to EC2
    Connect ELB to API gateway

    SQS from API gateway 
    SQS from EC2

    SNS triggers from Lambda
    SNS triggers from EC2

    Setup Elastic cache to save API calls, db calls from Lambda
    Setup Elastic cache to save API calls, db calls from EC2

    Setup NGINX on EC2
        SLS/ TLS
        HTTPS
        Encryption
    
    Deploy on EKS
