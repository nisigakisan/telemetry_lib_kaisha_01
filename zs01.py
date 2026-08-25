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

# importしたモジュールに含まれるclassの名前を取得
def list_classnames_in_module():
    for module in modules:
        for name, class_object in inspect.getmembers(module, inspect.isclass):
            if class_object.__module__ == module.__name__:
                print(f"{module.__name__}, {name}")


def print_inst(inst):
    name_module_and_class = f"{type(inst).__module__}.{type(inst).__name__}"
    name_module_and_class = name_module_and_class.replace("core.", "")
    # print(f"☆instのモジュール名・クラス名：{name_module_and_class}")

    # print("＝＝print_inst(inst)ここから＝＝")
    # print(inst)
    # print("＝＝print_inst(inst)ここまで＝＝")

    # print("＝＝メンバー一覧ここから＝＝")
    for name_member, value in vars(inst).items():
        value_type = type(value).__name__
        set_value_type.add(value_type)
        outstr = f"{name_module_and_class}, {name_member}, {value_type}"
        if isinstance(value, list):
            outstr += f", {len(value)}"
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

# ここからmain
# list_classnames_in_module()
create_instance_and_inspect()

print()
print("＝＝値の型一覧ここから＝＝")
for value_type in set_value_type:
    print(f"{value_type}")
print("＝＝値の型一覧ここまで＝＝")
