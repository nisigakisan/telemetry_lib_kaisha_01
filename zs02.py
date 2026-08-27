#
# テレコマLibからメンバー変数とその名前を抜き出す
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

from core import djm
from core import pcu
from core import gas
from core import gyro
from core import attitude_control
from core import obc
from core import rw
from core import stt
from core import mission_controller

# importしたmoduleのリスト
list_module = [
    djm,
    pcu,
    gas,
    gyro,
    attitude_control,
    obc,
    rw,
    stt,
    mission_controller
]

FILENAME_1 = "1.モジュール名+クラス名.txt"
FILENAME_2 = "2.クラス名.txt"
FILENAME_3 = "3.クラスのメンバーの型.txt"
FILENAME_4 = "4.モジュール-クラス-メンバー型-長さ.txt"
FILENAME_5 = "5.instのlog出力.txt"
FILENAME_6 = "6.クラス-基本型だけ.txt"
FILENAME_7 = "7.クラス-基本型以外.txt"
FILENAME_8 = "8.クラスinクラスの解決.txt"
FILENAME_9 = "9.クラスinクラスの解決(モジュール-クラス-メンバー型-長さ).txt"

list_basic_type = ["str", "int", "float", "NoneType"]

# 型の種類を調査
list_module_class = []
set_class_name = set()
set_member_type = set()
list_module_class_member_name_type_len = []

class_vs_list_member_name = {}
class_vs_list_member_type = {}
class_vs_list_member_length = {}

list_class_basic_only = []
list_class_has_class = []

outstr_inst = ""

# ファイルへ書き出し
def write_list_to_file(filename, list_data):
    with open(filename, "w", encoding="utf-8") as f:
        for item in list_data:
            f.write(f"{item}\n")

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
    inst = gas.Gps()
    print_inst(inst)
    inst = gas.ReceiverStatus()
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

# importしたモジュール, そこに含まれるclassの名前を取得
def build_list_class_name_in_list_module():
    for module in list_module:
        for class_name, class_object in inspect.getmembers(module, inspect.isclass):
            if class_object.__module__ == module.__name__:
                outstr = f"{module.__name__}, {class_name}"
                list_module_class.append(outstr)
                set_class_name.add(class_name)

# inst の__str__を呼ぶ
# inst を作って詳しく調べる
def print_inst(inst):
    module_name = f"{type(inst).__module__}"
    class_name = f"{type(inst).__name__}"
    name_module_and_class = f"{module_name}.{class_name}"

    global outstr_inst
    outstr_inst += f"☆instのモジュール名・クラス名：{name_module_and_class}\n"
    outstr_inst += f"{inst}\n"
    outstr_inst += f"\n"
    
    class_vs_list_member_type[class_name] = []
    class_vs_list_member_name[class_name] = []
    class_vs_list_member_length[class_name] = []

    for member_name, member_value in vars(inst).items():
        member_type = type(member_value).__name__
        if isinstance(member_value, list):
            member_type = type(member_value[0]).__name__
        set_member_type.add(member_type)

        length = 1
        if isinstance(member_value, list):
            length = len(member_value)

        outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
        list_module_class_member_name_type_len.append(outstr)

        class_vs_list_member_name[class_name].append(member_name)
        class_vs_list_member_type[class_name].append(member_type)
        class_vs_list_member_length[class_name].append(length)

# メンバーが基本型だけのクラスと、メンバーにそれ以外を含むクラスに分類
def build_list_class_by_member_type():
    for class_name in class_vs_list_member_type.keys():
        member_types = class_vs_list_member_type[class_name]
        if all(member_type in list_basic_type for member_type in member_types):
            list_class_basic_only.append(class_name)
        else:
            list_class_has_class.append(class_name)

