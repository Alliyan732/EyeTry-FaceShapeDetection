FROM python:3-alpine3.17
WORKDIR /app
COPY . /app
RUN . venv/bin/activate && pip install --upgrade pip && pip --default-timeout=1000 install --no-cache-dir -r requirements.txt
EXPOSE 4444
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--port=4444"]