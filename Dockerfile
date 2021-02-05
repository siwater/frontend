FROM python:3.8-buster

WORKDIR /app

COPY frontend.py requirements.txt /app/
COPY templates/ /app/templates/

RUN python -m  pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "-u", "frontend.py"]
