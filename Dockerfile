FROM docker.io/fnndsc/mni-conda-base:civet2.1.1-python3.10.2

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="pl-premc-mincmorph" \
      org.opencontainers.image.description="A ChRIS plugin which smoothens a mask using mincmorph in preparation for marching-cubes."

WORKDIR /usr/local/src/ep-premc-mincmorph

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["premc_mincmorph", "--help"]
