<?php

if ($file = fopen("input.txt", "r")) {
    $num_larger = 0;
    $previous_line = null;
    while(!feof($file)) {
        $current_line = (int) fgets($file);

        if($previous_line != null){
            if($current_line > $previous_line){
                $num_larger++;
            }
        }

        $previous_line = $current_line;
     }
    fclose($file);
    echo $num_larger;
 }

