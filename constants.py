from enum import Enum

tlgToken = ""
yadiskToken = ""


idChatArchive = 0
adminId = 0

proxy = {'https': ''}

class StatusAddLink(Enum):
    s_start = 0
    s_addTag = 1
    s_addDescription = 2
    s_addLink = 3