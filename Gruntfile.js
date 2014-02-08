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
			      'app/js/app.js': ['app/app/*.js']
			    }
			  }
			},
			browserifyBower: {
				options: {
					file: './app/js/lib.js'
				}
			},
			uglify: {
			  options: {
			    // the banner is inserted at the top of the output
			    banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n',
			    sourceMap: true,
			    preserveComments: false
			  },
			  dist: {
			    files: {
			      'app/js/app.min.js': ['app/js/app.js']
			    }
			  }
			},
			sass: {
				dist: {
					options: {
						style: 'expanded',
						lineNumbers: 'true',

					},
					files: [{
						expand: true,
						src: ['app/css/*.scss'],
						dest: './',
						ext: '.css'
					}]
				}
			},
			watch: {
				hint:{
					files: ['<%= jshint.files %>'],
					tasks: ['jshint']
				},
				sass: {
					files: ['<%= sass.files %>'],
					tasks:['sass']
				}
			}
	});

	//TODO add bower-resolve for angular libraries
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-browserify');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-clean');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-browserify-bower');

	grunt.registerTask('test', ['jshint']);
	grunt.registerTask('default', ['clean','browserify','jshint', 'uglify', 'sass']);
};
