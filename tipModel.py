import peewee as pw

from baseModel import BaseModel

#Model for Organisation
class Tip (BaseModel):
    OrderNumber = pw.IntegerField(primary_key=True, column_name="OrderNumber")
    TipValue = pw.CharField(column_name="TipValue")

    class Meta:
        table_name = ''