import peewee as pw

from baseModel import BaseModel

#Model for Organisation
class Rating (BaseModel):
    customerName = pw.CharField(primary_key=True, column_name="customerName")
    rating = pw.CharField(column_name="rating")
    comment = pw.CharField(column_name="comment")

    class Meta:
        table_name = ''