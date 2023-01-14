import requests
import base64

try:
    password = base64.b64encode(bytes(input("Для перезагрузки роутера введите пароль: "), "utf-8")).decode("utf-8")
    x = requests.post('http://192.168.0.1/login/Auth', data={"password":password}, allow_redirects=False)
    requests.post("http://192.168.0.1/goform/sysReboot", data={"module1":"sysOperate","action":"reboot"}, headers={"cookie":x.headers["Set-Cookie"].split(";")[0]})
    print("Роутер перезагружется. Пожалуйста ожидайте включения.")
except:
    print("Произошла ошибка. Проверьте правильность ввода пароля и / или повторите попытку позже.")

input("Нажмите Enter, что бы закрыть это окно.")
quit()