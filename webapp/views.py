#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from flask import render_template, redirect, request
import sys
import subprocess
import time
from webapp import app
from pagination import Paginate
import requests
from user import User
import json
from requests.auth import HTTPDigestAuth

app.website_url="https://tntwebserver.herokuapp.com/"
app.token=None

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

@app.route('/add_employe/', methods=['GET', 'POST'])
def add_Employe():
    if request.method == 'GET' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]
        if user['valid']:
            username = user['name']
            response = render_template("add_employe.html")
        else:
            response = redirect("/signout/")
    elif request.method == 'POST' and app.token!=None:
      pass
    else:
        response = redirect("/signout/")

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
                if user_type == "Employeur":
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

                elif user_type == "Employe":
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

                url=app.website_url+"card_state/"
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                card_state=json.loads(r.text)[0]['valid']

                paginate = Paginate(5)
                Mylist, pages = paginate.getListAndPages(transactions, page, search_text)

                if pages < page:
                    page = pages

                response = render_template("home.html",
                                           usertype=user['group'],
                                           user=user['name'],
                                           userid=user['id'],
                                           solde=solde,
                                           card_state=card_state,
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
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]

        s = ""
        for key in request.form:
            if key.startswith("checkfor"):
                s += key.split("_")[1]+";"

        if request.form['btn'] == 'search':
            search_text = request.form["search_text"]
            if search_text == "":
                response = redirect("/home/")
            else:
                index_search = "/home/search_text=" + search_text
                response = redirect(index_search)

        elif request.form['btn'] == 'add':
            response = redirect("/add_employe/")
        elif request.form['btn'] == 'bloc':
          if user['valid'] and user['group']==u'Employe':
              url=app.website_url+"bloc_card/"
              r=requests.get(url, headers={'Authorization': 'Token '+app.token})
              response = redirect("/home/")
        elif request.form['btn'] == 'locked':
            if user_type!="":
                response = redirect("/home/user_type="+user_type)
            else:
                response = redirect("/home/")
        elif request.form['btn'].startswith("bloc"):
            if s == "":
                s = request.form['btn'].split("_")[1]+";"
                response = redirect("/confirm_bloc="+s)

            else:
                response = redirect("/confirm_bloc="+s)

        elif request.form['btn'].startswith("recharge"):
            if s == "":
                s = request.form['btn'].split("_")[1]+";"
                response = redirect("/confirm_recharge="+s)

            else:
                response = redirect("/confirm_recharge="+s)
        else:
            if user_type!="":
                response = redirect("/home/user_type="+user_type)
            else:
                response = redirect("/home/")

    else:
        response = redirect("/")
    return response

@app.route('/confirm_bloc=<ids>', methods=['GET', 'POST'])
def confirm_bloc(ids):
    if request.method == 'GET' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]

        if user['valid']:
            deleteList = ids.split(";")
            nameList = []
            if "" in deleteList:
                deleteList.remove("")
            name = ""

            if len(deleteList) == 1:
                url=app.website_url+"get_card/"+str(deleteList[0])
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                card=json.loads(r.text)
                if card[0]['valid']:
                    name = u"La Carte Numéro: "+card[1]['Carte']+u", Propriétaire: "+card[1]['Nom']
                    response = render_template("delete.html",
                                               usertype=user['type'],
                                               user=user['name'],
                                               userid=user['id'],
                                               campainName=name,
                                               campainList=nameList)
                else:
                    response = redirect("/")
            else:
                for ids in deleteList:
                    url=app.website_url+"get_card/"+str(ids)
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                    card=json.loads(r.text)
                    print card
                    if card[0]['valid']:
                        name = u"La Carte Numéro: "+card[1]['Carte']+u", Propriétaire: "+card[1]['Nom']
                        nameList.append(name)

                response = render_template("delete.html",
                                           usertype=user['type'],
                                           user=user['name'],
                                           userid=user['id'],
                                           campainName=name,
                                           campainList=nameList)
                
        else:
            response = redirect("/")

    elif request.method == 'POST' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]

        if user['valid']:
            if request.form['btn'] == "doDelete":
                deleteList = ids.split(";")
                if "" in deleteList:
                    deleteList.remove("")
                if len(deleteList) == 1:
                    url=app.website_url+"bloc_card_id/"+str(deleteList[0])
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                else:
                    for ids in deleteList:
                        url=app.website_url+"bloc_card_id/"+str(ids)
                        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        response = redirect("/home/")
    else:
        response = redirect("/")

    return response



@app.route('/confirm_recharge=<ids>', methods=['GET', 'POST'])
def confirm_recharge(ids):
    if request.method == 'GET' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]
        if user['valid']:
            rechargeList = ids.split(";")
            nameList = []
            if "" in rechargeList:
                rechargeList.remove("")
            name = ""
            if len(rechargeList) == 1:
                url=app.website_url+"get_card/"+str(rechargeList[0])
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                card=json.loads(r.text)

                if card[0]['valid']:
                    name = u"La Carte Numéro: "+card[1]['Carte']+u", Propriétaire: "+card[1]['Nom']
                    response = render_template("ean13_add.html",
                                               usertype=user['type'],
                                               user=user['name'],
                                               userid=user['id'],
                                               campainName=name,
                                               campainList=nameList)
                else:
                    response = redirect("/")
            else:
                for ids in rechargeList:
                    url=app.website_url+"get_card/"+str(ids)
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                    card=json.loads(r.text)
                    print card
                    if card[0]['valid']:
                        name = u"La Carte Numéro: "+card[1]['Carte']+u", Propriétaire: "+card[1]['Nom']
                        nameList.append(name)

                response = render_template("ean13_add.html",
                                           usertype=user['type'],
                                           user=user['name'],
                                           userid=user['id'],
                                           campainName=name,
                                           campainList=nameList)

        else:
            response = redirect("/signout/")
    elif request.method == 'POST' and app.token!=None:
        url=app.website_url+"user/"
        r=requests.get(url, headers={'Authorization': 'Token '+app.token})
        user=json.loads(r.text)[0]

        if user['valid']:
            rechargeList = ids.split(";")
            amount = request.form['amount']
            Errors = []
            if "" in rechargeList:
                rechargeList.remove("")
            if len(rechargeList) == 1:
                url=app.website_url+"recharge_card/"+str(rechargeList[0])+"/"+amount
                r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                card = json.loads(r.text)
                if card[0]['valid']:
                    response = redirect("/home/")
                else:
                    Errors.append(card[0])
                    response = render_template("ean13_add.html",
                                                   Errors=Errors,
                                                   usertype=user['type'],
                                                   user=user['name'],
                                                   userid=user['id'],
                                                   ean13=amount,
                                                   style="")

            else:
                Errors = []
                for ids in rechargeList:
                    url=app.website_url+"recharge_card/"+str(ids)+"/"+amount
                    r=requests.get(url, headers={'Authorization': 'Token '+app.token})
                    card = json.loads(r.text)
                    if card[0]['valid']:
                        pass
                    else:
                        Errors.append(card[0])
                if Errors == []:
                    response = redirect("/home/")
                else:
                    response = render_template("ean13_add.html",
                                                   Errors=Errors,
                                                   usertype=user['type'],
                                                   user=user['name'],
                                                   userid=user['id'],
                                                   ean13=amount,
                                                   style="")
        
    else:
        response = redirect("/")

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
