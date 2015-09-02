/**
 * Created by Carlos Tonatihu on 01/09/2015.
 */
var gulp = require('gulp');
var browserify = require('browserify');

var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var uglify = require('gulp-uglify');

var stylus = require('gulp-stylus');
var nib = require('nib');
var concat = require('gulp-concat-css');
var minify = require('gulp-minify-css');

gulp.task('styl', function() {
    return gulp.src('./static/lib/app.styl')
        .pipe(stylus({use: nib()}))
        .pipe(concat('app.css'))
        .pipe(minify())
        .pipe(gulp.dest('./static/public/css'));
});

gulp.task('js', function () {
    return browserify({
        entries: './static/lib/app.js'
    })
    .bundle()
    .pipe(source('app.js'))
    .pipe(buffer())
    .pipe(uglify())
    .pipe(gulp.dest('./static/public'));
});
