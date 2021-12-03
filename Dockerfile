FROM python:3.9
ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt install python3-psycopg2 -y
RUN pip install -r requirements.txt

CMD [ "python", "ms_user/manage.py", "runserver", "0.0.0.0:8000" ]
