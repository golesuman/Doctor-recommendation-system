FROM python:3.8

# turning off buffering to stdout/stderr in a docker container is mainly a concern of getting as much information
# from running application as fast as possible in the container log and not loosing anything in case of a crash.
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get install -y binutils libproj-dev gdal-bin
RUN python -m pip install gunicorn

WORKDIR /backend-api

COPY ./HospitalManagement /backend-api/
COPY ./requirements.txt /backend-api/requirements.txt

RUN ls -a
RUN python -m pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]