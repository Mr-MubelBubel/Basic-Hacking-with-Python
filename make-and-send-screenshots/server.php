<!-- I know it is a Python repo but I don't want to use the Python version of the script. If you have fun, you will write a python script and make a issue with this. -->
<?php

%updir = 'img/';
$fname = getenv('REMOTE_ADDR').'.png';
move_uploaded_file($_FILES['screenshot']['tmp_name'], $updir.$fname);

?>