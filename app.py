from flask import Flask,jsonify,request
import json
import MySQLdb
app = Flask(__name__)

conn= MySQLdb.connect(
	'localhost',
	'root',
	'123',
	'testing')

a=conn.cursor()
#read
@app.route('/',methods=['GET'])
def readdb():
 	query='select * from details'
 	a.execute(query)
 	data=a.fetchall()
	return jsonify({"message":"success","name":data})


#write
@app.route('/test',methods = ['POST'])
def test():
	id= request.json['id']
	name= request.json['name']
	age = request.json['age']	
	a.execute("insert into details values('%s','%s','%s')" %(id,name,age))
	conn.commit()
	return jsonify({"message":"hi"})
	return redirect(url_for('/'))
#update
@app.route('/update',methods=['PUT'])
def funupdate():
	name=request.json['name']
	id= request.json['id']
	query="update details set name='%s' where id='%s'"%(name,id)
	a.execute(query)
	conn.commit()
	return jsonify({"message":"success"})
	return redirect(url_for('/'))

 #delete
@app.route('/delete1', methods=['delete'])
def deletefun():
 	age=request.json['age']
 	query="delete from details where age='%s'"%(age)
 	a.execute(query)
 	conn.commit()
 	return jsonify({"message":"success"})
 	return redirect(url_for('/'))

if __name__=="__main__":
	app.run()
