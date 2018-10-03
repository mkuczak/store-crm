from src.config import *
from src.refund import *


def get_next_id():
    max_id = cursor.execute("SELECT MAX(ID) FROM Refunds").fetchone()
    if max_id is None:
        return 1
    else:
        return max_id + 1


def add_to_db(refund):
    item_string = ""
    for i in range(1,51):
        item_string += ', :Item_' + str(i)
    cursor.execute("INSERT INTO Items VALUES (:ID, :Reason" + item_string + ")",
                   {'ID': refund.t_id, 'Reason': refund.reason,
                    'Item_1': refund.item[0], 'Item_2': refund.item[1], 'Item_3': refund.item[3],
                    'Item_4': refund.item[3], 'Item_5': refund.item[4], 'Item_6': refund.item[5],
                    'Item_7': refund.item[6], 'Item_8': refund.item[7], 'Item_9': refund.item[8],
                    'Item_10': refund.item[9], 'Item_11': refund.item[10], 'Item_12': refund.item[11],
                    'Item_13': refund.item[12], 'Item_14': refund.item[13], 'Item_15': refund.item[14],
                    'Item_16': refund.item[15], 'Item_17': refund.item[16], 'Item_18': refund.item[17],
                    'Item_19': refund.item[18], 'Item_20': refund.item[19], 'Item_21': refund.item[20],
                    'Item_22': refund.item[21], 'Item_23': refund.item[22], 'Item_24': refund.item[23],
                    'Item_25': refund.item[24], 'Item_26': refund.item[25], 'Item_27': refund.item[26],
                    'Item_28': refund.item[27], 'Item_29': refund.item[28], 'Item_30': refund.item[29],
                    'Item_31': refund.item[30], 'Item_32': refund.item[31], 'Item_33': refund.item[32],
                    'Item_34': refund.item[33], 'Item_35': refund.item[34], 'Item_36': refund.item[35],
                    'Item_37': refund.item[36], 'Item_38': refund.item[37], 'Item_39': refund.item[38],
                    'Item_40': refund.item[39], 'Item_41': refund.item[40], 'Item_42': refund.item[41],
                    'Item_43': refund.item[42], 'Item_44': refund.item[43], 'Item_45': refund.item[44],
                    'Item_46': refund.item[45], 'Item_47': refund.item[46], 'Item_48': refund.item[47],
                    'Item_49': refund.item[48], 'Item_50': refund.item[49]})
    connector.commit()


def get_reason(tid):
    try:
        return cursor.execute("SELECT Reason FROM Refunds WHERE ID=?", str(tid)).fetchone()[0]
    except TypeError:
        return None


def get_items(tid):
    items = []
    row = cursor.execute("SELECT * FROM Refunds WHERE ID=?", str(tid)).fetchone()
    if row is None:
        return None
    for i in range(4, 54):
        item = row[i]
        if item != "":
            items.append(item)
        else:
            break
    return items


def extract_from_db(tid):
    if cursor.execute("SELECT * FROM Refunds WHERE ID = ?", str(tid)).fetchone() is None:
        raise ValueError
    else:
        return Refund(tid, get_items(tid), get_reason(tid))


def remove_from_db(tid):
    cursor.execute("DELETE * FROM Refunds WHERE ID = ?", tid)
    connector.commit()
