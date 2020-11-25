#!/usr/bin/env python3
from logging import error
import os, sys
import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean

#DB
engine = create_engine('sqlite:///pwdata.db')
meta = MetaData()
conn = engine.connect()

data = Table(
'data', meta,
Column('id',Integer, primary_key=True),
Column('email',String),
Column('password',String)
)
meta.create_all(engine)

pfl=open("problemForlater",'w')

headers = {
    'User-Agent': 'Wer das sieht hat keine Hobbies'}
last=None
last=list(conn.execute('SELECT MAX(id),email,password from data'))
if last[0][0]==None:
    print("There is no last Data")
    last=None
else:
    print("There is last Data")
    lastp=last[0][2]
    last=last[0][1]

def store(email,pwd):
    try:
        conn.execute(data.insert().values(
                        email=email,
                        password=pwd
                    )
                )
    except KeyboardInterrupt:
        conn.close()
        engine.dispose()
        pfl.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as ex:
        print("DB: "+str(ex))
        conn.close()
        engine.dispose()
        pfl.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def send(email,pwd):
    try:
        req=requests.get("https://ipv6.benedikt-schwering.de/api/pwd/new", headers=headers, params=
            {
                "t":"U3VuIDIyIE5vdiAyMDIwIDEyOjU1OjQyIEFNIENFVAo",
                "email":email,
                "password":pwd
            }
        )
        if req.status_code != 200:
            print(f"{email}:{pwd}")
    except KeyboardInterrupt:
        conn.close()
        engine.dispose()
        pfl.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as e:
        print(f"{email}:{pwd}")
        error("Error reaching Server")
    

def processFile(path):
    f=open(path,'rb')
    try:
        while l:=f.readline():
            l=l.strip()
            l.replace(b"\t",b":")
            try:
                l=l.decode("utf-8")
            except:
                l=l.decode('latin1')
            l.replace("\t",":")
            try:
                i=l.index(':')
                email=l[:i]
                pwd=l[i+1:]
                store(email,pwd)
                send(email,pwd)
            except:
                try:
                    i=l.index(';')
                    email=l[:i]
                    pwd=l[i+1:]
                    store(email,pwd)
                    send(email,pwd)
                except:
                    pfl.write(l+"\n")
    except KeyboardInterrupt:
        conn.close()
        engine.dispose()
        pfl.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    f.close()
    pfl.flush()

def processFileRes(path):
    global last,lastp
    f=open(path,'rb')
    try:
        while l:=f.readline():
            l=l.strip()
            l.replace(b"\t",b":")
            try:
                l=l.decode("utf-8")
            except:
                l=l.decode('latin1')
            l.replace("\t",":")
            try:
                i=l.index(':')
                email=l[:i]
                pwd=l[i+1:]
                if email==last and pwd==lastp:
                    print("lastdata was found")
                    send(email,pwd)
                    last=None
                if last==None:
                    store(email,pwd)
                    send(email,pwd)
            except:
                try:
                    i=l.index(';')
                    email=l[:i]
                    pwd=l[i+1:]
                    if email==last and pwd==lastp:
                        print("lastdata was found")
                        last=None
                    if last==None:
                        store(email,pwd)
                        send(email,pwd)
                except:
                    pfl.write(l+"\n")
    except KeyboardInterrupt:
        conn.close()
        engine.dispose()
        pfl.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    f.close()
    pfl.flush()


def traverseDir(folderPath):
    num=0
    for subFolderRoot, foldersWithinSubFolder, files in os.walk(folderPath, topdown=False):
 
        for fileName in files:
            try:
                if last!=None:
                    file=str(os.path.join(subFolderRoot, fileName))
                    file=file.replace('BreachCompilation/data/',"")
                    file=file.replace("/","")
                    if last.startswith(file):
                        processFileRes(os.path.join(subFolderRoot, fileName))
                else:
                    processFile(os.path.join(subFolderRoot, fileName))
                    num+=1
                    print(num,end="\r")
            except KeyboardInterrupt:
                conn.close()
                engine.dispose()
                pfl.close()
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)

traverseDir('BreachCompilation/data')

