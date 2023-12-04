FROM python:3-alpine3.17
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip --default-timeout=1000 install -r requirements.txt
EXPOSE 4444
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--port=4444"]