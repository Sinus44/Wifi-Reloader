import requests
import base64

try:
	password = base64.b64encode(bytes(input("For restart input password: "), "utf-8")).decode("utf-8")
	x = requests.post('http://192.168.0.1/login/Auth', data={"password":password}, allow_redirects=False)
	requests.post("http://192.168.0.1/goform/sysReboot", data={"module1":"sysOperate","action":"reboot"}, headers={"cookie":x.headers["Set-Cookie"].split(";")[0]})
except:
	print("Произошла ошибка. Проверьте правильность ввода пароля и / или повторите попытку позже.")
	quit()
print("Роутер перезагружется. Пожалуйста ожидайте включения.")
