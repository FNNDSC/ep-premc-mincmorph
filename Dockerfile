# Python version can be changed, e.g.
# FROM python:3.8
# FROM docker.io/fnndsc/conda:python3.10.2-cuda11.6.0
FROM docker.io/python:3.10.2-slim-buster

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="pl-premc-mincmorph" \
      org.opencontainers.image.description="A ChRIS plugin which smoothens a mask using mincmorph in preparation for marching-cubes."

WORKDIR /usr/local/src/ep-premc-mincmorph

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["premc_mincmorph", "--help"]
