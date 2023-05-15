import os
import subprocess
import re

def addImports(filename):
    filename.write("@use '../abstracts/icons' as icon;\n")
    filename.write("@use '../abstracts/colors' as color;\n")
    filename.write("@use '../abstracts/mixins' as mix;\n")
    filename.write("@use '../abstracts/functions' as func;\n")
    filename.write("@use '../abstracts/fonts' as font;\n")
    filename.write("@use '../abstracts/margins' as margin;\n")


# user input: projectname
print("Enter a project name: ")
projectname = input()

# remove non-alphanumeric and non-English letters characters using regular expression
projectnamet = re.sub(r'[^a-zA-Z0-9]+', '', projectname)

# remove the characters ä,ö,ü,å,ø,œ
projectname = projectname.translate(str.maketrans('', '', 'äöüåøœÄÖÜÅØŒß'))

# create root folder
os.mkdir(projectname)
os.chdir(projectname)

#create public folder and its subfolders
os.mkdir("public")
os.chdir("public")
#assets
os.mkdir("assets")
os.chdir("assets")
os.mkdir("images")
os.mkdir("js")
os.mkdir("videos")
os.mkdir("fonts")

#go back to root folder
os.chdir("../../")

#create src, sass folder and its subfolders
# src
os.mkdir("src")
os.chdir("src")
# src --> assets
os.mkdir("assets")
os.chdir("assets")
os.mkdir("images")
os.mkdir("js")
os.mkdir("videos")
os.mkdir("fonts")
os.chdir("../../")
#  src --> sass
os.chdir("src")
os.mkdir("sass")
os.chdir("sass")
os.mkdir("abstracts")
os.mkdir("base")
os.mkdir("components")
os.mkdir("layout")
os.mkdir("pages")
os.mkdir("themes")
os.mkdir("vendors")
os.chdir("../../")


# crate .scss-files
os.chdir("src/sass")

# abstracts
os.chdir("abstracts")
#_ icons.scss
icons = open("_icons.scss", "w")
icons.close()
#_ colors.scss
colors = open("_colors.scss", "w")
colors.close()
#_ mixins.scss
mixins = open("_mixins.scss", "w")
mixins.close()
#_ functions.scss
functions = open("_functions.scss", "w")
functions.close()
#_ fonts.scss
fonts = open("_fonts.scss", "w")
fonts.close()
#_ margins.scss
margins = open("_margins.scss", "w")
margins.close()
os.chdir("../")

# base
os.chdir("base")
#_ resets.scss
reset = open("_reset.scss", "w")
reset.close()
os.chdir("../")

# components
os.chdir("components")
# _buttons.scss
buttons = open("_buttons.scss", "w")
addImports(buttons)
buttons.close()
# _carousel.scss
carousel = open("_carousel.scss", "w")
addImports(carousel)
carousel.close()
os.chdir("../")


# layout
os.chdir("layout")
# _grid.scss
grid = open("_grid.scss", "w")
addImports(grid)
grid.close()
# _header.scss
header = open("_header.scss", "w")
addImports(header)
header.close()
# _main.scss
main = open("_main.scss", "w")
addImports(main)
main.close()
# _footer.scss
footer = open("_footer.scss", "w")
addImports(footer)
footer.close()
# _sidebar.scss
sidebar = open("_sidebar.scss", "w")
addImports(sidebar)
sidebar.close()
# _forms.scss
forms = open("_forms.scss", "w")
addImports(forms)
forms.close()
os.chdir("../")

# pages
os.chdir("pages")
# _home.scss
home = open("_home.scss", "w")
addImports(home)
home.close()
# _blog.scss
blog = open("_blog.scss", "w")
addImports(blog)
blog.close()
os.chdir("../")


# themes
os.chdir("themes")
# _light-theme.scss
lightTheme = open("_light-theme.scss", "w")
addImports(lightTheme)
lightTheme.close()
# _dark-theme.scss
darkTheme = open("_dark-theme.scss", "w")
addImports(darkTheme)
darkTheme.close()
os.chdir("../")


# go back to src
os.chdir("../")

