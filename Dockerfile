FROM python:3.9-alpine
COPY ./ /work
RUN apk update && pip install -r /work/requirements.txt --no-cache-dir
RUN pip install -e /work
EXPOSE 8080
CMD ["flask","run"]