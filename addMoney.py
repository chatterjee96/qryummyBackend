import peewee as pw

from baseModel import BaseModel

#Model for Organisation
class AddMoney (BaseModel):
    customerName = pw.CharField(primary_key=True, column_name="customerName")
    money = pw.CharField(column_name="money")

    class Meta:
        table_name = ''