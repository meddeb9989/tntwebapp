#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from flask import render_template, redirect, request
import sys
import subprocess
import time
from .flask_app import app
from pagination import Paginate
import requests
from user import User
import json
from requests.auth import HTTPDigestAuth


app.token=None
app.website_url="http://localhost:8000/"

@app.route('/')
def index():
    return redirect("/signin/")


@app.route("/signin/", methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        response = render_template("login.html")
    else:
        login = request.form['login']
        password = request.form['passwd']

        r = requests.post(app.website_url+"api-token-auth/", data={"username": login,"password":password})
        token =json.loads(r.text)

        if u'non_field_errors' in token:
            response = render_template("login.html", msg="Login ou mot de passe Incorrect !")
        else:
            app.token = token[u'token']
            url=app.website_url+"user/"
            r=requests.get(url, headers={'Authorization': 'Token '+app.token})
            user=json.loads(r.text)[0]
            if user['valid']:
              print user
              if u'&' in user['group']:
                  response = redirect("/view_choice/")
              else:
                  response = redirect("/home/")

    return response

@app.route("/view_choice/", methods=['GET', 'POST'])
def view_choice():
    if request.method == 'GET' and app.token!=None:
        response = render_template("choice.html")
    elif request.method == 'POST' and app.token!=None:
        index_search = "/home/user_type=" + request.form['btn']
        response = redirect(index_search)
    else:
        response = redirect("/")

    return response

@app.route('/profile/', methods=['GET', 'POST'])
def user_Profile():
    if request.method == 'GET' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]
        if user['valid']:
            username = user['name']
            response = render_template("profile.html", username=username)
        else:
            response = redirect("/signout/")
    elif request.method == 'POST' and app.token!=None:
      pass
    else:
        response = redirect("/signout/")

    return response

@app.route("/signout/")
def signout():
    app.token=None
    r = requests.get(app.website_url+"logout")
    return redirect("/")


