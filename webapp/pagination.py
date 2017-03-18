#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


class Paginate():

    itemPerPage = 0

    def __init__(self, itemPerPage):
        self.itemPerPage = itemPerPage

    def getListAndPages(self, table, page, search_text):
        MyList = {}
        search_list=[]
        i = 0
        j=0

        if search_text=="":
            for transac in table[self.itemPerPage*(page-1): self.itemPerPage*page]:
                print transac
                MyList[str(transac['id']+j)] = transac
                j=j+1
            i = len(table)
        else:
            stringToSearch = search_text.lower()
            for transac in table:
                if stringToSearch in str(transac[u'Transaction']).lower():
                    search_list.append(transac)
            for transac in search_list[self.itemPerPage*(page-1): self.itemPerPage*page]:
                MyList[str(transac['id']+j)] = transac
                j=j+1
            i = len(MyList)

#            today = datetime.today()
#            session_searched = session.query(tableName).filter(or_(func.lower(tableName.product_name).contains(stringToSearch), func.lower(tableName.trade_mark).contains(stringToSearch)))
#            if validation == "valid":
#                session_searched_valid = session_searched.filter(tableName.begin_date <= today, tableName.end_date > today)
#                i = session_searched_valid.count()
#                for instance in session_searched_valid.slice(self.itemPerPage*(page-1), self.itemPerPage*page):
#                    MyList[str(instance.ean13)] = instance.__dict__
#            elif validation == "invalid":
#                session_searched_invalid = session_searched.filter(tableName.begin_date < today, tableName.end_date < today)
#                i = session_searched_invalid.count()
#                for instance in session_searched_invalid.slice(self.itemPerPage*(page-1), self.itemPerPage*page):
#                    MyList[str(instance.ean13)] = instance.__dict__
#            elif validation == "coming":
#                session_searched_coming = session_searched.filter(tableName.begin_date > today, tableName.end_date > today)
#                i = session_searched_coming.count()
#                for instance in session_searched_coming.slice(self.itemPerPage*(page-1), self.itemPerPage*page):
#                    MyList[str(instance.ean13)] = instance.__dict__


        for key, value in MyList.iteritems():
            MyList[key]["Date"] = self.get_Fr_Format(datetime.strftime(datetime.strptime(MyList[key]["Date"], '%Y-%m-%dT%H:%M:%SZ'), "%d %b %Y - %H:%M"))

        if (i % self.itemPerPage) != 0:
            i = i/self.itemPerPage + 1
        else:
            i = i/self.itemPerPage

        return MyList, i

    def get_En_Format(self, date):

        if date.split()[1] == "Fev":
            date_string = date.replace("Fev", "Feb")
        elif date.split()[1] == "Avr":
            date_string = date.replace("Avr", "Apr")
        elif date.split()[1] == "Mai":
            date_string = date.replace("Mai", "May")
        elif date.split()[1] == "Jui":
            date_string = date.replace("Jui", "Jun")
        elif date.split()[1] == "Aou":
            date_string = date.replace("Aou", "Aug")
        else:
            date_string = date

        return date_string

    def get_Fr_Format(self, date):

        if date.split()[1] == "Feb":
            date_string = date.replace("Feb", "Fev")
        elif date.split()[1] == "Apr":
            date_string = date.replace("Apr", "Avr")
        elif date.split()[1] == "May":
            date_string = date.replace("May", "Mai")
        elif date.split()[1] == "Jun":
            date_string = date.replace("Jun", "Jui")
        elif date.split()[1] == "Aug":
            date_string = date.replace("Aug", "Aou")
        else:
            date_string = date

        return date_string

def __Print__(List):
    for i, j in List.iteritems():
        print i, " : ", j
