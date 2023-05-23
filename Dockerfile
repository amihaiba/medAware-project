# Base image
FROM python:3.8.16-slim
# Create a system user
RUN groupadd -r medaware && useradd -r -g medaware med-user
# Set app directory
WORKDIR /usr/share/medaware-app
RUN mkdir staging done
# Copy requirements and install dependencies
ADD --chown=med-user:medaware requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Expose app port and set entrypoint to start a gunicorn WSGI server
EXPOSE 5000
ENTRYPOINT ["gunicorn","--user","med-user","--workers","1","--umask","007","--bind","0.0.0.0:5000","app:app"]
ADD --chown=med-user:medaware . .
# Switch to user
USER med-user