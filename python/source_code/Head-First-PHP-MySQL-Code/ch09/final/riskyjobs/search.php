<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Risky Jobs - Search</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <img src="riskyjobs_title.gif" alt="Risky Jobs" />
  <img src="riskyjobs_fireman.jpg" alt="Risky Jobs" style="float:right" />
  <h3>Risky Jobs - Search Results</h3>

<?php
  // This function builds a search query from the search keywords and sort setting
  function build_query($user_search, $sort) {
    $search_query = "SELECT * FROM riskyjobs";

    // Extract the search keywords into an array
    $clean_search = str_replace(',', ' ', $user_search);
    $search_words = explode(' ', $clean_search);
    $final_search_words = array();
    if (count($search_words) > 0) {
      foreach ($search_words as $word) {
        if (!empty($word)) {
          $final_search_words[] = $word;
        }
      }
    }

    // Generate a WHERE clause using all of the search keywords
    $where_list = array();
    if (count($final_search_words) > 0) {
      foreach($final_search_words as $word) {
        $where_list[] = "description LIKE '%$word%'";
      }
    }
    $where_clause = implode(' OR ', $where_list);

    // Add the keyword WHERE clause to the search query
    if (!empty($where_clause)) {
      $search_query .= " WHERE $where_clause";
    }

    // Sort the search query using the sort setting
    switch ($sort) {
    // Ascending by job title
    case 1:
      $search_query .= " ORDER BY title";
      break;
    // Descending by job title
    case 2:
      $search_query .= " ORDER BY title DESC";
      break;
    // Ascending by state
    case 3:
      $search_query .= " ORDER BY state";
      break;
    // Descending by state
    case 4:
      $search_query .= " ORDER BY state DESC";
      break;
    // Ascending by date posted (oldest first)
    case 5:
      $search_query .= " ORDER BY date_posted";
      break;
    // Descending by date posted (newest first)
    case 6:
      $search_query .= " ORDER BY date_posted DESC";
      break;
    default:
      // No sort setting provided, so don't sort the query
    }

    return $search_query;
  }

  // This function builds heading links based on the specified sort setting
  function generate_sort_links($user_search, $sort) {
    $sort_links = '';

    switch ($sort) {
    case 1:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=2">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=5">Date Posted</a></td>';
      break;
    case 3:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=1">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=4">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">Date Posted</a></td>';
      break;
    case 5:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=1">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=6">Date Posted</a></td>';
      break;
    default:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=1">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=5">Date Posted</a></td>';
    }

    return $sort_links;
  }

  // This function builds navigational page links based on the current page and the number of pages
  function generate_page_links($user_search, $sort, $cur_page, $num_pages) {
    $page_links = '';

    // If this page is not the first page, generate the "previous" link
    if ($cur_page > 1) {
      $page_links .= '<a href="' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=' . $sort . '&page=' . ($cur_page - 1) . '"><-</a> ';
    }
    else {
      $page_links .= '<- ';
    }

    // Loop through the pages generating the page number links
    for ($i = 1; $i <= $num_pages; $i++) {
      if ($cur_page == $i) {
        $page_links .= ' ' . $i;
      }
      else {
        $page_links .= ' <a href="' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=' . $sort . '&page=' . $i . '"> ' . $i . '</a>';
      }
    }

    // If this page is not the last page, generate the "next" link
    if ($cur_page < $num_pages) {
      $page_links .= ' <a href="' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=' . $sort . '&page=' . ($cur_page + 1) . '">-></a>';
    }
    else {
      $page_links .= ' ->';
    }

    return $page_links;
  }

  // Grab the sort setting and search keywords from the URL using GET
  $sort = $_GET['sort'];
  $user_search = $_GET['usersearch'];

  // Calculate pagination information
  $cur_page = isset($_GET['page']) ? $_GET['page'] : 1;
  $results_per_page = 5;  // number of results per page
  $skip = (($cur_page - 1) * $results_per_page);

  // Start generating the table of results
  echo '<table border="0" cellpadding="2">';

  // Generate the search result headings
  echo '<tr class="heading">';
  echo generate_sort_links($user_search, $sort);
  echo '</tr>';

  // Connect to the database
  require_once('connectvars.php');
  $dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

  // Query to get the total results 
  $query = build_query($user_search, $sort);
  $result = mysqli_query($dbc, $query);
  $total = mysqli_num_rows($result);
  $num_pages = ceil($total / $results_per_page);

  // Query again to get just the subset of results
  $query =  $query . " LIMIT $skip, $results_per_page";
  $result = mysqli_query($dbc, $query);
  while ($row = mysqli_fetch_array($result)) {
    echo '<tr class="results">';
    echo '<td valign="top" width="20%">' . $row['title'] . '</td>';
    echo '<td valign="top" width="50%">' . substr($row['description'], 0, 100) . '...</td>';
    echo '<td valign="top" width="10%">' . $row['state'] . '</td>';
    echo '<td valign="top" width="20%">' . substr($row['date_posted'], 0, 10) . '</td>';
    echo '</tr>';
  } 
  echo '</table>';

  // Generate navigational page links if we have more than one page
  if ($num_pages > 1) {
    echo generate_page_links($user_search, $sort, $cur_page, $num_pages);
  }

  mysqli_close($dbc);
?>

</body>
</html>
