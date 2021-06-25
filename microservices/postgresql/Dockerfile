FROM postgres:12

RUN apt update && apt install -y pgagent

RUN ./usr/bin/pgagent hostaddr=postgres_container dbname=postgres user=postgres -s pgagent_log.log

COPY ./backup_script ./home/backup_script