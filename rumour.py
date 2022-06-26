import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import send_file
import string

from newinput import *
from googlesearch import *
from stanceself import *
from getreplies import *
from gettweettext import *

app = Flask(__name__)

@app.route('/rumour', methods = ['GET', 'POST'])
def upload_file1():
   return render_template('index.html')
	
@app.route('/app', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      #files = request.files.getlist('files[]')
      
      raw_message = request.form['message']

      raw_msg_split = raw_message.split("/")

      input_type = ""
      stanceresult = 2
      
      if "https:" in raw_msg_split:
         input_type = "url"
         message = gettweettext(raw_message)
         getreplies(raw_message)
      else:
         input_type = "normaltext"
         message = raw_message

      
      try:
          mlresult = rumourdetect(message)
      except:
          mlresult = 2
            
      googleresult = googlesearch(message)

      if input_type == "url":
         stanceresult = getstance()

      print(stanceresult)
      print(googleresult)
      print(mlresult)

      results = [mlresult, googleresult, stanceresult]
    
      #result = (googleresult + mlresult) / 2
      #gr = 1 = true
      #ml = 1 = true
      #sr = 1 = true
      

      '''

      if mlresult == 1 and googleresult == 0:
          result = 1
      elif mlresult == 0 and googleresult == 1:
          result = 1
      elif mlresult == 0 and googleresult == 0:
          result = 0
      elif mlresult == 0 and googleresult == 2:
          result = 2
      elif mlresult == 2 and googleresult == 0:
          result = 0
      elif mlresult == 2 and googleresult == 1:
          result = 1
      elif mlresult == 2 and googleresult == 2:
          result = 2
      else:
          result = 2

      '''
          
      if results[0] == 0:
         result = 0
      elif results[1] == 1:
         result = 1
      elif results[0] and results[1] == 2:
         result = 2
      elif results == [1,0,0]:
         result = 0
      elif results == [1,0,1]:
         result = 0
      elif results == [1,0,2]:
         result = 0
      elif results == [1,2,0]:
         result = 0
      elif results == [1,2,1]:
         result = 1
      elif results == [1,2,2]:
         result = 2
      elif results == [2,0,0]:
         result = 0
      elif results == [2,0,1]:
         result = 0
      elif results == [2,0,2]:
         result = 0
      
      


      print("Result = " + str(result))

      if result == 0:
          output = "Fake"
      elif result == 1:
          output = "True"
      else:
          output = "Unverified"
          

      return render_template('index.html', name = output)


@app.route('/download')
def download():
   outputFilename = "rumourdetails.txt"
   try:
      return send_file(outputFilename, as_attachment=True, attachment_filename=outputFilename)
   except Exception as e:
      return str(e)

		
if __name__ == '__main__':
   app.run(debug = True)
