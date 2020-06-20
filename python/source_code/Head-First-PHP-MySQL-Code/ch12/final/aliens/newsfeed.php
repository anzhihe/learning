<?php header('Content-Type: text/xml'); ?>
<?php echo '<?xml version="1.0" encoding="utf-8"?>'; ?>
<rss version="2.0">
  <channel>
    <title>Aliens Abducted Me - Newsfeed</title>    <link>http://aliensabductedme.com/</link>    <description>Alien abduction reports from around the world courtesy of Owen and his abducted dog Fang.</description>    <language>en-us</language>

<?php
  require_once('connectvars.php');

  // Connect to the database 
  $dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME); 

  // Retrieve the alien sighting data from MySQL
  $query = "SELECT abduction_id, first_name, last_name, DATE_FORMAT(when_it_happened,'%a, %d %b %Y %T') AS when_it_happened_rfc, " .
    "alien_description, what_they_did FROM aliens_abduction ORDER BY when_it_happened DESC";
  $data = mysqli_query($dbc, $query);

  // Loop through the array of alien sighting data, formatting it as RSS
  while ($row = mysqli_fetch_array($data)) {
    // Display each row as an RSS item
    echo '<item>';
    echo '  <title>' . $row['first_name'] . ' ' . $row['last_name'] . ' - ' . substr($row['alien_description'], 0, 32) . '...</title>';
    echo '  <link>http://www.aliensabductedme.com/index.php?abduction_id=' . $row['abduction_id'] . '</link>';
    echo '  <pubDate>' . $row['when_it_happened_rfc'] . ' ' . date('T') . '</pubDate>';
    echo '  <description>' . $row['what_they_did'] . '</description>';
    echo '</item>';
  }
?>

  </channel>
</rss>
