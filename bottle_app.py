from bottle import route, run, default_app, debug
from bottle import static_file

#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################



def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>
    """ % (title,text)
    return page

#def index():
#    return htmlify("My lovely website",
#                   "This is going to be an awesome website, when it is finished.")

def index():
    return static_file('index.html', root='./a1-elifkoseler')

def static_file_callback(filename):
    return static_file(filename, root='./a1-elifkoseler')


route('/', 'GET', index)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
