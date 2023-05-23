FROM python:3.8.16-slim
WORKDIR /usr/share/medaware-app
RUN mkdir staging done
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["gunicorn","--user","med-user","--workers","1","--umask","007","--bind","0.0.0.0:5000","app:app"]
COPY . .
RUN groupadd -r medaware && useradd -r -g medaware med-user && chown -R med-user:medaware /usr/share/medaware-app
USER med-user