from src.config import *
from src.refund import *


def get_next_id():
    max_id = cursor.execute("SELECT MAX(ID) FROM Refunds").fetchone()
    if max_id is None:
        return 1
    else:
        return max_id + 1


def add_to_db(refund):
    gap_items = refund.items
    while len(gap_items) < 50:
        gap_items.append("")
    item_string = ""
    for i in range(1,51):
        item_string += ', :Item_' + str(i)
    cursor.execute("INSERT INTO Refunds VALUES (:ID, :Reason" + item_string + ")",
                   {'ID': refund.t_id, 'Reason': refund.reason,
                    'Item_1': gap_items[0], 'Item_2': gap_items[1], 'Item_3': gap_items[2],
                    'Item_4': gap_items[3], 'Item_5': gap_items[4], 'Item_6': gap_items[5],
                    'Item_7': gap_items[6], 'Item_8': gap_items[7], 'Item_9': gap_items[8],
                    'Item_10': gap_items[9], 'Item_11': gap_items[10], 'Item_12': gap_items[11],
                    'Item_13': gap_items[12], 'Item_14': gap_items[13], 'Item_15': gap_items[14],
                    'Item_16': gap_items[15], 'Item_17': gap_items[16], 'Item_18': gap_items[17],
                    'Item_19': gap_items[18], 'Item_20': gap_items[19], 'Item_21': gap_items[20],
                    'Item_22': gap_items[21], 'Item_23': gap_items[22], 'Item_24': gap_items[23],
                    'Item_25': gap_items[24], 'Item_26': gap_items[25], 'Item_27': gap_items[26],
                    'Item_28': gap_items[27], 'Item_29': gap_items[28], 'Item_30': gap_items[29],
                    'Item_31': gap_items[30], 'Item_32': gap_items[31], 'Item_33': gap_items[32],
                    'Item_34': gap_items[33], 'Item_35': gap_items[34], 'Item_36': gap_items[35],
                    'Item_37': gap_items[36], 'Item_38': gap_items[37], 'Item_39': gap_items[38],
                    'Item_40': gap_items[39], 'Item_41': gap_items[40], 'Item_42': gap_items[41],
                    'Item_43': gap_items[42], 'Item_44': gap_items[43], 'Item_45': gap_items[44],
                    'Item_46': gap_items[45], 'Item_47': gap_items[46], 'Item_48': gap_items[47],
                    'Item_49': gap_items[48], 'Item_50': gap_items[49]})
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
