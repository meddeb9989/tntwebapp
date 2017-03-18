#!/usr/bin/env python
# -*- coding: utf-8 -*-


from errormessages import ErrorMessages
from werkzeug import secure_filename


class Fileds():

    def Validate(self):
        pass


class Ean13Field(Fileds):

    ean13 = ""
    ErrorsList = []

    def __init__(self, ean13):
        self.ean13 = ean13
        self.ErrorsList = []

    def Validate(self):
        if not self.ean13.isdigit():
            self.ErrorsList.append(
                ErrorMessages.Error_Message_Number_FR)
            if len(self.ean13) != 13:
                if len(self.ean13) > 13:
                    self.ErrorsList.append(
                        ErrorMessages.Error_Message_Length_More_FR)
                elif len(self.ean13) < 13:
                    self.ErrorsList.append(
                        ErrorMessages.Error_Message_Length_Less_FR)
            return False

        elif len(self.ean13) != 13:
            if len(self.ean13) > 13:
                self.ErrorsList.append(
                    ErrorMessages.Error_Message_Length_More_FR)
            elif len(self.ean13) < 13:
                self.ErrorsList.append(
                    ErrorMessages.Error_Message_Length_Less_FR)
            return False
        else:
            return True

    def getErrorsList(self):
        return self.ErrorsList


class DateField(Fileds):

    beginDate = ""
    endDate = ""
    BeginDateErrorsList = []
    EndDateErrorsList = []
    DateErrorsList = []

    def __init__(self, beginDate, endDate):
        self.endDate = endDate
        self.beginDate = beginDate
        self.BeginDateErrorsList = []
        self.EndDateErrorsList = []
        self.DateErrorsList = []

    def Validate(self):
        return True

    def getBeginDateErrorsList(self):
        return self.BeginDateErrorsList

    def getEndDateErrorsList(self):
        return self.EndDateErrorsList

    def getDateErrorsList(self):
        return self.DateErrorsList


class PriceField(Fileds):

    oldPrice = ""
    newPrice = ""
    digitOldPrice = ""
    digitNewPrice = ""
    OldPriceErrorsList = []
    NewPriceErrorsList = []
    PriceErrorsList = []

    def __init__(self, oldPrice, newPrice):
        self.oldPrice = oldPrice
        self.newPrice = newPrice
        self.OldPriceErrorsList = []
        self.NewPriceErrorsList = []
        self.PriceErrorsList = []

    def Validate(self):
        
        if "." in self.oldPrice:
            self.digitOldPrice = self.oldPrice.split(".")[0]+self.oldPrice.split(".")[1]
        elif "," in self.oldPrice:
            self.digitOldPrice = self.oldPrice.split(",")[0]+self.oldPrice.split(",")[1]
        else:
            self.digitOldPrice = self.oldPrice

        if "." in self.newPrice:
            self.digitNewPrice = self.newPrice.split(".")[0]+self.newPrice.split(".")[1]
        elif "," in self.newPrice:
            self.digitNewPrice = self.newPrice.split(",")[0]+self.newPrice.split(",")[1]
        else:
            self.digitNewPrice = self.newPrice

        if not self.digitOldPrice.isdigit():
            self.OldPriceErrorsList.append(
                ErrorMessages.Error_Message_OldPrice_Not_Digits_FR)

            if not self.digitNewPrice.isdigit():
                self.NewPriceErrorsList.append(
                    ErrorMessages.Error_Message_NewPrice_Not_Digits_FR)

            return False

        elif not self.digitNewPrice.isdigit():
            self.NewPriceErrorsList.append(
                 ErrorMessages.Error_Message_NewPrice_Not_Digits_FR)

            return False

        elif (float(self.newPrice)>float(self.oldPrice)):
            self.PriceErrorsList.append(
                ErrorMessages.Error_Message_NewPrice_Bigger_OldPrice_FR)

            return False

        else:
            return True

    def getOldPriceErrorsList(self):
        return self.OldPriceErrorsList

    def getNewPriceErrorsList(self):
        return self.NewPriceErrorsList

    def getPriceErrorsList(self):
        return self.PriceErrorsList


class DescriptionField(Fileds):

    description = ""
    ErrorList = []

    def __init__(self, description):
        self.description = description
        ErrorList = []

    def Validate(self):
        return True

    def getErrorsList(self):
        return self.ErrorList


class PathField(Fileds):

    file = file
    ErrorsList = []
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    NoPath = ""

    def __init__(self, file, NoPath):
        self.file = file
        self.NoPath = NoPath
        self.ErrorsList = []

    def Validate(self):
        if not self.NoPath:
            if self.file.filename != "":
                if self.file.filename.rsplit('.', 1)[1] in self.ALLOWED_EXTENSIONS:
                    return True
                else:
                    self.ErrorsList.append(
                        ErrorMessages.Error_Message_Incorrect_Format_Path_FR)
                    return False
            else:
                self.ErrorsList.append(
                    ErrorMessages.Error_Message_No_Photo_FR)
                return False
        else:
            return True

    def getErrorsList(self):
        return self.ErrorsList

    def setPath(self, file):
        self.file = file
