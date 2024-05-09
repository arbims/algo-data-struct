<?php

$s = readline();
$s = str_split($s);

$i = 0;

while ($i < count($s) - 1) {
    if ($s[$i] == $s[$i+1]) {
        unset($s[$i+1]);
        unset($s[$i]);
        $s = array_values($s);
        $i = 0;
    } else {
        $i = $i + 1;
    }
}

$s = implode($s);
echo $s."\n";