import peewee as pw

from baseModel import BaseModel

#Model for Organisation
class Payment (BaseModel):
    CardNumber = pw.CharField(primary_key=True, column_name="CardNumber")
    CardHolder = pw.CharField(column_name="CardHolder")
    ExpMonth = pw.CharField(column_name="ExpMonth")
    ExpYear = pw.CharField(column_name="ExpYear")
    CVV = pw.IntegerField(column_name="CVV")
    PaymentStatus = pw.CharField(column_name="PaymentStatus")

    class Meta:
        table_name = ''