@app.route('/home/', methods=['GET', 'POST'], defaults={'page': 1, 'validation': "", 'search_text': "", 'user_type': ""})
@app.route('/home/user_type=<user_type>', methods=['GET', 'POST'], defaults={'page': 1, 'validation': "", 'search_text': ""})
@app.route('/home/page=<int:page>', methods=['GET', 'POST'], defaults={'validation': "", 'search_text': "", 'user_type': ""})
@app.route('/home/search_text=<search_text>', methods=['GET', 'POST'], defaults={'validation': "", 'page': 1, 'user_type': ""})
@app.route('/home/search_text=<search_text>_page=<int:page>', methods=['GET', 'POST'], defaults={'validation': "", 'user_type': ""})
@app.route('/home/user_type=<user_type>_page=<int:page>', methods=['GET', 'POST'], defaults={'validation': "", 'search_text': ""})
@app.route('/home/user_type=<user_type>_search_text=<search_text>', methods=['GET', 'POST'], defaults={'validation': "", 'page': 1})
@app.route('/home/user_type=<user_type>_search_text=<search_text>_page=<int:page>', methods=['GET', 'POST'], defaults={'validation': ""})
def my_home_page(page, validation, search_text, user_type):
    if request.method == 'GET' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]
        if user['valid']:

            if search_text == "" and validation == "" and user_type == "":
                pagination_for = "/home/page"
            elif search_text == "" and user_type == "":
                pagination_for = "/home/validation="+validation+"_page"
            elif validation == "" and user_type == "":
                pagination_for = "/home/search_text="+search_text+"_page"
            elif search_text == "" and validation == "":
                pagination_for = "/home/user_type="+user_type+"_page"
            elif validation == "":
                pagination_for = "/home/user_type="+user_type+"_search_text="+search_text+"_page"
            else:
                pagination_for = "/home/user_type="+user_type+"_search_text="+search_text+"_validation="+validation+"_page"

            if u'&' in user['group']:
                if user_type!="" and user_type == "Employeur":
                    url=app.website_url+"rh_cards/"
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                    cartes=json.loads(r.text)
                    del cartes[0]

                    paginate = Paginate(5)
                    Mylist, pages = paginate.getListAndPages(cartes, page, search_text)
                
                    if pages < page:
                        page = pages

                    response = render_template("home.html",
                                               usertype=user_type,
                                               user=user['name'],
                                               userid=user['id'],
                                               currentPage=page,
                                               numberOfPages=pages,
                                               validation=validation,
                                               MyCampainsList=Mylist,
                                               search_text=search_text,
                                               pagination_for=pagination_for,
                                               itemPerPage = paginate.itemPerPage)

                elif user_type!="" and user_type == "Employe":
                    url=app.website_url+"transactions/"
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                    transactions=json.loads(r.text)
                    del transactions[0]
    
                    url=app.website_url+"amount/"
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                    solde=json.loads(r.text)[0]['amount']
    
                    paginate = Paginate(5)
                    Mylist, pages = paginate.getListAndPages(transactions, page, search_text)
    
                    if pages < page:
                        page = pages
    
                    response = render_template("home.html",
                                               usertype=user_type,
                                               user=user['name'],
                                               userid=user['id'],
                                               solde=solde,
                                               currentPage=page,
                                               numberOfPages=pages,
                                               validation=validation,
                                               MyCampainsList=Mylist,
                                               search_text=search_text,
                                               pagination_for=pagination_for,
                                               itemPerPage = paginate.itemPerPage)

                else:
                    response = redirect("/view_choice/")

            elif user['group']==u'Employeur':
                url=app.website_url+"cards/"
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                cartes=json.loads(r.text)
                del cartes[0]

                paginate = Paginate(5)
                Mylist, pages = paginate.getListAndPages(cartes, page, search_text)
                
                if pages < page:
                    page = pages

                response = render_template("home.html",
                                           usertype=user['group'],
                                           user=user['name'],
                                           userid=user['id'],
                                           currentPage=page,
                                           numberOfPages=pages,
                                           validation=validation,
                                           MyCampainsList=Mylist,
                                           search_text=search_text,
                                           pagination_for=pagination_for,
                                           itemPerPage = paginate.itemPerPage)

            elif user['group']==u'Employe':
                url=app.website_url+"transactions/"
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                transactions=json.loads(r.text)
                del transactions[0]

                url=app.website_url+"amount/"
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                solde=json.loads(r.text)[0]['amount']

                paginate = Paginate(5)
                Mylist, pages = paginate.getListAndPages(transactions, page, search_text)

                if pages < page:
                    page = pages

                response = render_template("home.html",
                                           usertype=user['group'],
                                           user=user['name'],
                                           userid=user['id'],
                                           solde=solde,
                                           currentPage=page,
                                           numberOfPages=pages,
                                           validation=validation,
                                           MyCampainsList=Mylist,
                                           search_text=search_text,
                                           pagination_for=pagination_for,
                                           itemPerPage = paginate.itemPerPage)
            else:
                url=app.website_url+"transactions/"
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                transactions=json.loads(r.text)
                del transactions[0]

                paginate = Paginate(5)
                Mylist, pages = paginate.getListAndPages(transactions, page, search_text)

                if pages < page:
                    page = pages

                response = render_template("home.html",
                                           usertype=user['type'],
                                           user=user['name'],
                                           userid=user['id'],
                                           currentPage=page,
                                           numberOfPages=pages,
                                           validation=validation,
                                           MyCampainsList=Mylist,
                                           search_text=search_text,
                                           pagination_for=pagination_for,
                                           itemPerPage = paginate.itemPerPage)


        else:
            response = redirect("/signout/")
    elif request.method == 'POST' and app.token!=None:
        if request.form['btn'] == 'search':
            search_text = request.form["search_text"]
            if search_text == "":
                response = redirect("/home/")
            else:
                index_search = "/home/search_text=" + search_text
                response = redirect(index_search)
