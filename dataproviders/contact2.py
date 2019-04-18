# 需要预先导入的联系人数据
PRESET_CONTACTS = [
    ('给个红包1', '13800138000'),
    ('给个红包2', '13800138001'),
    ('给个红包3', '13800138002'),
    ('给个红包4', '13800138003'),
    ('给个红包5茻', '13800138004'),
    ('大佬1', '13800138005'),
    ('大佬2', '13800138006'),
    ('大佬3', '13800138007'),
    ('大佬4', '13800138008'),
    ('大佬10', '13800138010'),
    ('大佬5', '13800138009'),
    ('大佬6', '13800138011'),
    ('大佬7', '13800138012'),
    ('香港大佬', '67656003'),
    ('xili','13410669632'),
    ('xili', '13410669625'),
    ('xili', '13410669616'),
    ('xihua', '13410669616'),
    ('xika','+8613410559655'),
    ('xiaowen','+85213410559644'),
    ('aaaaaaaaaaaaaaaaaaaa','13410559633'),
('wa ss', '075528233375'),
('waas ss', '67656022'),
('1-a', '67656004'),
('1-a子', '67652004'),
('1-ab', '67656009'),
('1-a子月', '67658009'),
    ('b测算', '13800138111'),
    ('c平5', '13800138222'),
]

# 需要预先导入的群聊数据
PRESET_GROUP_CHATS = [
    ('给个红包1', ['给个红包1', '给个红包2']),
    ('给个红包2', ['给个红包1', '给个红包2']),
    ('给个红包3', ['给个红包1', '给个红包2']),
    ('给个红包4', ['给个红包1', '给个红包2']),
    ('群聊1', ['给个红包1', '给个红包2']),
    ('群聊2', ['给个红包1', '给个红包2']),
    ('群聊3', ['给个红包1', '给个红包2']),
    ('群聊4', ['给个红包1', '给个红包2']),
]


def get_preset_contacts():
    """
    需要预存的联系人数据
    """
    return PRESET_CONTACTS


def get_preset_group_chats():
    """
    需要预先导入的群聊数据
    """
    return PRESET_GROUP_CHATS


def push_resource_dir_to_mobile_sdcard(dist_mobile):
    from settings import RESOURCE_FILE_PATH
    push_to = '/sdcard'
    dist_mobile.push_folder(RESOURCE_FILE_PATH, push_to)