# crate basic-html file
index = open("index.html", "w")
index.write("<!DOCTYPE html>\n")
index.write("<html lang='en'>\n")
index.write("<head>\n")
index.write("\t<meta charset='UTF-8'>\n")
index.write("\t<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n")
index.write("\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
index.write("\t<title>Sass Boilerplate</title>\n")
index.write("\t<link rel='stylesheet' href='style.css'>\n")
index.write("</head>\n")
index.write("<body>\n")
index.write("</body>\n")
index.write("</html>\n")
index.close()


# crate style.scss and import ALL scss-files
style = open("style.scss", "w")
style.write("@use '../abstracts/icons' as icon;\n")
style.write("@use '../abstracts/colors' as color;\n")
style.write("@use '../abstracts/mixins' as mix;\n")
style.write("@use '../abstracts/functions' as func;\n")
style.write("@use '../abstracts/fonts' as font;\n")
style.write("@use '../abstracts/margins' as margin;\n\n")
style.write("@use '../base/reset';\n\n")
style.write("@use '../components/buttons';\n")
style.write("@use '../components/carousel';\n\n")
style.write("@use '../layout/grid';\n")
style.write("@use '../layout/header';\n")
style.write("@use '../layout/main';\n")
style.write("@use '../layout/footer';\n")
style.write("@use '../layout/sidebar';\n")
style.write("@use '../layout/forms';\n\n")
style.write("@use '../pages/home';\n")
style.write("@use '../pages/blog';\n\n")
style.write("@use '../themes/light-theme';\n")
style.write("@use '../themes/dark-theme';\n")
style.close()

# go back to root
os.chdir("../")

# crate package.json-file
packageJson = open("package.json", "w")
packageJson.write('{\n')
packageJson.write('\t"name": "sass-boilerplate",\n')
packageJson.write('\t "version": "0.1.0",\n')
packageJson.write('\t"description": "SASS compile|autoprefix|minimize and live-reload dev server using Browsersync for static HTML",\n')
packageJson.write('\t "main": "public/index.html",\n')
packageJson.write('\t"author": "volkerson",\n')
packageJson.write('\t "scripts": {\n')
packageJson.write('\t\t "build:sass": "sass  --no-source-map src/sass:public",\n')
packageJson.write('\t\t"copy:assets": "copyfiles -u 1 ./src/assets/**/* public",\n')
packageJson.write('\t\t"copy:html": "copyfiles -u 1 ./src/*.html public",\n')
packageJson.write('\t\t"copy": "npm-run-all --parallel copy:*",\n')
packageJson.write('\t\t "watch:assets": "onchange \'src/assets/**/*\' -- npm run copy:assets",\n')
packageJson.write('\t\t "watch:html": "onchange \'src/*.html\' -- npm run copy:html",\n')
packageJson.write('\t\t"watch:sass": "sass  --no-source-map --watch src/sass:public",\n')
packageJson.write('\t\t "watch": "npm-run-all --parallel watch:*",\n')
packageJson.write('\t\t"serve": "browser-sync start --server public --files public",\n')
packageJson.write('\t\n')
packageJson.write('\t\t"start": "npm-run-all copy --parallel watch serve",\n')
packageJson.write('\t\t "build": "npm-run-all copy:html build:*",\n')
packageJson.write('\t\t "postbuild": "postcss public/css/*.css -u autoprefixer cssnano -r --no-map"\n')
packageJson.write('\t },\n')
packageJson.write('\t"dependencies": {\n')
packageJson.write('\t\t "autoprefixer": "^10.4.2",\n')
packageJson.write('\t\t"browser-sync": "^2.27.7",\n')
packageJson.write('\t\t"copyfiles": "^2.4.1",\n')
packageJson.write('\t\t"cssnano": "^5.0.17",\n')
packageJson.write('\t\t "npm-run-all": "^4.1.5",\n')
packageJson.write('\t\t "onchange": "^7.1.0",\n')
packageJson.write('\t\t"postcss-cli": "^9.1.0",\n')
packageJson.write('\t\t"sass": "^1.49.8"\n')
packageJson.write('\t}\n')
packageJson.write('}\n')
packageJson.close()


# chek if node is installed
subprocess.call(["npm","install"])

print("Your projet with the name " + projectname + " has been created!\nHappy coding. :)")