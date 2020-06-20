<?php
  // Custom function to draw a bar graph given a data set, maximum value, and image filename
  function draw_bar_graph($width, $height, $data, $max_value, $filename) {
    // Create the empty graph image
    $img = imagecreatetruecolor($width, $height);    // Set a white background with black text and gray graphics    $bg_color = imagecolorallocate($img, 255, 255, 255);       // white    $text_color = imagecolorallocate($img, 255, 255, 255);     // white    $bar_color = imagecolorallocate($img, 0, 0, 0);            // black
    $border_color = imagecolorallocate($img, 192, 192, 192);   // light gray

    // Fill the background
    imagefilledrectangle($img, 0, 0, $width, $height, $bg_color);
    // Draw the bars
    $bar_width = $width / ((count($data) * 2) + 1);
    for ($i = 0; $i < count($data); $i++) {
      imagefilledrectangle($img, ($i * $bar_width * 2) + $bar_width, $height,
        ($i * $bar_width * 2) + ($bar_width * 2), $height - (($height / $max_value) * $data[$i][1]), $bar_color);
      imagestringup($img, 5, ($i * $bar_width * 2) + ($bar_width), $height - 5, $data[$i][0], $text_color);
    }

    // Draw a rectangle around the whole thing
    imagerectangle($img, 0, 0, $width - 1, $height - 1, $border_color);

    // Draw the range up the left side of the graph
    for ($i = 1; $i <= $max_value; $i++) {
      imagestring($img, 5, 0, $height - ($i * ($height / $max_value)), $i, $bar_color);
    }

    // Write the graph image to a file
    imagepng($img, $filename, 5);    imagedestroy($img);
  } // End of draw_bar_graph() function

  // Start the session
  require_once('startsession.php');

  // Insert the page header
  $page_title = 'My Mismatch';
  require_once('header.php');

  require_once('appvars.php');
  require_once('connectvars.php');

  // Make sure the user is logged in before going any further.
  if (!isset($_SESSION['user_id'])) {
    echo '<p class="login">Please <a href="login.php">log in</a> to access this page.</p>';
    exit();
  }

  // Show the navigation menu
  require_once('navmenu.php');

  // Connect to the database
  $dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

  // Only look for a mismatch if the user has questionnaire responses stored
  $query = "SELECT * FROM mismatch_response WHERE user_id = '" . $_SESSION['user_id'] . "'";
  $data = mysqli_query($dbc, $query);
  if (mysqli_num_rows($data) != 0) {
    // First grab the user's responses from the response table (JOIN to get the topic and category names)
    $query = "SELECT mr.response_id, mr.topic_id, mr.response, mt.name AS topic_name, mc.name AS category_name " .
      "FROM mismatch_response AS mr " .
      "INNER JOIN mismatch_topic AS mt USING (topic_id) " .
      "INNER JOIN mismatch_category AS mc USING (category_id) " .
      "WHERE mr.user_id = '" . $_SESSION['user_id'] . "'";
    $data = mysqli_query($dbc, $query);
    $user_responses = array();
    while ($row = mysqli_fetch_array($data)) {
      array_push($user_responses, $row);
    }

    // Initialize the mismatch search results
    $mismatch_score = 0;
    $mismatch_user_id = -1;
    $mismatch_topics = array();
    $mismatch_categories = array();

    // Loop through the user table comparing other people's responses to the user's responses
    $query = "SELECT user_id FROM mismatch_user WHERE user_id != '" . $_SESSION['user_id'] . "'";
    $data = mysqli_query($dbc, $query);
    while ($row = mysqli_fetch_array($data)) {
      // Grab the response data for the user (a potential mismatch)
      $query2 = "SELECT response_id, topic_id, response FROM mismatch_response WHERE user_id = '" . $row['user_id'] . "'";
      $data2 = mysqli_query($dbc, $query2);
      $mismatch_responses = array();
      while ($row2 = mysqli_fetch_array($data2)) {
        array_push($mismatch_responses, $row2);
      } // End of inner while loop

      // Compare each response and calculate a mismatch total
      $score = 0;
      $topics = array();
      $categories = array();
      for ($i = 0; $i < count($user_responses); $i++) {
        if ($user_responses[$i]['response'] + $mismatch_responses[$i]['response'] == 3) {
          $score += 1;
          array_push($topics, $user_responses[$i]['topic_name']);
          array_push($categories, $user_responses[$i]['category_name']);
        }
      }

      // Check to see if this person is better than the best mismatch so far
      if ($score > $mismatch_score) {
        // We found a better mismatch, so update the mismatch search results
        $mismatch_score = $score;
        $mismatch_user_id = $row['user_id'];
        $mismatch_topics = array_slice($topics, 0);
        $mismatch_categories = array_slice($categories, 0);
      }
    } // End of outer while loop

    // Make sure a mismatch was found
    if ($mismatch_user_id != -1) {
      $query = "SELECT username, first_name, last_name, city, state, picture FROM mismatch_user WHERE user_id = '$mismatch_user_id'";
      $data = mysqli_query($dbc, $query);
      if (mysqli_num_rows($data) == 1) {
        // The user row for the mismatch was found, so display the user data
        $row = mysqli_fetch_array($data);
        echo '<table><tr><td class="label">';
        if (!empty($row['first_name']) && !empty($row['last_name'])) {
          echo $row['first_name'] . ' ' . $row['last_name'] . '<br />';
        }
        if (!empty($row['city']) && !empty($row['state'])) {
          echo $row['city'] . ', ' . $row['state'] . '<br />';
        }
        echo '</td><td>';
        if (!empty($row['picture'])) {
          echo '<img src="' . MM_UPLOADPATH . $row['picture'] . '" alt="Profile Picture" /><br />';
        }
        echo '</td></tr></table>';

        // Display the mismatched topics in a table with four columns
        echo '<h4>You are mismatched on the following ' . count($mismatch_topics) . ' topics:</h4>';
        echo '<table><tr>';
        $i = 0;
        foreach ($mismatch_topics as $topic) {
          echo '<td>' . $topic . '</td>';
          if (++$i > 3) {
            echo '</tr><tr>';
            $i = 0;
          }
        }
        echo '</tr></table>';

        // Calculate the mismatched category totals
        $category_totals = array(array($mismatch_categories[0], 0));
        foreach ($mismatch_categories as $category) {
          if ($category_totals[count($category_totals) - 1][0] != $category) {
            array_push($category_totals, array($category, 1));
          }
          else {
            $category_totals[count($category_totals) - 1][1]++;
          }
        }

        // Generate and display the mismatched category bar graph image
        echo '<h4>Mismatched category breakdown:</h4>';
        draw_bar_graph(480, 240, $category_totals, 5, MM_UPLOADPATH . 'mymismatchgraph.png');
        echo '<img src="' . MM_UPLOADPATH . 'mymismatchgraph.png" alt="Mismatch category graph" /><br />';

        // Display a link to the mismatch user's profile
        echo '<h4>View <a href=viewprofile.php?user_id=' . $mismatch_user_id . '>' . $row['first_name'] . '\'s profile</a>.</h4>';
      } // End of check for a single row of mismatch user results
    } // End of check for a user mismatch
  } // End of check for any questionnaire response results
  else {
    echo '<p>You must first <a href="questionnaire.php">answer the questionnaire</a> before you can be mismatched.</p>';
  }

  mysqli_close($dbc);

  // Insert the page footer
  require_once('footer.php');
?>
