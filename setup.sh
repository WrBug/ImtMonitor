wget https://github.com/WrBug/ImtMonitor/archive/master.zip -O master.zip
unzip master.zip
cd ImtMonitor-master
python init.py
mkdir -p /usr/monitor
mv ./* /usr/monitor
echo '*/10 * * * *  root cd /usr/monitor && sh run.sh' >> /etc/crontab
service cron restart
cd ..
rm -rf master.zip ImtMonitor-master
echo '配置完成'