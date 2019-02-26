# Pymail

![N|Moodle v1](./pantallas/home.png?raw=true "Title")

El programa permite el envío de correos utilizando Gmail

Recomendaciones
  - Máximo 200 correos por hora (se bloquea la cuenta de Gmail)
  - No enviar demasiados links, se detectan como SPAM


![N|Moodle ](./pantallas/contenido.png?raw=true "Title")

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

Edita el archivo `config.php` con los parámetros adecuados a tu sistema 

```php
<?php  /// Moodle Configuration File 

unset($CFG);

$CFG->dbtype    = 'mysql';
$CFG->dbhost    = 'localhost';
//$CFG->dbhost    = '192.168.2.98';

//$CFG->dbname    = 'moodle';
//$CFG->dbuser    = 'moodle';
//$CFG->dbpass    = 'M0oDL34r';
$CFG->dbname    = 'm1';
$CFG->dbuser    = 'root';
$CFG->dbpass    = '';

$CFG->dbpersist =  false;
$CFG->prefix    = 'mdl_';

//$CFG->wwwroot   = 'http://187.141.33.146/moodle';
//$CFG->dirroot   = '/home/httpd/html/ciclope/moodle';
//$CFG->dataroot  = '/home/httpd/html/ciclope/moodledata';

$CFG->wwwroot   = 'http://localhost/lce-moodlev1/moodle';
//$CFG->wwwroot   = 'http://192.168.4.36/moodle-v1/moodle';

$CFG->dirroot   = '/Applications/XAMPP/xamppfiles/htdocs/lce-moodlev1/moodle';
$CFG->dataroot  = '/Applications/XAMPP/xamppfiles/htdocs/lce-moodlev1/moodledata';
//$CFG->dirroot   = ' C:\xampp\htdocs\lce-moodlev1\moodle';
//$CFG->dataroot  = 'C:\xampp\htdocs\lce-moodlev1\moodledata';

$CFG->admin     = 'admin';

$CFG->directorypermissions = 00777;  // try 02777 on a server in Safe Mode

require_once("$CFG->dirroot/lib/setup.php");
// MAKE SURE WHEN YOU EDIT THIS FILE THAT THERE ARE NO SPACES, BLANK LINES,
// RETURNS, OR ANYTHING ELSE AFTER THE TWO CHARACTERS ON THE NEXT LINE.
?>

```


### Acceso

Una vez instalado abrimos el navegador con los datos:

[http://localhost/lce-moodlev1/](http://localhost/lce-moodlev1/)


![N|Moodle login](./pantallas/login.png?raw=true "Title")

`
admin:admin
`



### Plataforma

![N|Moodle ](./pantallas/moodle.png?raw=true "Title")

![N|Moodle ](./pantallas/moodle-2.png?raw=true "Title")


### Para Dev

Editar el archivo .fla para modificar la ruta de login de moodle

![N|Moodle ](./pantallas/edit-fla-login.png?raw=true "Title")


