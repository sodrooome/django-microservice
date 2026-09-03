FROM nginx:1.27-alpine

RUN rm /etc/nginx/conf.d/default.conf

ADD services.conf /etc/nginx/conf.d/

RUN ls /etc/nginx/conf.d/