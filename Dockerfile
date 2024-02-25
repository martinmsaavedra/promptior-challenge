FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir aiohttp==3.9.3 aiosignal==1.3.1 annotated-types==0.6.0 anyio==4.3.0 attrs==23.2.0 beautifulsoup4==4.12.3 ...

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
