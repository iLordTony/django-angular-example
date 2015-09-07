/**
 * Created by Carlos Tonatihu on 01/09/2015.
 */
// Para el modulo static

// Se requiren las dependencias necesario ya que las usa el app.js
require('./static/controllers');
require('./static/app'); // Se require el app

// Modulo basic
require('./basic/services');
require('./basic/controllers');
require('./basic/app');

// Modulo resource
require('./resource/services');
require('./resource/controllers');
require('./resource/app');
