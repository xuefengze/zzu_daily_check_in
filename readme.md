# zzu每日打卡

### 依赖：
* chrome
* selenium
* pandas
* [chromedriver](https://npm.taobao.org/mirrors/chromedriver)
* email

### user.csv(example)
```
id,password
1,2
123456,12345
```

### 安装
`selenium`
```
pip3 install selenium
```
`email`
```
pip3 install email
```
`chrome`
```
yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
```
`依赖`
```
yum install mesa-libOSMesa-devel gnu-free-sans-fonts wqy-zenhei-fonts
```
`chromedriver`(换成和chrome对应的版本)
```
wget http://npm.taobao.org/mirrors/chromedriver/92.0.4515.107/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
`pandas`
```
pip3 install pandas
```
（以及一个垃圾的`log`，仅为了记录是否正常打卡）
* 使用`cron`时注意路径问题，使用相对路径会报错
