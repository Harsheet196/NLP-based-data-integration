import pymongo

mgoclient = pymongo.MongoClient("mongodb://localhost:27017/")
mgodb = mgoclient["temp1"]
mgocol = mgodb["harsh"]
mgocol.create_index("ID", unique=True)
row = {'user_id': 3, 'name': 'harsh sharma', 'email': 'test2@test.com', 'phone': '1234567', 'password': 'd4e3730e8cba214f85cddae5f9331d74',
       'image': '1641493921.jpg', 'status': 1, }
mgocol.insert_one(row)
