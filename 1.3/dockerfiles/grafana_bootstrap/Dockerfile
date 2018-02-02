FROM alpine

RUN apk update 
RUN apk add httpie bash

COPY bootstrap.sh /

CMD ["/bootstrap.sh"]
