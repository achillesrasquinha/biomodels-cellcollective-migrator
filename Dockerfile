FROM  python:alpine
LABEL maintainer=achillesrasquinha@gmail.com

ENV BCMPATH=/usr/local/src/bcm

RUN apk add --no-cache bash git

RUN mkdir -p $BCMPATH

COPY . $BCMPATH

RUN pip install $BCMPATH

WORKDIR $BCMPATH

ENTRYPOINT ["/usr/local/src/bcm/docker/entrypoint.sh"]

CMD ["bcm"]