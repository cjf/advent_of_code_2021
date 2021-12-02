<?php

$array = file("input.txt");
$num_larger = 0;
for($i = 0; $i+3 < count($array); $i++){
    $groupA = (int)$array[$i] + (int)$array[$i+1] + (int)$array[$i+2];
    $groupB = (int)$array[$i+1] + (int)$array[$i+2] + (int)$array[$i+3];

    if($groupB > $groupA){
        $num_larger++;
    }
}

var_dump($num_larger);




