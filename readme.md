# zzu每日打卡

### 所需库及软件：
* chrome
* selenium
* pandas
* [chromedriver](https://npm.taobao.org/mirrors/chromedriver)

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
`chrome`
```
yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
```
`依赖的库`
```
yum install mesa-libOSMesa-devel gnu-free-sans-fonts wqy-zenhei-fonts
```
`chromedriver`(换成和chrome对应的版本)
```
wget http://npm.taobao.org/mirrors/chromedriver/92.0.4515.107/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x /usr/bin/chromedriver
```
`pandas`
```
pip3 install pandas
```