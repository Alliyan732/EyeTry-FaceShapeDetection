FROM python:3-alpine3.18
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 4444
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--port=4444"]