import gdrive as g
txts=[]
g.files={}


folderid='0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'
g.q=SimpleQueue()
g.q.put(folderid)

gauth = g.GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = g.GoogleDrive(gauth)


g.bfs(drive)
txts=g.get_content_files()
get_contents(txts)


download(txts,300,100)
a_file = open("files.json", "w")
json.dump(files, a_file)
a_file.close()




f_file = open("files.json", "r")
files = json.load(f_file)



fileList = drive.ListFile({'q': "'0B0Rlpx3MRZ1SLVFXRFctd0t1cDA' in parents and trashed=false"}).GetList()
for file in fileList:
	print(file)

 # print('Title: %s, ID: %s' % (file['title'], file['id']))
 MyFiles=["2019-2020 Spring"]

folderid='0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'
value="'%s' in parents" % (folderid )
s={}
 
