# Base image
FROM python:3.8.16-slim
# Add user to be used in the container
RUN groupadd -r medaware && useradd -r -g medaware med-user
# Set the directory where the app sits
WORKDIR /usr/share/medaware-app
RUN mkdir staging done
# Copy requirements file and install dependencies
ADD --chown=med-user:medaware requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Expose port 5000 to be used by Gunicorn
EXPOSE 5000
# Start Gunicorn WSGI server
ENTRYPOINT ["gunicorn","--user","med-user","--workers","1","--umask","007","--bind","0.0.0.0:5000","app:app"]
# Copy app source files
ADD --chown=med-user:medaware . .
USER med-user