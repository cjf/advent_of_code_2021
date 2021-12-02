<?php

if ($file = fopen("input.txt", "r")) {
    $current_depth = 0;
    $current_hor = 0;
    $current_aim = 0;
    while (!feof($file)) {
        $current_line = fgets($file);

        if (strlen($current_line) > 0) {

            $line_parts = explode(' ', $current_line);
            $direction = $line_parts[0];
            $value = (int)$line_parts[1];

            switch ($direction) {
                case 'down':                    
                    // $current_depth += $value;     
                    $current_aim += $value;               
                    break;
                case 'up':
                    // $current_depth -= $value;
                    $current_aim -= $value;
                    break;
                case 'forward':
                    $current_hor += $value;
                    $current_depth += $current_aim * $value;
                    break;

                default:
                    echo "shit";
                    break;
            }
        }
        echo $current_depth . ' - ' . $current_hor . ' - ' . $current_aim . "\r\n";
    }
    fclose($file);
    echo $current_depth * $current_hor;
}
