FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install requirements.txt

COPY . .

CMD ["gunicorn", "bind", "0.0.0.0:8000", "project.wsgi:application"]