#                        if validation == "":
#                            response = redirect(index_search)
#                        elif validation == "valid":
#                            response = redirect(index_search+"_validation=valid")
#                        elif validation == "invalid":
#                            response = redirect(index_search+"_validation=invalid")
#                        elif validation == "coming":
#                            response = redirect(index_search+"_validation=coming")
#
#                elif request.form['btn'].startswith("delete"):
#                    if s == "":
#                        s = request.form['btn'].split("_")[1]+";"
#                        response = redirect("/campain/delete="+s)
#
#                    else:
#                        response = redirect("/campain/delete="+s)
#
#                elif request.form['btn'].startswith("exportCSV"):
#                    if s == "":
#                        s = request.form['btn'].split("_")[1]+";"
#                        response = redirect("/campain/exportCSV="+s)
#
#                    else:
#                        response = redirect("/campain/exportCSV="+s)
#
#                elif request.form['btn'].startswith("compare"):
#                    if s == "":
#                        s = request.form['btn'].split("_")[1]+";"
#                        response = redirect("/campain/stats="+s)
#
#                    else:
#                        response = redirect("/campain/stats="+s)
#
#                else:
#                    response = redirect("/signout/")
#
#            elif "btnShowValid" in request.form:
#                if search_text == "":
#                    response = redirect("/home/validation=valid")
#                else:
#                    response = redirect("/home/search_text="+search_text+"_validation=valid")
#
#            elif "btnShowinValid" in request.form:
#                if search_text == "":
#                    response = redirect("/home/validation=invalid")
#                else:
#                    response = redirect("/home/search_text="+search_text+"_validation=invalid")
#
#            elif "btnShowComing" in request.form:
#                if search_text == "":
#                    response = redirect("/home/validation=coming")
#                else:
#                    response = redirect("/home/search_text="+search_text+"_validation=coming")
#
#            else:
#                if search_text == "":
#                    response = redirect("/home/")
#                else:
#                    response = redirect("/home/search_text="+search_text)
#        response = redirect("/home/")
    else:
        response = redirect("/")
    return response

@app.route('/product/add', methods=['GET', 'POST'])
def add_Product():
    logged, response = login_campain.login_test(session_manager)
    cat_manager = CategoryManager()
    first_category_list = cat_manager.get_first_category_list()
    if request.method == 'GET':
        if logged:
            first_category = {}
            user = user_manager.get_user_by_ID(int(session_manager.get_session_user_id()))
            response = render_template("add_product.html", user=user, category_list=first_category_list, display="none")
    else:
        if logged:
            fields = {}
            fields["ean13"] = str(request.form['ean13'])
            fields["product_name"] = str(request.form['product_name'])
            fields["trade_mark"] = str(request.form['trade_mark'])
            fields["price"] = str(request.form['price'])
            fields["description"] = str(request.form['description'])
            fields["rayon"] = str(request.form['rayon'])
            fields["mdd"] = str(request.form['mdd'])
            fields["category_id"] = str(request.form['category_id'])

            user = user_manager.get_user_by_ID(int(session_manager.get_session_user_id()))

            Errors = {}

            if "btn" in request.form:

                if "check" in request.form:
                    if "file_trademark" in request.files:
                        file_video_trademark = request.files['file_trademark']
                    if "file_demo" in request.files:
                        file_video_demo = request.files['file_trademark']
                    if "file_image" in request.files:
                        file_image = request.files['file_image']

            else:
                category_list = cat_manager.get_category_list_by_id(int(fields["category_id"]))
                response = render_template("add_product.html", user=user, category_list=category_list, display="none")

#
#            validatefields = ValidateFields(fields)
#            Errors = validatefields.Validate()
#
#            if len(Errors) == 0:
#                Errors = crud.bind(fields["ean13"],
#                                   Errors,
#                                   fields["old_price"],
#                                   fields["new_price"],
#                                   fields["description"],
#                                   fields["begin_date"],
#                                   fields["end_date"],
#                                   fields["Path"])
#
#                if len(Errors) == 0:
#                    response = redirect("/")
#                else:
#                    response = render_template("add.html",
#                                               Errors=Errors,
#                                               user=user,
#                                               fields=fields,
#                                               display="")
#            else:
#                print Errors
#                response = render_template("add.html",
#                                           Errors=Errors,
#                                           user=user,
#                                           fields=fields,
#                                           display="")

    return response


