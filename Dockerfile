FROM python:3.9-alpine
WORKDIR /src
ENV FLASK_APP=index.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
CMD ["flask", "run"]
