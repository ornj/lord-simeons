module.exports = function(grunt) {
    var config = {
        base: './app/static',
        css: './app/static/css',
        js: './app/static/js'
    };

    grunt.initConfig({
        config: config,
        pkg: grunt.file.readJSON('package.json'),
        compass: {
            dist: {
                options: {
                    sassDir: '<%= config.css %>',
                    cssDir: '<%= config.css %>',
                    outputStyle: 'compressed'
                }
            }
        },
        watch: {
            css: {
                files: '<%= config.css %>/**/*',
                tasks: ['compass']
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['compass']);
};
