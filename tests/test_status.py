import asyncio
import json

from nsecpy import regions
from nsecpy.status import Status


STATUS_STRING = """{"lang":"en_US","categories":[{"name":"Wii U","type":0},{"name":"nintendo 3DS","type":0},{"name":"Wii","type":0},{"name":"nintendo DS","type":0},{"name":"web","type":0},{"name":"other","type":0},{"name":"iOS","type":0},{"name":"Nintendo Switch","type":0},{"name":"Android","type":0}],"operational_statuses":[],"temporary_maintenances":[{"platform":["Nintendo Switch"],"platform_image":["img/label_switch.png"],"software_title":"Online play of some software","message":"Server maintenance has been completed. Thank you for your cooperation.","free_write":"","begin":"Wednesday, February 24, 2021  6 :55 AM","end":"Wednesday, February 24, 2021  7 :01 AM","utc_del_time":"2021-02-25 15:01:00","event_status":"3","services":["certain network services"],"update_date":"Wednesday, February 24, 2021"},{"platform":["Nintendo Switch"],"platform_image":["img/label_switch.png"],"software_title":"Splatoon 2","message":"Server maintenance has been completed. Thank you for your cooperation.","free_write":"","begin":"Tuesday, February 23, 2021  4 :55 PM","end":"Tuesday, February 23, 2021  5 :21 PM","utc_del_time":"2021-02-25 01:21:00","event_status":"3","update_date":"Tuesday, February 23, 2021"},{"platform":["Nintendo Switch"],"platform_image":["img/label_switch.png"],"software_title":"Online play of some software","message":"Server maintenance has been completed. Thank you for your cooperation.","free_write":"","begin":"Tuesday, February 23, 2021  4 :55 PM","end":"Tuesday, February 23, 2021  5 :01 PM","utc_del_time":"2021-02-25 01:01:00","event_status":"3","services":["certain network services"],"update_date":"Tuesday, February 23, 2021"},{"platform":["Nintendo Switch"],"platform_image":["img/label_switch.png"],"software_title":"Posting to social networks","message":"During the maintenance window, network services may be unavailable.","free_write":"","begin":"Wednesday, February 24, 2021  5 :00 PM","end":"Wednesday, February 24, 2021  7 :30 PM","event_status":"0","update_date":"Friday, February 19, 2021"},{"platform":["Nintendo Switch"],"platform_image":["img/label_switch.png"],"software_title":"Network Services","message":"During the maintenance window, network services may be unavailable.","free_write":"","begin":"Wednesday, February 24, 2021  8 :30 PM","end":"Wednesday, February 24, 2021 11 :30 PM","event_status":"0","services":["Notice to friends, etc."],"update_date":"Tuesday, February 23, 2021"}]}"""


def test_status():
    data = json.loads(STATUS_STRING)
    stats = Status(data, regions['en_US'])

    assert len(stats.categories) == 9
