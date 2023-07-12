# pull official base image
FROM python:3.11

RUN apt update

# set work directory
WORKDIR /src

# install libs
COPY src/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY src/ /src/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]