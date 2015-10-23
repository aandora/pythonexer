var gulp = require('gulp');

var browserify = require('browserify');
var reactify = require('reactify');
var source = require('vinyl-source-stream');

gulp.task('js', function(){
    browserify('./app/static/js/src/index.jsx')
        .transform(reactify)
        .bundle()
        .pipe(source('index.js'))
        .pipe(gulp.dest('app/static/js/build/'));
});

gulp.task('default', ['js']);