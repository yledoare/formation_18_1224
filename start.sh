docker ps |grep docker-db-1 

if [ $? = 1 ]
then
	cd docker
	docker-compose up -d
fi

[ ! -e venv ] && python3 -m venv venv
. venv/bin/activate
[ ! -e odoo ] && git clone --depth 1 -b 17.0 https://github.com/odoo/odoo 
[ -e /home/linuxconsole2024/x86_64/ ] && grep psycopg2 odoo/requirements.txt && cd odoo && pwd && patch -p1 < ../linuxconsole-odoo.patch && cd ..
pip3 install -r odoo/requirements.txt
[ -e /home/linuxconsole2024/x86_64/lib/python3.10/site-packages/ ] && export PYTHONPATH=/home/linuxconsole2024/x86_64/lib/python3.10/site-packages/:$PYTHONPATH
./odoo/odoo-bin -d postgres  --db_host localhost -r odoo -w odoo -i base  --addons-path=$PWD/addons,$PWD/odoo/addons -i estate_property_management -u estate_property_management
