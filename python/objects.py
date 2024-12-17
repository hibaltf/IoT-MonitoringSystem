class Room:
    def __init__ (self,roomNumber ):
        self.roomNumber=roomNumber

    def roomTemperature(self,temp) : 
        self.temp=temp
        tempval = {
            "minNormalVal" : 19,
            "maxNormalVal" : 24, 
        }
        if((self.temp < tempval["maxNormalVal"])and(self.temp > tempval["minNormalVal"])) : 
            message="Comfort Temperature"
        elif (self.temp > tempval["maxNormalVal"]) : 
            message="Hot, turn on the air conditioner "
        elif (self.temp < tempval["minNormalVal"]) : 
            message="Cold, turn on the air conditioner"
        return  message
        
    def roomHumidity(self,hum) : 
        self.hum=hum
        humval = {
            "minNormalVal" : 30,
            "maxNormalVal" : 60
        }
        if((self.hum < humval["maxNormalVal"])and(self.hum > humval["minNormalVal"])) : 
            message="Comfort Humidity"
        elif (self.hum > humval["maxNormalVal"]) : 
            message="Abnormal Humidity, open the windows"
        elif (self.hum < humval["minNormalVal"]) : 
            message="Humidity under the normal"
        return message



class patient(Room):
    def __init__ (self,namePatient,age,sex,blood,patientCase,roomNumber):
        super().__init__(roomNumber)
        self.namePatient=namePatient
        self.age=age
        self.patientCase=patientCase
        self.sex=sex
        self.blood=blood
    

    def BodyTemperature(self,temp) : 
        self.temp=temp
        tempval = {
            "minNormalVal" : 36,
            "maxNormalVal" : 37.5, 
        }
        if((self.temp < tempval["maxNormalVal"])and(self.temp > tempval["minNormalVal"])) : 
            message="Normal"
        elif (self.temp > tempval["maxNormalVal"]) : 
            message="Abnormal Temp (Hight) "
        elif (self.temp < tempval["minNormalVal"]) : 
            message="Abnormal Temp (Low)"
        return message

    def BodyPosition(self,bodyPos,spesificPos):
        self.bodyPos=bodyPos
        if (self.bodyPos == spesificPos):
            message="Warning! Patient in the wrong position"
        else :
            message="Normal"
        return message



    

    









     


    

    