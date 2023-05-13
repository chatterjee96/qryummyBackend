
from dbconnection import insertuserdata
from dbconnection import modifyuserdata
from dbconnection import getuserdata
from dbconnection import deleteuserdata
from dbconnection import login
from userInputValidation import userValidation
from dbconnection import selectCuisinegetMenu
from dbconnection import getMenu
from dbconnection import addOrders
from dbconnection import reviewPreviousOrder
from dbconnection import addPayment
from dbconnection import addTip
from dbconnection import addMultipleOrders
from dbconnection import calculateDiscount
from dbconnection import reserveTable
from dbconnection import addMoney
from dbconnection import rating

def lambda_handler(event, context):
    
    # print(event)
    # print(context)

    if event['context']['pathARN'].split("/")[-1] == 'login':
        
        if event['context']['method'] == "POST":

            #print ("LOGIN POST METHOD")

            loginResponse = login (event ['body'])

            if loginResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": loginResponse ['message']
                    }

            else:
                return{
                    "status": "error", 
                    "body": loginResponse ['message']
                    }

        else:
            return {
                'statusCode': 401,
                'body': 'Error in parsing login method'
            }

    elif event['context']['pathARN'].split("/")[-2] == 'usersignin':

        if event['context']['method'] == "GET":

            CustomerID = event['CustomerID']
            #print ("GET METHOD")
            getuserdataResponse = getuserdata (CustomerID)

            if getuserdataResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": getuserdataResponse ['body']
                    }

            else:
                return{
                    "status": "error", 
                    "body": "Error in fetching user details"
                    }

        elif event['context']['method'] == "DELETE":

            CustomerID = event ['CustomerID']
            #print ("DELETE METHOD")
            deleteuserdataResponse = deleteuserdata (CustomerID)


            if deleteuserdataResponse ['status'] == "success":

                return {
                    "status": "success"
                    }

            else:
                return{
                    "status": "error", 
                    "body": "Error in deleting user details"
                    }

        else:
            return {
                'statusCode': 401,
                'body': 'Error in parsing Path ARN'
            }
    
    elif event['context']['pathARN'].split("/")[-1] == 'usersignin':

        if event['context']['method'] == "POST":

            #print ("POST METHOD")

            userValidationResponse= userValidation (event ['body'])

            if userValidationResponse["status"]=="success":

                insertuserdataResponse = insertuserdata (event ['body'])

                if insertuserdataResponse ['status'] == "success":

                    return {
                        "status": "success", 
                        "body": insertuserdataResponse ['message']
                        }

                else:
                    return{
                        "status": "error", 
                        "body": "Error in inserting new user details"
                        }

            else:
                return{
                    "status": "error", 
                    "body": userValidationResponse["message"]
                }

        elif event['context']['method'] == "PUT":

            #print ("PUT METHOD")

            if event['body']['CustomerName'] == '' and event['body']['PhNumber'] == '' and event['body']['email'] == '' and event['body']['password'] == '' and event['body']['CurrentRestaurant']=='':
                
                return {
                        "status": "error", 
                        "body": "No input"
                        }
            
            elif event['body']['CustomerName'] != '' or event['body']['PhNumber'] != '' or event['body']['email'] != '' or event['body']['password'] != '' or event['body']['CurrentRestaurant']!='':

                event1={'body':{}}
                for key,value in event['body'].items():
                    if value != "":
                        event1['body'][key]=value

                event1['body']['CustomerID']=event['body']['CustomerID']

                modifyuserdataResponse = modifyuserdata (event1 ['body'])

                if modifyuserdataResponse ['status'] == "success":

                    return {
                        "status": "success", 
                        "body": modifyuserdataResponse ['body']
                        }

                else:
                    return{
                        "status": "error", 
                        "body": "Error in updating user details while parsing body"
                        }
            
            else:
                    return{
                        "status": "error", 
                        "body": "Error in updating user details"
                        }

        else:
            return {
                'statusCode': 401,
                'body': 'Error in parsing method'
            }

    elif event['context']['pathARN'].split("/")[-2] == 'addtocart':

        if event['context']['method'] == "GET":

            #print ("GET METHOD")
            reviewPreviousOrderResponse = reviewPreviousOrder (event['customerName'])

            if reviewPreviousOrderResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": reviewPreviousOrderResponse ['body']
                    }

            else:
                return{
                    "status": "error", 
                    "body": "Error in fetching last order details"
                    }
            

        else:
            return {
                'statusCode': 401,
                'body': 'Error in parsing method'
            }

        
    elif event['context']['pathARN'].split("/")[-1] == 'addtocart':

        if event['context']['method'] == "POST":

            #print ("POST METHOD")

            addOrdersResponse= addOrders (event["body"])

            if addOrdersResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": addOrdersResponse ['message']
                    }

            else:
                return{
                    "status": "error", 
                    "body": "Error in inserting new orders"
                    }

        else:
            return {
                'statusCode': 401,
                'body': 'Error in parsing method'
            }

    elif event['context']['pathARN'].split("/")[-2] == 'menufetch':

        #For getting cusine list of specific restaurant
        if event['context']['method'] == "GET":

            # print ("GET METHOD")
            # put in API body in cusine: restaurant value
            selectCuisinegetMenuResponse = selectCuisinegetMenu (event['cuisine'])

            if selectCuisinegetMenuResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": selectCuisinegetMenuResponse ['body']
                    }

            else:
                return{
                    "status": "error", 
                    "body": "Error in fetching cuisine details"
                    }
            
    elif event['context']['pathARN'].split("/")[-2] == 'getmenu':

        #For getting menu list of specific restaurant
        if event['context']['method'] == "GET":

            #print ("GET METHOD")
            getMenuResponse = getMenu (event['restaurantName'])

            if getMenuResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": getMenuResponse ['body']
                    }

            else:
                return{
                    "status": "error", 
                    "body": "Error in fetching menu details"
                    }
            
    elif event['context']['pathARN'].split("/")[-1] == 'payment':

        #For getting payment list of specific restaurant
        if event['context']['method'] == "POST":

            # print ("POST METHOD")
            addPaymentResponse = addPayment (event["body"])

            if addPaymentResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": addPaymentResponse ['message']
                    }

            else:
                return {
                    "status": "error", 
                    "body": "Error in fetching payment details"
                    }
    
    elif event['context']['pathARN'].split("/")[-2] == 'payment':

        #For getting tip of specific restaurant
        if event['context']['method'] == "POST":

            #print ("POST METHOD")
            addTipResponse = addTip (event["body"])

            if addTipResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": addTipResponse ['message']
                    }

            else:
                return {
                    "status": "error", 
                    "body": "Error in fetching tip details"
                    }
    
    
    elif event['context']['pathARN'].split("/")[-1] == 'addMultipleOrders':

        #For mulitple order add
        if event['context']['method'] == "POST":

            #print ("POST METHOD")
            addMultipleOrdersResponse = addMultipleOrders (event["body"])

            if addMultipleOrdersResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "body": addMultipleOrdersResponse ['message']
                    }

            else:
                return {
                    "status": "error", 
                    "body": "Error in inserting multiple orders"
                    }
            

    elif event['context']['pathARN'].split("/")[-1] == 'discountCalc':

        #For calculating discount 
        if event['context']['method'] == "POST":

            price = event["body"]["price"]
            customerName = event["body"]["customerName"]
            promoCode = event["body"]["promoCode"]

            #print ("POST METHOD")
            discountCalcResponse = calculateDiscount (price, customerName, promoCode)

            if discountCalcResponse ['status'] == "success":

                return {
                    "status": "success", 
                    "type": discountCalcResponse ['type'],
                    "body": round(discountCalcResponse ['body'], 2)
                    }

            else:
                return {
                    "status": "error", 
                    "body": "Error in fetching discount"
                    }

    elif event['context']['pathARN'].split("/")[-1] == 'reservetable':

        if event['context']['method'] == "POST":

            reserveTableResponse = reserveTable (event["body"])

            if reserveTableResponse ['status'] == "success":

                return reserveTableResponse

            else:
                return {
                    "status": "error", 
                    "body": "Error in fetching reserve table"
                    }
            

    elif event['context']['pathARN'].split("/")[-1] == 'addmoney':

        if event['context']['method'] == "POST":

            addMoneyResponse = addMoney (event["body"])

            if addMoneyResponse ['status'] == "success":

                return addMoneyResponse

            else:
                return {
                    "status": "error", 
                    "body": "Error in adding money table"
                    }
            
    elif event['context']['pathARN'].split("/")[-1] == 'rating':

        if event['context']['method'] == "POST":

            ratingResponse = rating (event["body"])

            if ratingResponse ['status'] == "success":

                return ratingResponse

            else:
                return {
                    "status": "error", 
                    "body": "Error in adding rating table"
                    }
    
    else:

        return {
            'statusCode': 401,
            'body': 'Error in parsing Path ARN'
        }

