#ADDRESS TRACKER

**prerequisite**

Docker

##How To Run

1.Clone This Repo

2.Checkout to master branch

2.docker build -t fastapi_interview .

3.1 docker run -it -p 8000:8000 -v ${pwd}/app:/app fastapi_interview (if on windows)

            OR

3.2 docker run -it -p 8000:8000 -v $(pwd)/app:/app fastapi_interview (if on linux)

4.open the url localhost:8000/docs/ for seeing the api docs
