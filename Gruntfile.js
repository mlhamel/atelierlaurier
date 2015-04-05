module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        datetime: Date.now(),
        concat: {
            'atelierlaurier-js': {
                src: [
                    'bower_components/jquery/jquery.js',
                    'bower_components/bootstrap/dist/js/bootstrap.js'
                ],
                dest: 'atelierlaurier/static/js/atelierlaurier.js'
            }
        },
        uglify: {
            'options': {
                mangle: {toplevel: true},
                squeeze: {dead_code: false},
                codegen: {quote_keys: true}
            },
            'atelierlaurier-js': {
                src: 'atelierlaurier/static/js/atelierlaurier.js',
                dest: 'atelierlaurier/static/js/atelierlaurier.min.js'
            }
        }
    });


    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

     grunt.registerTask('default', [
        'concat:atelierlaurier-js',
        'uglify:atelierlaurier-js'
    ]);
}
