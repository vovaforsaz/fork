FROM python:3.7
MAINTAINER "imaxfp@gmail.com"
RUN mkdir stock
COPY . /stock
WORKDIR /stock
RUN pip install -r requirements.txt
RUN pip install --upgrade streamlit
RUN ls -la
WORKDIR /stock/src
RUN ls -la
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]