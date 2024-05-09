<?php
// Read input
$input = readline();
$elements = explode(" ", $input);
$nb = intval($elements[0]);
$mot = $elements[1];

// Print the word multiple times
for ($id = 0; $id < $nb; $id++) {
    echo ($id < $nb-1) ? "$mot " : "$mot";
}
?>
