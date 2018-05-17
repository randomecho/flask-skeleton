FROM python:3.3-slim

WORKDIR /app

RUN pip install --trusted-host pypi.python.org Flask Flask-Markdown

EXPOSE 80

COPY . /app

CMD ["python", "app.py"]
