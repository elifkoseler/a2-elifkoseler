from bottle import route, run, request, debug, default_app
from bottle import static_file, get
from hashlib import sha256

log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))

person1 = {'username':'Elif','password':'12345','comment': 'Huge fan of this website :p'}
person2 = {'username':'Bahadir','password':'6789','comment': 'Love it xx'}
person3 = {'username':'Sumeyye','password':'7777','comment':'Best I have ever seen!!'}

mylist = [person1, person2, person3]
	
def index():
    return static_file('index.html', root='./a1-elifkoseler')

def static_file_callback(filename):
    return static_file(filename, root='./a1-elifkoseler')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='./a1-elifkoseler/img')

def htmlify(title,text):
    mywebpagestring = '''
 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title> Lord of The Rings Film Series </title>
<link rel="icon" type="image/png" href="./icons/ring.png"/>
<!--<link rel="stylesheet" type=text/css href="./css/index.css"/>!-->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster">
</head>
<body>
  <h1>
Lord of The Rings Film Series </h1>

  <nav class="options-header">
  <ol>
  <li><a id="fs-header" href="fellowship.html">
  Lord of The Rings: The Fellowship of The Ring </a> <br/><br/>
  </li><li><a id="tw-header" href="tower.html">
  Lord of The Rings: The Two Towers  </a><br/><br/>
  </li><li><a id="kg-header" href="king.html">
  Lord of The Rings: The Return of The King  </a></li>
</ol>
  </nav>

<hr/>

   <b class="about-header">ABOUT THE TRIOLOGY</b>

<br/>
<p class="about">The Lord of the Rings is a film series consisting of three fantasy adventure films directed by <b>Peter Jackson</b>.<br/>
They are based on the novel The Lord of the Rings by <a href="tolkien.html"><b>J. R. R. Tolkien</b>.</a><br/><br/>
<img id="Peter"src="https://cdn.vox-cdn.com/thumbor/Xz00oL4Ot3LQpMPmObINfuZyicg=/0x40:960x680/1200x800/filters:focal(0x40:960x680)/cdn.vox-cdn.com/assets/2960799/Peter_Jackson_and_Gandalf.jpg">
<br/>Peter Jackson and Ian McKellen as Gandalf<br/><br/>
The films are subtitled The Fellowship of the Ring (2001),
The Two Towers (2002) and The Return of the King (2003).
They are a New Zealand-American venture produced by WingNut Films and The Saul Zaentz Company and distributed by New Line Cinema.
<br/><br/>
The trilogy was one of the biggest and most ambitious film projects ever undertaken.
It had a budget of $281 to <ins>$330 million </ins> depending on the source.
All three films were shot over eight years simultaneously and entirely in Jackson's native New Zealand.
One in every 160 New Zealanders was part of the production.
Each film in the series also had special extended editions released on DVD a year after their respective theatrical releases.
While the films follow the book's general storyline, they do omit some of the novel's plot elements and include some additions to and deviations from the source material.
<br/><br/>
<img id="trilogy"src="http://thefridacinema.org/wp-content/uploads/2018/07/The-Lord-of-the-Rings-Trilogy-Extended-Editions-at-The-Frida-Cinema.jpg">
<br/><br/>
Set in the fictional world of Middle-earth, the films follow the hobbit <i>Frodo Baggins (Elijah Wood)</i> as he and
the Fellowship embark on a quest to destroy the One Ring, and thus ensure the destruction of its maker,
the Dark Lord <i>Sauron</i>. The Fellowship eventually splits up and Frodo continues the quest together with his loyal companion <i>Sam (Sean Astin)</i> and the treacherous <i>Gollum (Andy Serkis)</i>.
Meanwhile, <i>Aragorn (Viggo Mortensen)</i>, heir in exile to the throne of <i>Gondor, Legolas, Gimli, Merry, Pippin,</i> and the wizard <i>Gandalf (Ian McKellen) </i>
unite to rally the Free Peoples of Middle-earth in the War of the Ring.
<br/><br/>
The series was received with overwhelming praise and was a major financial success, with the films collectively being among the highest-grossing film series of all time.
The films were critically acclaimed and heavily awarded, winning 17 out of 30 total <i>Academy Award</i> nominations. The final film in the series,
The Return of the King, won all 11 of its Academy Award nominations including Best Picture, which also tied it with Ben-Hur and Titanic for most Academy Awards received for a film. The series received wide praise for its innovative special and visual effects.
<br/>
<img id="oscar"src="https://www.empireonline.com/images/uploaded/return-of-the-king-oscar-stage.jpg">
<br/> Lord of The Rings win the Oscar.<br/>

</p>
<a class="about-source" href="https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)"><sup> source </sup></a>
<hr/>

<p class="cast">  <b class="cast-header">CAST</b>
<br/>
  <div class="gallery">

      <img src="images/frodo.jpg">

    <div class="desc">Elijah Wood as <i>Frodo Baggins</i></div>
  </div>

  <div class="gallery">

      <img src="images/sam.jpg">

    <div class="desc">Sean Astin as <i>Samwise 'Sam' Gamgee</i></div>
  </div>
  <div class="gallery">

      <img src="https://cdn.media.gazeteduvar.com/2017/12/gandalf.jpg">

    <div class="desc">Ian McKellen as <i>Gandalf </i></div>
  </div>
  <div class="gallery">

      <img src="https://nerdist.com/wp-content/uploads/2018/05/Lord-of-the-Rings-Aragorn-Viggo-Mortensen-1.jpg" >

    <div class="desc">Viggo Mortensen as <i>Aragorn </i></div>
  </div>

  <div class="gallery">

      <img src="https://vignette.wikia.nocookie.net/lotr/images/4/43/Gimli.jpg/revision/latest?cb=20080318220808" >

    <div class="desc">John Rhys-Davies as <i>Gimli</i></div>
  </div>
  <div class="gallery">

      <img src="http://pm1.narvii.com/6495/8867c85472503289f859634cfbfce34571516ccf_00.jpg" >

    <div class="desc"> Billy Boyd as <i>Peregrin 'Pippin' Took</i></div>
  </div>
  <div class="gallery">

      <img src="images/legolas.jpg" >

    <div class="desc"> Orlando Bloom as <i>Legolas Greenleaf</i> </div>
  </div>

  <div class="gallery">

      <img src="https://vignette.wikia.nocookie.net/3861f6ed-8e16-4d34-9c39-c9de8fc7074b/scale-to-width-down/800" >

    <div class="desc">Sean Bean as <i>Boromir</i> </div>
  </div>
  <div class="gallery">

      <img src="https://pbs.twimg.com/profile_images/555447406100480000/oKgqX5Mt_400x400.jpeg" >

    <div class="desc">Christopher Lee as <i>Saruman</i></div>
  </div>
  <div class="gallery">

      <img src="https://vignette.wikia.nocookie.net/lotr/images/f/fc/%28ARWEN._QUEEN.%2866%29.jpg/revision/latest?cb=20130630151908" >

    <div class="desc">Liv Tyler as <i>Arwen Undomiel </i></div>
  </div>
  <div class="gallery">

      <img src="https://vignette.wikia.nocookie.net/edain-mod/images/f/ff/Movies_the_hobbit_still_1.jpg/revision/latest?cb=20160505102219" >

    <div class="desc">Cate Blanchett as <i>Galadriel </i></div>
  </div>
  <div class="gallery">

      <img src="http://www.thewhitetree.org/wp-content/uploads/2015/12/Elrond.jpg" >

    <div class="desc">Hugo Weaving as <i>Elrond </i></div>
  </div>

  <div class="gallery">

      <img src="https://www.politikyol.com/wp-content/uploads/2017/04/gollum.png" >

    <div class="desc"> Andy Serkis as <i>Voice of Smeagol/Gollum</i></div>
  </div>
  <div class="gallery">

      <img src="images/sauron.jpg" >

    <div class="desc"> Sauron</div>
  </div>
<br/><br/>
</p>

<a class="cast-source" href="https://www.tvguide.com/movies/the-lord-of-the-rings-the-fellowship-of-the-ring/cast/134637/"><sup> source </sup></a>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><hr/>
<p id="made">
  Made by <a href="aboutme.html">Elif Koseler</a>
</p>

<form id="1">
	Username:<br>
  	<input type="text" name="username" required><br>
  	Password:<br>
	<input type="text" name="password" required><br>
	
	Choose your gender:<br>
	<input type="radio" name="gender" value="male" checked> Male<br>
 	<input type="radio" name="gender" value="female"> Female<br>
  	<input type="radio" name="gender" value="other"> Other<br>
	<b>Please select your age interval:</b>
	<select name="Age" style=color:red;>
    	<option value="15-20" selected>15-20</option>
    	<option value="20-30">20-30</option>
    	<option value="30-40" >30-40</option>
    	<option value="40-50">40-50</option>
	<option value="50+">50+</option>
  	</select>
	<br>
	Enter your comment:<br>
	<input type="text" name="comment" required><br>
	<input type="checkbox" name="lotr" value="lotr" style="color:gold;" required> I am fan of LOTR :)<br>
	
	<input type="submit" value="Send">
	</form>



</body>
<style>
form{	text-align:right;	
	}
body{
  background-color:NavajoWhite;
  font-family: "Lobster", serif;


}
h1{
  color: white;
  border: outset;
  border-color: gold;
  padding: 50px;
  text-align: center;
  text-shadow: 5px 5px 5px gold;
  letter-spacing: 4px;
  background-image: url("https://i.gifer.com/CGfq.gif");
  font-size: 40px;
  box-shadow: 5px 5px 5px grey;

}

.options-header{
  font-size: 20px;
  color:sienna;
  text-align: left;
  text-shadow: 3px 3px 5px gold;
  background-image: url('https://media2.giphy.com/media/V4uGHRgz0zi6Y/giphy.gif?cid=3640f6095be07f806d4e437855efebbf');
  padding: 40px;
  box-shadow: 5px 5px 5px grey;

}
#fs-header{
  color: Turquoise;


}
#tw-header{
  color: Aquamarine;

}
#kg-header{
  color: PaleTurquoise;

}
.about-header{
  color: Sienna;
  text-shadow: 3px 3px 5px gold;
  font-size: 25px;


}
.about{
    background-color: #F4BE57;
    width: 1300px;
    border: 20px solid gold;
    padding: 25px;
    margin: 25px;
    box-sizing: border-box;
    text-align: center;
    box-shadow: 10px 10px 5px grey;
}
#Peter{
  width:200px;height:150px;
  border-radius: 50%;
  border: 3px solid black;
}

#trilogy{
  width:550px; height:300px;
  border-radius: 10%;
  border: 3px solid black;
}

#oscar{
  width:450px; height: 300px;
  border-radius: 10%;
  border: 3px solid black;
}
.cast-header{
  color: Sienna;
  text-shadow: 3px 3px 5px gold;
  font-size: 25px;
}

div.gallery {
    margin: 5px;
    border: 1px ;
    float: left;
    width: 180px;
    box-shadow: 10px 10px 5px grey;
}
div.gallery img {
    width: 100%;
    height: 100%;
    border: 3px circle black ;

}

div.desc {
    background-color: SandyBrown;
    color: white;
    padding: 15px;
    text-align: center;

}
table, th, td {
    border: 1px dotted sienna;

}
.about-source{
  color: gold;
}
.cast-source{
  color: gold;
}
#made{
  color:sienna;
  border: 5px sienna dotted;
  text-align: left;
  width: 200px;
  background-color: gold;
}
</style>
 '''+text+'''
    ''' 
    return mywebpagestring

