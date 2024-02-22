FROM python:3.9-alpine
COPY ./ /work
RUN apk update && pip install -r /work/requirements.txt --no-cache-dir
EXPOSE 8080
CMD ["flask","run"]