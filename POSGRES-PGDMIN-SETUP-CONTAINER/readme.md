################ POSTGRESQL#######################
services:
  db:
    container_name: postgresql_db
    image: postgres
    restart: always
    environment:
      POSTGRES_DB:student_db
      POSTGRES_USER:root
      POSTGRES_PASSWORD:root
    ports:
    - "5432:5432"  

  pgadmin:
    container_name: pgadmin 
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: root@root.com
      PGADMIN_DEFAULT_PASSWORD: root
      #PGAMIN_DEFAOULT_PORT: 80
    ports:
    - "5050:80"  

########################    MYSQL    ###############################

services:
  db:
    container_name: mysql_db
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_DATABASE: student_db
      MYSQL_ROOT_PASSWORD: root
      MYSQL_USER: user
      MYSQL_PASSWORD: userpassword
    ports:
      - "3307:3306"

  phpmyadmin:
    container_name: phpmyadmin
    image: phpmyadmin/phpmyadmin
    #image: adminer
    restart: always
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "8080:80"






#############################################




