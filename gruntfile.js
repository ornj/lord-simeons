module.exports = function(grunt) {
    var config = {
        base: './',
        css: 'css',
        js: 'js'
    };

    // Callback prevents this from being evaluated
    var tmpl_compiled = '<%= config.tmpl.compiled %>';

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
