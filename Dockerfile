# FROM busybox
FROM python:3-slim

COPY ./bin/redis-shake.linux /usr/local/app/redis-shake
COPY ./conf/redis-shake.conf /usr/local/app/redis-shake.conf
COPY ./start.py /usr/local/app/start.py

ENV SOURCE_TYPE standalone
ENV SOURCE_ADDRESS 127.0.0.1:20441
ENV SOURCE_PASSWORD_RAW 123456
ENV TARGET_TYPE standalone
ENV TARGET_ADDRESS 127.0.0.1:6379
ENV TARGET_PASSWORD_RAW 123456
ENV TARGET_DB -1

ENV KEY_EXISTS none
ENV FILTER_DB_WHITELIST -1
ENV FILTER_DB_BLACKLIST -1
ENV FILTER_KEY_WHITELIST -1
ENV FILTER_KEY_BLACKLIST -1
ENV LOG_LEVEL info

ENV BIG_KEY_THRESHOLD 524288000

ENV TYPE sync

CMD python /usr/local/app/start.py
