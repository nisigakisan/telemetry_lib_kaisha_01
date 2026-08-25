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

# importしたもの
modules = [
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

# 型の種類を調査
set_value_type = set()
list_basic_type = ["str","int","NoneType","float"]
list_class = []
class_vs_member_type = {}
class_vs_member_name = {}


# importしたモジュールに含まれるclassの名前を取得
def list_classnames_in_module():
    for module in modules:
        for name, class_object in inspect.getmembers(module, inspect.isclass):
            if class_object.__module__ == module.__name__:
                print(f"{module.__name__}, {name}")


def print_inst(inst):
    name_module = f"{type(inst).__module__}"
    name_class = f"{type(inst).__name__}"

    list_class.append(name_class)
    class_vs_member_type[name_class] = []
    class_vs_member_name[name_class] = []
    # print(f"☆instのモジュール名・クラス名：{name_module_and_class}")

    # print("＝＝print_inst(inst)ここから＝＝")
    # print(inst)
    # print("＝＝print_inst(inst)ここまで＝＝")
    # return

    # print("＝＝メンバー一覧ここから＝＝")
    for member_name, value in vars(inst).items():
        outstr = ""
        value_type = type(value).__name__
        if isinstance(value, list):
            value_type = type(value[0]).__name__

        set_value_type.add(value_type)

        outstr += f"{name_module}, {name_class}, {member_name}, {value_type}"
        if isinstance(value, list):
            outstr += f", {len(value)}"
        else:
            outstr += f", 1"
        class_vs_member_type[name_class].append(value_type)
        class_vs_member_name[name_class].append(member_name)
        print(outstr)
    # print("＝＝メンバー一覧ここまで＝＝")


def create_instance_and_inspect():
    # djm_id: int を引数に取る
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

#==== ここからmain ====

# importしたモジュールに含まれるclassの名前を取得
# list_classnames_in_module()

# inst作って__str__呼ぶ
create_instance_and_inspect()

print()
print("＝＝値の型一覧ここから＝＝")
for value_type in set_value_type:
    print(f"{value_type}")
print("＝＝値の型一覧ここまで＝＝")

print()
print("＝＝クラス名のメンバーが基本型かクラスかここから＝＝")
list_class_basic_only = []
list_class_has_class = []
for class_name in list_class:
    print(class_name)

    flag = True
    for member_type_1 in class_vs_member_type[class_name]:
        if member_type_1 not in list_basic_type:
            print("\t", member_type_1)
            flag = False

    if flag:
        print("基本型だけ")
        list_class_basic_only.append(class_name)
    else:
        print("基本型だけじゃない")
        list_class_has_class.append(class_name)
print("＝＝クラス名のメンバーが基本型かクラスかここまで＝＝")

print()
print("＝＝クラス名のメンバーが基本型だけ ここから＝＝")
for class_name in list_class_basic_only:
    print(class_name)
print("＝＝クラス名のメンバーが基本型だけ ここまで＝＝")

print()
print("＝＝クラス名のメンバーが基本型だけじゃない ここから＝＝")
for class_name in list_class_has_class:
    print(class_name)
print("＝＝クラス名のメンバーが基本型だけじゃない ここまで＝＝")

print()
print("＝＝クラスinクラスの解決 ここから＝＝")
for class_name in list_class_has_class:
    print()
    print("☆" + class_name)
    for i, member_type_1 in enumerate(class_vs_member_type[class_name]):
        member_name_1 = class_vs_member_name[class_name][i]

        if member_type_1  in list_basic_type:
            print(f"{member_name_1}, {member_type_1}")
        else:
            print(f"{member_name_1}, {member_type_1} を解決する")
            if member_type_1 in ["GpsIndex", "list"]:
                print(f"{member_type_1} は解決不能なので深堀しない")
                continue

            for j, member_type_2 in enumerate(class_vs_member_type[member_type_1]):
                member_name_2 = class_vs_member_name[member_type_1][j]
                print(f"{member_name_1}.{member_type_1}.{member_name_2}, {member_type_2}")
                if member_type_2 not in list_basic_type:
                    print("2階層目でも基本型じゃない：", member_type_2)
print("クラスinクラスの解決 ここまで＝＝")
