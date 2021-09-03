#!/usr/bin/python

from __future__ import print_function

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'db'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )


print( "Using psycopg2:" )
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()
