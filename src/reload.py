from requests import post

x = post('http://192.168.0.1/login/Auth', data={"password":"MjIwNjIwMDU="}, allow_redirects=False)
post("http://192.168.0.1/goform/sysReboot", data={"module1":"sysOperate","action":"reboot"}, headers={"cookie":x.headers["Set-Cookie"].split(";")[0]})
