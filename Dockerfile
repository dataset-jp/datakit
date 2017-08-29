FROM continuumio/miniconda3

RUN conda install pandas -y
RUN conda install -c anaconda pytables -y
RUN pip install requests xlrd

ENV PYTHONPATH $PYTHONPATH:/src
WORKDIR /src
ADD . /src
