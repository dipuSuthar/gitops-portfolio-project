FROM python:3.9-slim

# Security best practice: Create a non-root user
RUN adduser --disabled-password myuser
USER myuser

WORKDIR /app

# Pehle sirf requirements copy karein (Docker caching optimize karne ke liye)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Baaki code copy karein
COPY . .

# PATH update for installed packages
ENV PATH="/home/myuser/.local/bin:${PATH}"

EXPOSE 5000
CMD ["python", "app.py"]