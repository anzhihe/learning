<?php  define('YOUTUBE_URL', 'http://gdata.youtube.com/feeds/api/users/aliensabductedme/favorites');
  define('NUM_VIDEOS', 5);

  // Read the XML data into an object  $xml = simplexml_load_file(YOUTUBE_URL);

  $num_videos_found = count($xml->entry);
  if ($num_videos_found > 0) {
    echo '<table><tr>';
    for ($i = 0; $i < min($num_videos_found, NUM_VIDEOS); $i++) {
      // Get the title
      $entry = $xml->entry[$i];
      $media = $entry->children('http://search.yahoo.com/mrss/');      $title = $media->group->title;

      // Get the duration in minutes and seconds, and then format it
      $yt = $media->children('http://gdata.youtube.com/schemas/2007');      $attrs = $yt->duration->attributes();      $length_min = floor($attrs['seconds'] / 60);
      $length_sec = $attrs['seconds'] % 60;
      $length_formatted = $length_min . (($length_min != 1) ? ' minutes, ':' minute, ') .
        $length_sec . (($length_sec != 1) ? ' seconds':' second');

      // Get the video URL
      $attrs = $media->group->player->attributes();      $video_url = $attrs['url'];

      // Get the thumbnail image URL
      $attrs = $media->group->thumbnail[0]->attributes();      $thumbnail_url = $attrs['url']; 

      // Display the results for this entry
      echo '<td style="vertical-align:bottom; text-align:center" width="' . (100 / NUM_VIDEOS) . '%"><a href="' . $video_url . '">' .
        $title . '<br /><span style="font-size:smaller">' . $length_formatted . '</span><br /><img src="' . $thumbnail_url . '" /></a></td>';    }
    echo '</tr></table>';
  }
  else {
    echo '<p>Sorry, no videos were found.</p>';
  }?>