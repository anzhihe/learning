<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Mismatch - View Profile</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>Mismatch - View Profile</h3>

<?php
  require_once('appvars.php');
  require_once('connectvars.php');

  // Connect to the database
  $dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

  // Grab the profile data from the database
  if (!isset($_GET['user_id'])) {
    $query = "SELECT username, first_name, last_name, gender, birthdate, city, state, picture FROM mismatch_user WHERE user_id = '$user_id'";
  }
  else {
    $query = "SELECT username, first_name, last_name, gender, birthdate, city, state, picture FROM mismatch_user WHERE user_id = '" . $_GET['user_id'] . "'";
  }
  $data = mysqli_query($dbc, $query);

  if (mysqli_num_rows($data) == 1) {
    // The user row was found so display the user data
    $row = mysqli_fetch_array($data);
    echo '<table>';
    if (!empty($row['username'])) {
      echo '<tr><td class="label">Username:</td><td>' . $row['username'] . '</td></tr>';
    }
    if (!empty($row['first_name'])) {
      echo '<tr><td class="label">First name:</td><td>' . $row['first_name'] . '</td></tr>';
    }
    if (!empty($row['last_name'])) {
      echo '<tr><td class="label">Last name:</td><td>' . $row['last_name'] . '</td></tr>';
    }
    if (!empty($row['gender'])) {
      echo '<tr><td class="label">Gender:</td><td>';
      if ($row['gender'] == 'M') {
        echo 'Male';
      }
      else if ($row['gender'] == 'F') {
        echo 'Female';
      }
      else {
        echo '?';
      }
      echo '</td></tr>';
    }
    if (!empty($row['birthdate'])) {
      if (!isset($_GET['user_id']) || ($user_id == $_GET['user_id'])) {
        // Show the user their own birthdate
        echo '<tr><td class="label">Birthdate:</td><td>' . $row['birthdate'] . '</td></tr>';
      }
      else {
        // Show only the birth year for everyone else
        list($year, $month, $day) = explode('-', $row['birthdate']);
        echo '<tr><td class="label">Year born:</td><td>' . $year . '</td></tr>';
      }
    }
    if (!empty($row['city']) || !empty($row['state'])) {
      echo '<tr><td class="label">Location:</td><td>' . $row['city'] . ', ' . $row['state'] . '</td></tr>';
    }
    if (!empty($row['picture'])) {
      echo '<tr><td class="label">Picture:</td><td><img src="' . MM_UPLOADPATH . $row['picture'] .
        '" alt="Profile Picture" /></td></tr>';
    }
    echo '</table>';
    if (!isset($_GET['user_id']) || ($user_id == $_GET['user_id'])) {
      echo '<p>Would you like to <a href="editprofile.php">edit your profile</a>?</p>';
    }
  } // End of check for a single row of user results
  else {
    echo '<p class="error">There was a problem accessing your profile.</p>';
  }

  mysqli_close($dbc);
?>
</body> 
</html>
