module.exports = function(grunt) {
	"use strict";

	//Grunt project configuration
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		banner: '* <%= pkg.description %> v<%=pkg.version %> by Dan Carter and Jaren Glover',
			jshint: {
				//define the files to lint
				files: [
					'Gruntfile.js',
					'app/js/app.js',
					'test/**/*.js',
					'!**/tests/**',
					'!node_modules',
					'!bower_components'
					],
				options: {
					//TODO add jshintrc file
						jshintrc: '.jshintrc'	
					}
			},
			clean: ["./app/js/app.js"],
			browserify: {
			  dist: {
			    files: {
			      'app/js/app.js': ['app/app/app.js']
			    }
			  }
			},
			watch: {
				files: ['<%= jshint.files %>'],
				tasks: ['jshint']
			}
	});

	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-browserify');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-clean');

	grunt.registerTask('test', ['jshint']);
	grunt.registerTask('default', ['browserify', 'jshint']);
};
