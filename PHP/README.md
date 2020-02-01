
## **count() 錯誤**

* count(): Parameter must be an array or an object that implements Countable in Builder.php

* Put this code at the beginning your routes file its will work fine

route.php

if(version_compare(PHP_VERSION, '7.2.0', '>=')) {
    error_reporting(E_ALL ^ E_NOTICE ^ E_WARNING);
}
