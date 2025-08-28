docker ps |grep docker-db-1 
if [ $? = 1 ]
then
       cd docker
       docker-compose up -d || docker compose up -d
       cd ..
fi

[ ! -e venv ] && python3 -m venv venv
. venv/bin/activate
[ ! -e odoo ] && git clone --depth 1 -b 18.0 https://github.com/odoo/odoo 
if [ -e /home/linuxconsole2024/x86_64/ ] 
then
  cd odoo
  grep psycopg2 requirements.txt && patch -p1 < ../linuxconsole-odoo.patch 
  cd ..
fi
pip3 install -r odoo/requirements.txt
[ -e /home/linuxconsole2024/x86_64/lib/python3.10/site-packages/ ] && export PYTHONPATH=/home/linuxconsole2024/x86_64/lib/python3.10/site-packages/:$PYTHONPATH
./odoo/odoo-bin -d postgres  --db_host localhost -r odoo -w odoo --addons-path=$PWD/addons,$PWD/odoo/addons -i estate_property_management -u estate_property_management
# docker exec -ti docker-db-1 psql -h localhost -U odoo postgres
