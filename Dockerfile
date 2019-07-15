From python:3

ADD omdb_rt_rating.py /

ADD omdb_config.py /

RUN pip install omdb

RUN pip install requests

ENTRYPOINT [ "python", "./omdb_rt_rating.py" ]

CMD []

