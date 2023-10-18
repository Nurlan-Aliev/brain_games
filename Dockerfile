FROM python:3

RUN pip install poetry

COPY . /python_project

WORKDIR python_project

RUN poetry install

CMD [ "poetry", "run",  "start-games" ]
