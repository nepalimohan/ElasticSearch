FROM python:3.11-slim

LABEL maintainer = "Mohan Nepali"

WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3-dev
    # pip install --upgrade pip



COPY requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

#copying codebase
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
