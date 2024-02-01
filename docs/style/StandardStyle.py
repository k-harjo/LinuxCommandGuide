

class StandardStyle: 

    style = '''
    body, h1, h2, h3, p, pre, div, span, input, button, select { /* Add any other tags or classes as needed */
    font-family: 'Open Sans', sans-serif;

    .title h1 {{
  font-family: 'Open Sans', sans-serif; /* Choose a font family */
  color: #555; /* Dark grey color */
  font-size: 28px; /* Large font size */
  font-weight: 150; /* Lighter font weight */
  font-style: italic; /* Italic font style */
  margin-bottom: 10px; /* Space below the heading */
  text-align: center; /* Center the text */
}}
.title h1 span {{
  color: #555; /* Slightly lighter color */
  text-align: center; /* Center the text */
  font-size: 36px; /* Large font size */

  margin-bottom: 10px; /* Space below the heading */

}}
.title h1 em {{
  font-style: normal; /* Override italic style for emphasis */
  font-weight: bold; /* Bold font weight for emphasized text */
  font-size: 36px; /* Large font size */

  text-transform: uppercase; /* Uppercase text */
  color: #000; /* Black color */
  text-align: center; /* Center the text */
  display: block; /* Make 'em' a block element to allow margins */
  margin-top: 10px; /* Add space above 'em' */
  margin-bottom: 10px; /* Add space below 'em' */
}}

.title:after {{
  content: '';
  display: block;
  width: 50px; /* Width of the underline */
  height: 2px; /* Height of the underline */
  background: #000; /* Color of the underline */
  margin: 5px auto 0; /* Center the underline */
}}
                  
s1 {{
  text-align: left;
  font-family: 'Open Sans', sans-serif; /* Choose a font family */
  font-size: 16px;
  font-weight: 150;
}}
p {{
  text-align: justify;
  font-family: 'Open Sans', sans-serif; /* Choose a font family */
  font-size: 14px;
  color: black;
}}
pre {{ 
  white-space: pre-wrap;
  word-wrap:normal;
}}
/* ------- Helper Styles -------------*/
*,
*:before,
*:after {{
-moz-box-sizing: border-box;
-webkit-box-sizing: border-box;
box-sizing: border-box;
}}
body {{
background: #eee;
}}
div {{
position: relative;
background: #f8f8f8;
width: 90%;
max-width: 800px;
padding: 2em;
margin: 1.5em auto;
border: 3px solid rgba(0, 0, 0, 0.08);
}}
h1:before,
h1:after {{
background-color: #c50000;
}}
'''