import peewee as pw

from baseModel import BaseModel

#Model for Organisation
class ReserveTable (BaseModel):
    emailId = pw.CharField(primary_key=True, column_name="emailId")
    NumberOfGuest = pw.CharField(column_name="NumberOfGuest")
    Dates = pw.CharField(column_name="Dates")
    TimePeriod = pw.CharField(column_name="TimePeriod")
    Section = pw.CharField(column_name="Section")

    class Meta:
        table_name = ''