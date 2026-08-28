#
# 子孫クラスを解決し、MarviHkDataを完全解決する
#


# hk_data.py
# marvi_hk_data.py

# djm.py
# pcu.py
# gas.py
# gyro.py
# attitude_control.py
# obc.py
# rw.py
# stt.py
# mission_controller.py

import inspect
import sys
from pprint import pprint

sys.stdout.reconfigure(encoding="utf-8")

from core import marvi_hk_data

from core import djm
from core import pcu
from core import gps
from core import gyro
from core import attitude_control
from core import obc
from core import rw
from core import stt
from core import mission_controller


FILENAME_A = "A.list_module_class_member_name_type_len_resolved.txt"
FILENAME_B = "B.txt"
FILENAME_C1 = "C.list_marvi_hk_data_resolved_1.txt"
FILENAME_C2 = "C.list_marvi_hk_data_resolved_2.txt"
FILENAME_C3 = "C.list_marvi_hk_data_resolved_3.txt"

list_basic_type = ["str", "int", "float", "NoneType"]

list_module_class_member_name_type_len = []
list_module_class_member_name_type_len_resolved = []

class_vs_list_member_name = {}
class_vs_list_member_type = {}
class_vs_list_member_length = {}
class_vs_list_module_class_member_name_type_len_resolved = {}

# ファイルへ書き出し
def write_list_to_file(filename, list_data):
    with open(filename, "w", encoding="utf-8") as f:
        for item in list_data:
            f.write(f"{item}\n")

# inst を作って詳しく調べる
def create_instance_and_inspect():
    inst = djm.Djm(djm_id=1)
    print_inst(inst)
    inst = djm.I2c(unit_type="Voltage")
    print_inst(inst)
    inst = djm.Sas()
    print_inst(inst)
    inst = pcu.AdData()
    print_inst(inst)
    inst = pcu.Ads7830Pop()
    print_inst(inst)
    inst = pcu.I2c(unit_type="Voltage")
    print_inst(inst)
    inst = pcu.I2cTmp()
    print_inst(inst)
    inst = pcu.Pcu()
    print_inst(inst)
    inst = gps.Gps()
    print_inst(inst)
    inst = gps.ReceiverStatus()
    print_inst(inst)
    inst = gyro.CeIru()
    print_inst(inst)
    inst = gyro.MIru()
    print_inst(inst)
    inst = attitude_control.AttitudeControl()
    print_inst(inst)
    inst = obc.Obc()
    print_inst(inst)
    inst = rw.ErrorInfo()
    print_inst(inst)
    inst = rw.Rw(rw_id=1)
    print_inst(inst)
    inst = rw.Status()
    print_inst(inst)
    inst = stt.StarInfo(star_info_id=1)
    print_inst(inst)
    inst = stt.Stt(stt_id=1)
    print_inst(inst)
    inst = mission_controller.MissionController()
    print_inst(inst)

# list_module_class_member_name_type_len を作る
def print_inst(inst):
    module_name = f"{type(inst).__module__}"
    class_name = f"{type(inst).__name__}"

    class_vs_list_member_type[class_name] = []
    class_vs_list_member_name[class_name] = []
    class_vs_list_member_length[class_name] = []

    for member_name, member_value in vars(inst).items():
        member_type = type(member_value).__name__
        if isinstance(member_value, list):
            member_type = type(member_value[0]).__name__

        length = 1
        if isinstance(member_value, list):
            length = len(member_value)

        outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
        list_module_class_member_name_type_len.append(outstr)

        class_vs_list_member_name[class_name].append(member_name)
        class_vs_list_member_type[class_name].append(member_type)
        class_vs_list_member_length[class_name].append(length)

