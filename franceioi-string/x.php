<?php

$x = readline();

for ($i = 0; $i<$x; $i++){
    for($j = 0; $j< $x; $j++) {
        if($i == $j || $j + $i == $x - 1) {
            echo 'x';
        }
        else {
            echo ' ';
        }
    }
    echo "\n";
}