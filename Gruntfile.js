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
					'public/**/*.js',
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
			requirejs: {
				compile: {
					options: {
						appDir: 'public/',
						baseUrl: './js',
						dir: './public/build/js',
						paths: {
							angular: '../bower_components/angular/angular',
							ngRoute: '../bower_components/angular-route/angular-route',
							domReady: '../bower_components/requirejs-domready/domReady',
							text: '../bower_components/requirejs-text/text'
						},
						shim: {
							angular: {exports: 'angular'},
							ngRoute: {deps: ['angular']}
						},
						priority: [
							'angular'
						],
						locale: 'en-us',
						optimize: 'uglify2',
						generateSourceMaps: true,
						preserveLicenseComments: false,
						inlineText: true,
						modules: [
							{
								name: 'app'
							}
						],
						stubModules: ['text']
					}
				}
			},
			watch: {
				files: ['<%= jshint.files %>'],
				tasks: ['jshint']
			}
	});

	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-contrib-requirejs');
	grunt.loadNpmTasks('grunt-contrib-watch');

	grunt.registerTask('test', ['jshint']);
	grunt.registerTask('default', ['jshint']);
	grunt.registerTask('build', ['requirejs:compile']);
};
