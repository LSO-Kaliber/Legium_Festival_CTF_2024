<?php error_reporting(0);
    // include 'flag.php';
    $flag = getenv("FLAG");
    $keys = "/^([a-bB-C]+)\[\\/([0-5]+)$/";
    if (isset($_POST['key'])) {
        $key = htmlspecialchars($_POST['key']);
        if (preg_match($keys, $key) == true) {
            if(strlen($key) < 8 && $key > 9999999){
                echo "there's your flag $flag";
            }else{
                echo "There's no Key with value $key";
            }
        }else{
            echo "Key Invalid";
        }
    }
?>
