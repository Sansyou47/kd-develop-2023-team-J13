FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Pythonファイルの実行
CMD ["python", "-u", "main.py"]