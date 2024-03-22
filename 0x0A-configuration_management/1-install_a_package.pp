# Install a version of flask (2.1.0)

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package {'werkzeug':
  ensure => '3.1.0',
  provider => 'pip3'
}
