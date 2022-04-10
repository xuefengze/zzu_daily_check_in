#!/bin/bash
checkin_login="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
checkin_submit="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
name=""
passwd=""
smbtn="进入健康上报平台"
myvs_24="否"	

punch () {
	ptoid_sid=`wget -q -O - --post-data "uid=${name}&upw=${passwd}&smbtn=${smbtn}&hh28=948" "$checkin_login" | \
		    sed -n 's/^.*first6?\(ptopid=.*\)"}}/\1/p'`

	wget -q -O - --post-data "day6=b&did=1&men6=a&${ptoid_sid}" "$checkin_submit" &> /dev/null

	#myvs_13="g"		#health code color
	myvs_13a="41"	#province
	myvs_13b="4101"	#city
	myvs_13c="郑大"	 #location
	myvs_26="5"		#vaccine
	longitude="113.631419"
	latitude="34.753439"

	wget -q -O - --post-data "myvs_1=否&myvs_2=否&myvs_3=否&myvs_4=否&myvs_5=否&myvs_6=否&myvs_7=否&myvs_8=否&myvs_9=否&myvs_10=否&myvs_11=否&myvs_12=否&myvs_13a=${myvs_13a}&myvs_13b=${myvs_13b}&myvs_13c=${myvs_13c}&myvs_24=${myvs_24}&myvs_26=${myvs_26}&memo22=成功获取&jingdu=${longitude}&weidu=${latitude}&door=&day6=&did=2&men6=a&sheng6=&shi6=&fun18=819&fun3=&${ptoid_sid}" "$checkin_submit" > a.html
}

while IFS="" read -r line || [ -n "$line" ]
do
	context=($line)
	name=${context[0]}
	passwd=${context[1]}

	punch
done < $SCRIPT_DIR/user.txt