FROM python:3.13


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


WORKDIR /practical


COPY requirements.txt /practical/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /practical/


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


