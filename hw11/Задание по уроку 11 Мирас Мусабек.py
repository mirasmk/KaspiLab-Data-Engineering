"""
demo.py

Christopher Jones, 10 Sep 2020

Demo of using flask with Oracle Database

Before running, set these environment variables:

    PYTHON_USERNAME       - your DB username
    PYTHON_PASSWORD       - your DB password
    PYTHON_CONNECTSTRING  - the connection string to the DB, e.g. "example.com/XEPDB1"
    PORT                  - port the web server will listen on.  The default in 8080

"""

import os
import cx_Oracle
from flask import Flask, jsonify, session

def init_session(connection, requestedTag_ignored):
    cursor = connection.cursor()
    cursor.execute("""
        ALTER SESSION SET
          TIME_ZONE = 'UTC'
          NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI'""")

# start_pool(): starts the connection pool
def start_pool():

    # Generally a fixed-size pool is recommended, i.e. pool_min=pool_max.
    # Here the pool contains 4 connections, which is fine for 4 conncurrent
    # users.
    #
    # The "get mode" is chosen so that if all connections are already in use, any
    # subsequent acquire() will wait for one to become available.

    pool_min = 4
    pool_max = 4
    pool_inc = 0
    pool_gmd = cx_Oracle.SPOOL_ATTRVAL_WAIT

    print("Connecting to", "C##MARFINI")

    pool = cx_Oracle.SessionPool(user="C##MARFINI",
                                 password="250598",
                                 dsn=os.environ.get("localhost:1521/xe"),
                                 min=pool_min,
                                 max=pool_max,
                                 increment=pool_inc,
                                 threaded=True,
                                 getmode=pool_gmd,
                                 sessionCallback=init_session)

    return pool

################################################################################
#
# Specify some routes
#
# The default route will display a welcome message:
#   http://127.0.0.1:33507/

app = Flask(__name__)
app.secret_key = 'dljsaklqk24qwerfdsae21cj234n!Ewew@@dsa5'
# Display a welcome message on the 'home' page
@app.route('/')
def index():
    return "Welcome to the Kaspi app"

@app.route('/hw10_1')
def show_table():
    connection = pool.acquire()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hw10_1 WHERE hw10_1.intervention_name='Ozanimod'")
    data = cursor.fetchall()
    session["data"] = data
    return jsonify(data)

@app.route('/hw10_1/insert')
def show_table_insert():
    data = session.get("data",None)
    connection = pool.acquire()
    cursor = connection.cursor()
    connection.autocommit = True
    print(data)
    for i in data:
        sql = "INSERT INTO hw11(NCT_ID, BRIEF_TITLE, SPONSORS_LEAD_SPONSOR_AGENCY, SPONSORS_LEAD_SPONSOR_AGENCY_CLASS, SPONSORS_COLLABORATOR_1_AGENCY, SPONSORS_COLLABORATOR_1_AGENCY_CLASS, SPONSORS_COLLABORATOR_2_AGENCY, SPONSORS_COLLABORATOR_2_AGENCY_CLASS, SPONSORS_COLLABORATOR_3_AGENCY, SPONSORS_COLLABORATOR_3_AGENCY_CLASS, START_DATE, COMPLETION_DATE, STUDY_DESIGN_INFO_OBSERVATIONAL_MODEL, STUDY_DESIGN_INFO_TIME_PERSPECTIVE, PRIMARY_OUTCOME_MEASURE, PRIMARY_OUTCOME_TIME_FRAME, SECONDARY_OUTCOME_1_MEASURE, SECONDARY_OUTCOME_1_TIME_FRAME, SECONDARY_OUTCOME_2_MEASURE, SECONDARY_OUTCOME_2_TIME_FRAME, INTERVENTION_TYPE, INTERVENTION_NAME, INTERVENTION_DESCRIPTION, INTERVENTION_ARM_GROUP_LABEL, LOCATION_1_FACILITY_NAME, LOCATION_1_FACILITY_ADDRESS_CITY, LOCATION_1_FACILITY_STATE, LOCATION_1_FACILITY_ZIP, LOCATION_1_FACILITY_COUNTRY, LOCATION_2_FACILITY_NAME, LOCATION_2_FACILITY_ADDRESS_CITY, LOCATION_2_FACILITY_STATE, LOCATION_2_FACILITY_ZIP, LOCATION_2_FACILITY_COUNTRY, LOCATION_3_FACILITY_NAME, LOCATION_3_FACILITY_ADDRESS_CITY, LOCATION_3_FACILITY_STATE, LOCATION_3_FACILITY_ZIP, LOCATION_3_FACILITY_COUNTRY) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26, :27, :28, :29, :30, :31, :32, :33, :34, :35, :36, :37, :38, :39)"
        cursor.execute(sql, tuple(i))
    return 'Data Inserted Successfully'

################################################################################
#
# Initialization is done once at startup time
#

if __name__ == '__main__':

    # Start a pool of connections
    pool = start_pool()

    # Start a webserver
    app.run(port=int(os.environ.get('PORT', '33507')))
