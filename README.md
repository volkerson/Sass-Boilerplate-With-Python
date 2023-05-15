# Sass Boilerplate With Python - For MAC OS

This Python Script creates a projects folder with the recommended SASS-7-1-pattern architecture and runs npm install for you. So you're ready to code in no time!

# System
The script runs on Mac OS.
You need to have node.js installed. Otherwise the command npm install won't work.

# How to use
1. Download the python file and move it to the folder where you're creating your projects
2. Open the terminal
3. Run the Script: 
```
python3 sass-boilerplate.py
```
4. Type in your project name. All characters besidese A-z, A-Z and 0-9 will be removed.

The script creates the following project folder and files for you:<br>

```
root (your projectname)
| -- node_modules
| -- src
	|
	| -- index.html
	| -- package.json	
	|
	| -- assets
		| -- images
		| -- videos
		| -- fonts
		| -- js
	| -- sass
		| -- style.scss
		|
		| -- abstracts
			| -- _icons.scss
			| -- _colors.scss
			| -- _mixins.scss
			| -- _functions.scss
			| -- _fonts.scss
			| -- _margins.scss	
		| -- base
			| -- _reset.scss	
		| -- components
			| -- _buttons.scss
			| -- _carousel.scss	
		| -- layout
			| -- _grid.scss
			| -- _header.scss
			| -- _main.scss
			| -- _footer.scss
			| -- _sidebar.scss
			| -- _fonts.scss
			| -- _forms.scss	
		| -- pages
			| -- _home.scss
			| -- _blog.scss
		| -- themes
			| -- _light-theme.scss
			| -- _dark-theme.scss	
		| -- vendor
| -- public
	| -- style.css
	|
	| -- assets
		| -- images
		| -- videos
		| -- fonts
		| -- js		
		
```
The scss-file already import other scss-files they depend on. For example _main.scss has the starter code:

```
@use '../abstracts/icons' as icon;
@use '../abstracts/colors' as color;
@use '../abstracts/mixins' as mix;
@use '../abstracts/functions' as func;
@use '../abstracts/fonts' as font;
@use '../abstracts/margins' as margin;
```
If you're need changes in the architecture, want to remove or add files, feel free to edit the python-file.