def create_hash(password):                  
    pw_bytestring = password.encode()       
    return sha256(pw_bytestring).hexdigest()

@route('/index.html')
def adder():
	global mylist
	html = '''<h2 style = "color:orange;text-shadow: 3px 2px red;"> Comments </h2>
'''
        isim = "username"
        sifre = "password"
        yorum ="comment"
       	hashing = create_hash(sifre)

        for person in mylist:
		if person["username"] == isim and create_hash(person["password"]) == hashing:
                	new={'username':isim,'password':hashing,'comment':yorum}
                	mylist.append(new)
	
		#if person["username"] == isim and create_hash(person["password"]) != hashing:
			#html+='''<p style="color:Orange;">
				#	<b>Please TRY AGAIN!</b>
				#</p>'''
	
		elif person["username"] != isim and create_hash(person["password"]) != hashing:
			new={'username':isim,'password':hashing,'comment':yorum}
			mylist.append(new)
			

	for who in mylist:
		html = html +''' <h4 style="color:brown;
				text-align:left; 
				text-decoration: underline;
				letter-spacing: 3px;
				text-shadow: 3px 2px gold;">
				%s
				</h4> 
				 <div style = "border: 5px dashed #D2691E;
				background-color:white;
  				width: 300px;	padding: 25px;
  				margin: 25px;
				color:">
				%s
				</div>''' %(who['username'],who['comment'])

	return htmlify("Comment Page",html)


route('/', 'GET', index)
#route('/<filename:path>', 'GET', static_file_callback)

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
