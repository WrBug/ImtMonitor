wget https://github.com/WrBug/ImtMonitor/archive/master.zip -O master.zip
unzip master.zip
cd ImtMonitor-master
python init.py
rm -rf /usr/monitor
mkdir -p /usr/monitor
mv ./* /usr/monitor

txt=$(cat /etc/crontab)
if [[ ${txt} == *'/usr/monitor'* ]]; then
  echo '定时任务已存在'
else
  echo '*/10 * * * *  root cd /usr/monitor && sh run.sh' >> /etc/crontab
fi
service cron restart
cd ..
rm -rf master.zip ImtMonitor-master
echo '配置完成'
