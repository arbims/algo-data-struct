<?php
// Read input
$nbPersonnes = readline();
// Iterate for each person
for ($i = 0; $i < $nbPersonnes; $i++) {
    // Read input for each person
    $line = readline();
    list($prenom, $nom) = explode(" ", trim($line));
    
    // Print last name followed by first name
    echo "$nom $prenom\n";
}
