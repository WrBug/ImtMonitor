# 星际魔盒监工

## 功能介绍

定时检查设备在线情况，设备异常时，将异常设备发送到设置的邮箱


### 加入qq群获取最新更新

    699453879
    
## 觉得监工对你有用，欢迎打赏


**0x7D6C23b07E931bA39Bed2DBD885ca9c280946BD5**

## android版钱包。支持IMT

[https://www.coolapk.com/apk/com.wrbug.wallet][1]
### 使用教程

#### 准备工具

    云搬家账号（绑定设备的账号）
    收信邮箱（用于接收异常邮件）
    smtp邮箱（用于发送邮件，推荐使用qq邮箱）
    一台linux机器（强烈推荐使用星际魔盒，物尽其用,，有树莓派也可以）
#### 配置监工服务

1. 使用ssh登录linux，并且切换到root账户(不会的百度找教程)
```
ssh admin@IP地址
#输入admin的密码，默认为IMTNAS，回车后登陆
sudo -s
#会再提示输入密码，回车后登陆
```
2. 执行下面脚本：

```
wget https://github.com/WrBug/ImtMonitor/archive/master.zip -O master.zip
unzip master.zip
cd ImtMonitor-master
```

3. 配置账号

编辑account.py文件。按照注释内容填写完整


4. 测试配置是否正常

执行：

`python run.py`

出现设备信息表示IMT账户配置成功.

执行：

`python mail.py `

检查邮件有收到说明邮箱配置成功

5. 设置定时任务

执行命令：

```
mkdir -p /usr/monitor
mv ./* /usr/monitor
# 10表示10分钟执行一次，可以改成1-59范围的值，已经设置过无需再次设置，可以通过修改/etc/crontab文件来修改
echo '*/10 * * * *  root cd /usr/monitor && sh run.sh' >> /etc/crontab
service cron restart
```
6. 检查定时任务
随便断开一台机器的网络【勿断开执行脚本的机器】，x分钟(步骤5的时间)后有邮件提醒说明配置成功


### 说明

如果有多台机器，可以在多台机器上配置改脚本，避免执行脚本的机器死机，无法正常发送邮件


[1]: https://www.coolapk.com/apk/com.wrbug.wallet
