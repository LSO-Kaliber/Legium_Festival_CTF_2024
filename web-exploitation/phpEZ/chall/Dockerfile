FROM php:8.0.0-apache

RUN rm -rf /var/www/html/*

COPY chall.php ./index.php

EXPOSE 80

CMD ["apache2-foreground"]
