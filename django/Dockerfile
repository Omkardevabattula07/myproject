FROM python:3.10-slim
LABEL name="omkar"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYCODE 1
WORKDIR /code
COPY  . /code/
COPY requirements.txt /code/
RUN  pip install --upgrade pip 
RUN pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate
EXPOSE 8000
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
