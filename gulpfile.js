var gulp = require('gulp'),
    sass = require('gulp-sass');

gulp.task('build-css', function () {
    return gulp
        .src('sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('css'));
});

gulp.task('watch', function () {
    gulp.watch('sass/**/*.scss', ['build-css']);
});

// Default Task
gulp.task('default', ['build-css']);
