from flask_restplus import fields
from src import regions

region_model = regions.model("Add New/Update Region Post Fields", {
    "regionId": fields.Integer("Id of Region."),
    "regionName": fields.String("User Group Code", required=True),
})