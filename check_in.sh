eckin_home="https://jksb.v.zzu.edu.cn"
checkin_login="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
checkin_submit="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"

name="123456"
passwd="123456"
smbtn="进入健康上报平台"

ptoid_sid=`wget -q -O - --post-data "uid=${name}&upw=${passwd}&smbtn=${smbtn}&hh28=948" "$checkin_login" | \
	    sed -n 's/^.*first6?\(ptopid=.*\)"}}/\1/p'`

wget -q -O - --post-data "day6=b&did=1&men6=a&${ptoid_sid}" "$checkin_submit" &> /dev/null

myvs_13="g"
myvs_13a="41"
myvs_13b="4101"
myvs_13c="郑大"
myvs_24="否"
myvs_26="2"
jingdu="113.53"
weidu="34.817"

wget -q -O - --post-data "myvs_1=否&myvs_2=否&myvs_3=否&myvs_4=否&myvs_5=否&myvs_6=否&myvs_7=否&myvs_8=否&myvs_9=否&myvs_10=否&myvs_11=否&myvs_12=否&myvs_13=${myvs_13}&myvs_13a=${myvs_13a}&myvs_13b=${myvs_13b}&myvs_13c=${myvs_13c}&myvs_24=${myvs_24}&myvs_26=${myvs_26}&jingdu=${jingdu}&weidu=${weidu}&day6=b&did=2&men6=a&${ptoid_sid}" "$checkin_submit" > tmp.html
