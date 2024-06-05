# automated puppet fix for an  Apache server that is returning a 500 error

exec { 'wordpress site typo fix':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
