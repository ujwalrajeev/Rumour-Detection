import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import send_file
import string

from newinput import *
from googlesearch import *

app = Flask(__name__)

@app.route('/rumour', methods = ['GET', 'POST'])
def upload_file1():
   return render_template('index.html')
	
@app.route('/app', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      #files = request.files.getlist('files[]')
      
      message = request.form['message']

      
      try:
          mlresult = rumourdetect(message)
      except:
          mlresult = 2
            
      googleresult = googlesearch(message)
      print(googleresult)
      print(mlresult)
    
      #result = (googleresult + mlresult) / 2

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
   nameOfFiles = open('nameOfFiles.txt', 'r')
   nf1 = nameOfFiles.readlines()
   outputFilename = nf1[2]
   outputFilename = outputFilename.rstrip('\n')
   filename = nf1[2].rstrip('\n')
   textOutputFilename = nf1[1]
   try:
      return send_file(outputFilename, as_attachment=True, attachment_filename=filename)
   except Exception as e:
      return str(e)
   nameOfFiles.close()

@app.route('/downloadtextfile')
def downloadtextfile():
   nameOfFiles = open('nameOfFiles.txt', 'r')
   nf1 = nameOfFiles.readlines()
   outputFilename = nf1[0] 
   textOutputFilename = nf1[1]
   try:
      return send_file(textOutputFilename, as_attachment=True, attachment_filename=nf1[1])
   except Exception as e:
      return str(e)
   nameOfFiles.close()

		
if __name__ == '__main__':
   app.run(debug = True)