# クラスinクラスの解決
def resolve_class_in_class(f):
    for class_name in list_class_has_class:
        outstr = f"☆メンバーの解決：{class_name}" + "\n"
        for i, member_type_1 in enumerate(class_vs_list_member_type[class_name]):
            member_name_1 = class_vs_list_member_name[class_name][i]

            if member_type_1  in list_basic_type:
                outstr += f"{member_name_1}, {member_type_1}" + "\n"
            else:
                outstr += f"解決対象：{member_name_1}, {member_type_1}" + "\n"

                #  Gps, gps_index, GpsIndex のケースの特例
                if member_type_1 == "GpsIndex" and class_name == "Gps":
                    outstr += f"{member_name_1}, int" + "\n"
                    continue

                # Obc, cell_balance_time, list のケースの特例
                if member_type_1 == "list" and class_name == "Obc":
                    outstr += f"{member_name_1}.1, int" + "\n"
                    outstr += f"{member_name_1}.2, int" + "\n"
                    continue

                for j, member_type_2 in enumerate(class_vs_list_member_type[member_type_1]):
                    member_name_2 = class_vs_list_member_name[member_type_1][j]
                    outstr += f"{member_name_1}.{member_type_1}.{member_name_2}, {member_type_2}" + "\n"

                    if member_type_2 not in list_basic_type:
                        print("2階層目でも基本型じゃない：", member_type_2)
        f.write(outstr)

# クラスinクラスの解決（モジュール-クラス-メンバー型-長さ を出力）
def resolve_class_in_class_full(f):
    for elem in list_module_class_member_name_type_len:
        module_name, class_name, member_name, member_type, length = elem.split(", ")
        outstr = ""

        if member_type in list_basic_type:
            outstr += f"{module_name}, {class_name}, {member_name}, {member_type}, {length}" + "\n"
        else:
            # outstr += f"解決対象：{module_name}, {class_name}, {member_name}, {member_type}, {length}" + "\n"

            #  Gps, gps_index, GpsIndex のケースの特例
            if member_type == "GpsIndex" and class_name == "Gps":
                outstr += f"{module_name}, {class_name}, {member_name}, int, {length}" + "\n"

            # Obc, cell_balance_time, list のケースの特例
            if member_type == "list" and class_name == "Obc":
                outstr += f"{module_name}, {class_name}, {member_name}.1, int, 5" + "\n"
                outstr += f"{module_name}, {class_name}, {member_name}.2, int, 5" + "\n"

            if member_type in class_vs_list_member_type.keys():
                for j, member_type_2 in enumerate(class_vs_list_member_type[member_type]):
                    member_name_2 = class_vs_list_member_name[member_type][j]
                    member_length_2 = class_vs_list_member_length[member_type][j]
                    outstr += f"{module_name}, {class_name}, {member_name}.{member_type}.{member_name_2}, {member_type_2}, {member_length_2}" + "\n"

                    if member_type_2 not in list_basic_type:
                        print("2階層目でも基本型じゃない：", member_type_2)

        f.write(outstr)

#========== ========== ========== ========== ==========
# ここからmain
#========== ========== ========== ========== ==========

# importしたモジュールに含まれるclassの名前を取得
build_list_class_name_in_list_module()
write_list_to_file(FILENAME_1, list_module_class)
write_list_to_file(FILENAME_2, sorted(set_class_name))

# inst を作って詳しく調べる
create_instance_and_inspect()
write_list_to_file(FILENAME_3, sorted(set_member_type))
write_list_to_file(FILENAME_4, list_module_class_member_name_type_len)

# inst の__str__を呼ぶ
with open(FILENAME_5, "w", encoding="utf-8") as f:
    f.write(outstr_inst)

# メンバーが基本型だけのクラスと、メンバーにそれ以外を含むクラスに分類
build_list_class_by_member_type()
write_list_to_file(FILENAME_6, sorted(list_class_basic_only))
write_list_to_file(FILENAME_7, sorted(list_class_has_class))

# クラスinクラスの解決
f = open(FILENAME_8, "w", encoding="utf-8")
resolve_class_in_class(f)
f.close()

# クラスinクラスの解決（モジュール-クラス-メンバー型-長さ を出力）
f = open(FILENAME_9, "w", encoding="utf-8")
resolve_class_in_class_full(f)
f.close()
