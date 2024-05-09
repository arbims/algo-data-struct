<?php

function fact($n) {
    $r = 1;
    for ($i = 2; $i< $n+1; $i++) {
        $r = $r * $i;
    }
    return $r;
}

echo fact(5);