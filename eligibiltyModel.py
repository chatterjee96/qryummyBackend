import peewee as pw

from baseModel import BaseModel

#Model for Organisation
class Eligibilty (BaseModel):
    Id = pw.CharField(primary_key=True, column_name="Id")
    CustomerName = pw.CharField(column_name="CustomerName")
    FirstTimeUserDeal = pw.CharField(column_name="FirstTimeUserDeal")
    MemberUserDeal = pw.CharField(column_name="MemberUserDeal")
    OccassionalDeal = pw.CharField(column_name="OccassionalDeal")
    MemberUserDealPercent = pw.CharField(column_name="MemberUserDealPercent")
    FirstTimeUserDealPercent = pw.CharField(column_name="FirstTimeUserDealPercent")
    OccassionalDealPercent = pw.CharField(column_name="OccassionalDealPercent")

    class Meta:
        table_name = ''