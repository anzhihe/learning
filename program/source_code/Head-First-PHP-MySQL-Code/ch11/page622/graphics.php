<?php
  define('IMG_WIDTH', 101);    // width of image
  define('IMG_HEIGHT', 101);   // height of image

  // Create the image  $img = imagecreatetruecolor(IMG_WIDTH, IMG_HEIGHT);  // Set a white background with black text and gray graphics  $white_color = imagecolorallocate($img, 255, 255, 255);     // white  $black_color = imagecolorallocate($img, 0, 0, 0);         // black  $gray_color = imagecolorallocate($img, 128, 128, 128);   // dark gray

  // Fill the background
  imagefilledrectangle($img, 0, 0, IMG_WIDTH, IMG_HEIGHT, $white_color);
  imagerectangle($img, 0, 0, IMG_WIDTH - 1, IMG_HEIGHT - 1, $gray_color);

  // Robot head
/*
  imagefilledrectangle($img, 10, 10, 90, 60, $gray_color);
  imagesetpixel($img, 30, 25, $black_color);
  imagesetpixel($img, 70, 25, $black_color);
  imageline($img, 35, 45, 65, 45, $black_color);
  imagefilledrectangle($img, 45, 50, 55, 90, $gray_color);
*/

  // Earth and moon
/*  imageellipse($img, 45, 45, 70, 70, $black_color);
  imagefilledellipse($img, 75, 75, 30, 30, $gray_color);
  imagesetpixel($img, 10, 10, $black_color);
  imagesetpixel($img, 80, 15, $black_color);
  imagesetpixel($img, 20, 15, $black_color);
  imagesetpixel($img, 90, 60, $black_color);
  imagesetpixel($img, 20, 80, $black_color);
  imagesetpixel($img, 45, 90, $black_color);
*/
  // Square circle square
/*
  imagefilledrectangle($img, 10, 10, 90, 90, $gray_color);
  imagefilledellipse($img, 50, 50, 60, 60, $white_color);
  imagefilledrectangle($img, 40, 40, 60, 60, $black_color);
*/

  // House
/*
  imagefilledrectangle($img, 25, 35, 75, 90, $black_color);
  imageline($img, 10, 50, 50, 10, $black_color);
  imageline($img, 50, 10, 90, 50, $black_color);
  imagefilledrectangle($img, 45, 65, 55, 90, $white_color);
  imageline($img, 0, 90, 100, 90, $black_color);
*/

  // Molecule
  imageline($img, 15, 15, 50, 50, $black_color);
  imageline($img, 15, 85, 50, 50, $black_color);
  imageline($img, 50, 50, 85, 50, $black_color);
  imagefilledellipse($img, 15, 15, 20, 20, $gray_color);
  imagefilledellipse($img, 15, 85, 20, 20, $gray_color);
  imagefilledellipse($img, 50, 50, 20, 20, $gray_color);
  imagefilledellipse($img, 85, 50, 20, 20, $gray_color);

  // Output the image as a PNG using a header  header("Content-type: image/png");  imagepng($img);
  imagedestroy($img);?>
