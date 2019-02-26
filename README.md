# Pymail

![N|Moodle v1](./pantallas/home.png?raw=true "Title")

El programa permite el envío de correos utilizando Gmail

Recomendaciones
  - Máximo 200 correos por hora (se bloquea la cuenta de Gmail)
  - No enviar demasiados links, se detectan como SPAM


### Requerimientos

Permisos en Google Accounts:
Dentro de la [configuración de seguridad de google ](https://myaccount.google.com/security), permitir el uso de aplicaciones poco seguras.

![N|Habilitar ](./permisos.png?raw=true "Permisos")

### Instalación

Hay dos opciones via git o descargando el zip del repositorio

  - Clonamos el repositorio Git y entramos

```sh
$ git clone https://github.com/hkeyland/pymail.git
$ cd pymail
```

  - Descargamos el [zip](https://github.com/hkeyland/pymail/archive/master.zip), lo descomprimimos y entramos


Abrimos la consola de comandos y nos posicionamos dentro de la carpeta que se genera


```sh
$ cd pymail-master
```


### Configuración

Edita el archivo `sender.py` con los parámetros adecuados a tu cuenta 

  - Uso de cuenta de empresa o personal

Si configuraste gmail para enviar correos de un dominio propio, puedes enviarlos directamente desde ahi, es necesario que la cuenta ya este configurada y desde Gmal, puedas enviar corrso sin problemas.

Si deseas usar tu cuenta personal, comenta la línea y descoemnta la otra (#).
```python

"""EMAIL SETTINGS"""
sender = 'Empresa <empresa@email.com>'
#sender = 'Mi nombre <correo@gmail.com>'



```

  - Password

Utiliza tu usuario de gmail y el password correspondiente, independientemente si envias de cuenta personal o de un dominio porpio. El proceso de verificación para envio de correo utiliza las credenciales de Google.  

```python
 """GMAIL"""
    username = 'user@gmail.com'
    password = '*********'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()

```


  - Lista de correo
Crea tantas listas de correo como requieras, por ejemplo [lista.txt](./lista.txt?raw=true "Lista")


### Uso

Una vez instalado y configurado abrimos la terminal y ejecutamos:

```sh
$ python sender.py lista.txt
```



`
admin:admin
`

