#!/usr/bin/env php
<?php
echo "Content-type: text/html\n\n";
echo "<html><head><title>PHP冒泡排序测试</title></head><body><pre>";
function bubble(array $array){
 for($i=0, $len=count($array)-1; $i<$len; ++$i){
     for($j=$len; $j>$i; --$j){
         if($array[$j] < $array[$j-1])
         {
             $temp = $array[$j];
             $array[$j] = $array[$j-1];
             $array[$j-1] = $temp;
         }
     }
 }
 return $array;
}
print_r(bubble(array(23,45,67,3,56,82,24,23,5,77,19,33,51,99)));
echo "</pre></body></html>";
?>