@app.route('/campain/add/ean13', methods=['GET', 'POST'])
def detect_ean13():
    logged, response = login_campain.login_test(session_manager)
    if request.method == 'GET':
        if logged:
            user = user_manager.get_user_by_ID(int(session_manager.get_session_user_id()))
            response = render_template("ean13_add.html", user=user, display="none")
    else:
        if logged:
            fields = {}
            fields["ean13"] = str(request.form['ean13'])
            user = user_manager.get_user_by_ID(int(session_manager.get_session_user_id()))

            Errors = {}
            ean13 = fields["ean13"]
            validatefields = ValidateFields(fields)
            Errors = validatefields.Validate()

            if len(Errors) == 0:
                Errors = crud.valid_ean13(ean13)

                if len(Errors) == 0:
                    Errors = crud.valid_not_exist(ean13)

                    if len(Errors) == 0:
                        response = redirect("/campain/add/ean13="+fields["ean13"])

                    else:
                        response = render_template("ean13_add.html",
                                                   Errors=Errors,
                                                   user=user,
                                                   ean13=ean13,
                                                   style="",
                                                   fields=fields)
                else:
                    response = render_template("ean13_add.html",
                                               Errors=Errors,
                                               user=user,
                                               ean13=ean13,
                                               style="none",
                                               fields=fields)
                
            else:
                response = render_template("ean13_add.html",
                                           Errors=Errors,
                                           user=user,
                                           ean13=ean13,
                                           style="none",
                                           fields=fields)

    return response


@app.route('/campain/add/ean13=<ean13>', methods=['GET', 'POST'])
def add_Campain(ean13):
    logged, response = login_campain.login_test(session_manager)
    price = str(crud.get_price_by_ean13(ean13))
    if request.method == 'GET':
        if logged:
            user = user_manager.get_user_by_ID(int(session_manager.get_session_user_id()))
            response = render_template("add.html", user=user, ean13=ean13, price=price, display="none")
    else:
        if logged:
            fields = {}
            fields["ean13"] = ean13
            fields["begin_date"] = str(request.form['begin_date'])
            fields["old_price"] = price
            fields["new_price"] = str(request.form['new_price'])
            fields["description"] = str(request.form['description'])
            fields["end_date"] = str(request.form['end_date'])

            user = user_manager.get_user_by_ID(int(session_manager.get_session_user_id()))

            Errors = {}

            if "check" in request.form:
                if "file" in request.files:
                    file = request.files['file']
                    fields["Path"] = file
                    fields["NoPath"] = False
                else:
                    fields["Path"] = ""
                    fields["NoPath"] = True
            else:
                fields["Path"] = ""
                fields["NoPath"] = True

            validatefields = ValidateFields(fields)
            Errors = validatefields.Validate()

            if len(Errors) == 0:
                Errors = crud.bind(fields["ean13"],
                                   Errors,
                                   fields["old_price"],
                                   fields["new_price"],
                                   fields["description"],
                                   fields["begin_date"],
                                   fields["end_date"],
                                   fields["Path"])

                if len(Errors) == 0:
                    response = redirect("/")
                else:
                    response = render_template("add.html",
                                               Errors=Errors,
                                               user=user,
                                               ean13=ean13, 
                                               price=price, 
                                               fields=fields,
                                               display="")
            else:
                response = render_template("add.html",
                                           Errors=Errors,
                                           user=user,
                                           ean13=ean13, 
                                           price=price, 
                                           fields=fields,
                                           display="")

    return response





@app.route('/recharge/', methods=['GET', 'POST'])
def recharge_cartes():
    if request.method == 'GET':
        pass
    else:
        pass

    return response
