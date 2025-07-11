#base image
FROM python:3.9

#workdirectory
WORKDIR /main

#COPY 
COPY . /main

#RUN
RUN pip install -r requirements.txt

#port
EXPOSE 8501

#command
CMD ["streamlit", "run", "streamlit_app.py"]
