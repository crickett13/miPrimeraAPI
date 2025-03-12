FROM httpd:2.4.33-alpine
RUN apk update; \
    apk upgrade;
# Copy apache vhost file to proxy php requests to php-fpm container
COPY demo.apache.conf /usr/local/apache2/conf/demo.apache.conf
RUN echo "Include /usr/local/apache2/conf/demo.apache.conf" \
    >> /usr/local/apache2/conf/httpd.conf

RUN mkdir -p /var/www/html
COPY ./static/*.html /var/www/html/
COPY ./static/*.png /var/www/html/
COPY ./static/*.txt /var/www/html/

