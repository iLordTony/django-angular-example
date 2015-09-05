/**
 * Created by Carlos Tonatihu on 01/09/2015.
 */
var gulp = require('gulp');
var browserify = require('browserify'); // Para requrir liberias
// Para trabajar con JS
var source = require('vinyl-source-stream'); // Para poner el archivo de destino
var buffer = require('vinyl-buffer');
var uglify = require('gulp-uglify'); // Minifica

// Cosas para que funcione el compilador de styl
var stylus = require('gulp-stylus'); // Stylus duh!
var nib = require('nib'); // Para poder usar mixins y cosas asi
var concat = require('gulp-concat-css'); // Compilar todo en un archivo
var minify = require('gulp-minify-css'); // Minifica el css duh!

gulp.task('build', ['styl', 'js']);

gulp.task('styl', function() {
    return gulp.src('./static/app/app.styl')
        .pipe(stylus({use: nib()}))
        .pipe(concat('app.css'))
        .pipe(minify())
        .pipe(gulp.dest('./static/public/css'));
});

gulp.task('js', function () {
    return browserify({
        entries: './static/app/app.js'
    })
    .bundle()
    .pipe(source('app.js'))
    .pipe(buffer())
    .pipe(uglify())
    .pipe(gulp.dest('./static/public'));
});
