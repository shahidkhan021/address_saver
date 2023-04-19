FROM python:3.9


RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install sqlalchemy

WORKDIR app

COPY /app /app 

ENTRYPOINT ["uvicorn","main:app", "--reload", "--host", "0.0.0.0"]