#DJANGO REST API

Blog Post API using Django Rest Framework
------- How to run --------

1. from root run vagrant machine:
 a. run "vagrant up" - start vagrant
 b. run "vagrant ssh" - connect vagrant to ubuntu-xenial server

2. run blog_api virtual environment: run "workon myenv"

3. access vagrant folder: "cd /vagrant" (access root directory on server)

4. access source: "cd src/blog_api_project"

5. run server: "python manage.py runserver 0.0.0.0:8080"
Server is now running on vagrant machine at port 0.0.0.0:8080
which is forwarded to port 127.0.0.1:8080 on local machine


** Also download ModHeader Chrome Extension to assist token authentication
Login via API to generate a token for that user
Using modheader to login, create a key-value pair:
Authorization - Token "token generated by user login"