# クラスinクラスの解決（モジュール-クラス-メンバー型-長さ を出力）
def resolve_class_in_class_full():
    for elem in list_module_class_member_name_type_len:
        module_name, class_name, member_name, member_type, length = elem.split(", ")

        if member_type in list_basic_type:
            outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
            list_module_class_member_name_type_len_resolved.append(outstr)
        else:
            # outstr += f"解決対象：{module_name}, {class_name}, {member_name}, {member_type}, {length}"

            #  Gps, gps_index, GpsIndex のケースの特例
            if member_type == "GpsIndex" and class_name == "Gps":
                outstr = f"{module_name}, {class_name}, {member_name}, int, {length}"
                list_module_class_member_name_type_len_resolved.append(outstr)

            # Obc, cell_balance_time, list のケースの特例
            if member_type == "list" and class_name == "Obc":
                outstr = f"{module_name}, {class_name}, {member_name}.1, int, 5"
                list_module_class_member_name_type_len_resolved.append(outstr)
                outstr = f"{module_name}, {class_name}, {member_name}.2, int, 5"
                list_module_class_member_name_type_len_resolved.append(outstr)

            if member_type in class_vs_list_member_type.keys():
                for j, member_type_2 in enumerate(class_vs_list_member_type[member_type]):
                    member_name_2 = class_vs_list_member_name[member_type][j]
                    member_length_2 = class_vs_list_member_length[member_type][j]
                    outstr = f"{module_name}, {class_name}, {member_name}.{member_type}.{member_name_2}, {member_type_2}, {member_length_2}"
                    list_module_class_member_name_type_len_resolved.append(outstr)

                    if member_type_2 not in list_basic_type:
                        print("2階層目でも基本型じゃない：", member_type_2)

def build_class_vs_list_module_class_member_name_type_len_resolved():
    for elem in list_module_class_member_name_type_len_resolved:
        module_name, class_name, member_name, member_type, length = elem.split(", ")

        if class_name not in class_vs_list_module_class_member_name_type_len_resolved:
            class_vs_list_module_class_member_name_type_len_resolved[class_name] = []

        outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
        class_vs_list_module_class_member_name_type_len_resolved[class_name].append(outstr)

    for class_name, list_data in class_vs_list_module_class_member_name_type_len_resolved.items():
        filename = f"B_{class_name}.txt"
        write_list_to_file(filename, list_data)


#========== ========== ========== ========== ==========
# ここからmain
#========== ========== ========== ========== ==========

# inst を作って詳しく調べる
create_instance_and_inspect()

# クラスinクラスの解決（モジュール-クラス-メンバー型-長さ を出力）
resolve_class_in_class_full()
write_list_to_file(FILENAME_A, list_module_class_member_name_type_len_resolved)

# 解決したリストクラス別に保持する
build_class_vs_list_module_class_member_name_type_len_resolved()

# MarviHkData について inst を作って詳しく調べる
list_marvi_hk_data_resolved_1 = []
list_marvi_hk_data_resolved_2 = []
list_marvi_hk_data_full_resolved = []

inst = marvi_hk_data.MarviHkData()
module_name = f"{type(inst).__module__}"
class_name = f"{type(inst).__name__}"
for member_name, member_value in vars(inst).items():
    member_type = type(member_value).__name__
    if isinstance(member_value, list):
        member_type = type(member_value[0]).__name__

    length = 1
    if isinstance(member_value, list):
        length = len(member_value)

    outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
    list_marvi_hk_data_resolved_1.append(outstr)

    if length > 1:
        for i in range(length):
            outstr = f"{module_name}, {class_name}, {member_name}.{i+1}, {member_type}, 1"
            list_marvi_hk_data_resolved_2.append(outstr)
    else:
        outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
        list_marvi_hk_data_resolved_2.append(outstr)

    # ここからフル解決
    for elem in list_marvi_hk_data_resolved_2:
        module_name, class_name, member_name, member_type, length = elem.split(", ")

        list_module_class_member_name_type_len_resolved \
            = class_vs_list_module_class_member_name_type_len_resolved[member_type]
        for elem2 in list_module_class_member_name_type_len_resolved:
            module_name2, class_name2, member_name2, member_type2, length2 = elem2.split(", ")

            outstr = f"{module_name}, {class_name}, {member_name}.{member_name2}, {member_type2}, {length2}"
            list_marvi_hk_data_full_resolved.append(outstr)

write_list_to_file(FILENAME_C1, list_marvi_hk_data_resolved_1)
write_list_to_file(FILENAME_C2, list_marvi_hk_data_resolved_2)
write_list_to_file(FILENAME_C3, list_marvi_hk_data_full_resolved)
