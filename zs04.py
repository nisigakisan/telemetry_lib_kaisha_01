#
# 子孫クラスを解決し、MarviHkDataを完全解決する
#

from pprint import pprint

import sys
sys.stdout.reconfigure(encoding="utf-8")


# ルートモジュールは特別扱い
from core import marvi_hk_data

# テレコマLibからはファイル単位で取り込む
list_module = [
    "attitude_control",
    "djm",
    "gps",
    "gyro",
    "mission_controller",
    "obc",
    "pcu",
    "rw",
    "stt",
]


# 上記モジュールをimport
list_imported_module = []
import importlib
for name in list_module:
    globals()[name] = importlib.import_module(f"core.{name}")
    list_imported_module.append(name)

# 上記モジュールに含まれるクラスを取得
list_class_name = []
set_module_name = set()
list_id_module_class = []

import inspect
def build_list_id_module_class():
    for module_name in list_imported_module:
        module = globals()[module_name]
        for class_name, cls_obj in inspect.getmembers(module, inspect.isclass):
            # GpsIndexは例外
            if "GpsIndex" == class_name:
                continue
            # そのモジュールで定義されたクラスだけ抽出
            if cls_obj.__module__ == module.__name__:
                classID = f"{module_name}.{class_name}"
                set_module_name.add(module_name)
                list_class_name.append(class_name)
                outstr = f"{classID}, {module_name}, {class_name}"
                list_id_module_class.append(outstr)


# inst を作って詳しく調べる
class_vs_inst = {}
def build_class_vs_inst():
    for elem in list_id_module_class:
        classID, module_name, class_name = elem.split(", ")
        module = globals()[module_name]
        cls_obj = getattr(module, class_name)

        try:
            inst = cls_obj()
        except TypeError:
            print(f"引数なしでインスタンス化できないクラス：{classID}")
            if classID == "djm.Djm":
                inst = cls_obj(djm_id=1)
            if classID == "djm.I2c":
                inst = cls_obj(unit_type="Voltage")
            if classID == "pcu.I2c":
                inst = cls_obj(unit_type="Voltage")
            if classID == "rw.Rw":
                inst = cls_obj(rw_id=1)
            if classID == "stt.StarInfo":
                inst = cls_obj(star_info_id=1)
            if classID == "stt.Stt":
                inst = cls_obj(stt_id=1)
        class_vs_inst[classID] = inst


list_basic_type = ["str", "int", "float", "NoneType"]

set_member_type = set()

class_vs_list_module_class_member_name_type_len = {}
class_vs_list_module_class_member_name_type_len_flatten = {}
class_vs_list_module_class_member_name_type_len_resolved = {}


# クラスごとにメンバー変数のリストを作る
def build_class_vs_members(inst):
    module_name = f"{type(inst).__module__}"
    module_name = module_name.replace("core.","")
    class_name = f"{type(inst).__name__}"
    classID = f"{module_name}.{class_name}"
    class_vs_list_module_class_member_name_type_len[classID] = []

    for member_name, member_value in vars(inst).items():
        member_type = type(member_value).__name__
        if isinstance(member_value, list):
            member_type = type(member_value[0]).__name__
        set_member_type.add(member_type)

        length = 1
        if isinstance(member_value, list):
            length = len(member_value)

        outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
        class_vs_list_module_class_member_name_type_len[classID].append(outstr)

# クラスごとにメンバー変数のリストをflattenする
def flatten_class_vs_members():
    for classID,list_module_class_member_name_type_len in class_vs_list_module_class_member_name_type_len.items():
        class_vs_list_module_class_member_name_type_len_flatten[classID] = []

        for elem in list_module_class_member_name_type_len:
            module_name, class_name, member_name, member_type, length = elem.split(", ")
            length = int(length)

            if length > 1:
                for i in range(length):
                    outstr = f"{module_name}, {class_name}, {member_name}.{i+1}, {member_type}, 1"
                    class_vs_list_module_class_member_name_type_len_flatten[classID].append(outstr)
            else:
                outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, 1"
                class_vs_list_module_class_member_name_type_len_flatten[classID].append(outstr)

# クラスinクラスの完全解決（モジュール-クラス-メンバー型-長さ を出力）
def full_resolve_class_vs_members():
    for classID, list_module_class_member_name_type_len_flatten in class_vs_list_module_class_member_name_type_len_flatten.items():
        class_vs_list_module_class_member_name_type_len_resolved[classID] = []

        for elem in list_module_class_member_name_type_len_flatten:
            module_name, class_name, member_name, member_type, length = elem.split(", ")

            if member_type in list_basic_type:
                outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}"
                class_vs_list_module_class_member_name_type_len_resolved[classID].append(outstr)
            else:
                outstr = f"解決対象：{module_name}, {class_name}, {member_name}, {member_type}, {length}"
                print(outstr)

                #  Gps, gps_index, GpsIndex のケースの特例
                if member_type == "GpsIndex" and "Gps" == class_name:
                    outstr = f"{module_name}, {class_name}, {member_name}, int, {length}"
                    class_vs_list_module_class_member_name_type_len_resolved[classID].append(outstr)
                    continue

                # Obc, cell_balance_time, list のケースの特例
                if member_type == "list" and "Obc" == class_name:
                    outstr = f"{module_name}, {class_name}, {member_name}, int, {length}"
                    class_vs_list_module_class_member_name_type_len_resolved[classID].append(outstr)
                    continue

                key = f"{module_name}.{member_type}"
                print(f"{member_type} => {key}")
                print(len(class_vs_list_module_class_member_name_type_len_flatten[key]))
                for elem2 in class_vs_list_module_class_member_name_type_len_flatten[key]:
                    module_name2, class_name2, member_name2, member_type2, length2 = elem2.split(", ")

                    outstr = f"{module_name2}, {class_name2}, {member_name}.{member_name2}, {member_type2}, {length2}"
                    class_vs_list_module_class_member_name_type_len_resolved[classID].append(outstr)

                    if member_type2 not in list_basic_type:
                        print("2階層目でも基本型じゃない：", member_type2)


root_class_vs_list_module_class_member_name_type_len = []
root_class_vs_list_module_class_member_name_type_len_flatten = []
root_class_vs_list_module_class_member_name_type_len_resolved = []

# ルートモジュールもメンバー変数のリストを作る
def build_root_class_vs_members(inst):
    module_name = f"{type(inst).__module__}"
    module_name = module_name.replace("core.","")
    class_name = f"{type(inst).__name__}"

    for member_name, member_value in vars(inst).items():
        member_type = type(member_value)
        member_type_s = type(member_value).__name__
        if isinstance(member_value, list):
            member_type = type(member_value[0])
            member_type_s = type(member_value[0]).__name__

        length = 1
        if isinstance(member_value, list):
            length = len(member_value)

        member_type = f"{member_type.__module__}.{member_type.__name__}"
        resolve_key = member_type.replace("core.","")

        outstr = f"{module_name}, {class_name}, {member_name}, {member_type_s}, {length}, {resolve_key}"
        root_class_vs_list_module_class_member_name_type_len.append(outstr)

# ルートモジュールをflattenする
def flatten_root_class_vs_members():
    for elem in root_class_vs_list_module_class_member_name_type_len:
        module_name, class_name, member_name, member_type, length, resolve_key = elem.split(", ")
        length = int(length)

        if length > 1:
            for i in range(length):
                outstr = f"{module_name}, {class_name}, {member_name}.{i+1}, {member_type}, 1, {resolve_key}"
                root_class_vs_list_module_class_member_name_type_len_flatten.append(outstr)
        else:
                outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, 1, {resolve_key}"
                root_class_vs_list_module_class_member_name_type_len_flatten.append(outstr)

# ルートモジュールを完全解決する
def full_resolve_root_class_vs_members():
    for elem in root_class_vs_list_module_class_member_name_type_len_flatten:
        module_name, class_name, member_name, member_type, length, resolve_key = elem.split(", ")

        if member_type in list_basic_type:
            outstr = f"{module_name}, {class_name}, {member_name}, {member_type}, {length}, {resolve_key}"
            root_class_vs_list_module_class_member_name_type_len_resolved.append(outstr)
        else:
            print(f"解決対象：{elem}")
            print(f"{member_type} => {resolve_key}")
            print(len(class_vs_list_module_class_member_name_type_len_resolved[resolve_key]))

            for elem2 in class_vs_list_module_class_member_name_type_len_resolved[resolve_key]:
                module_name2, class_name2, member_name2, member_type2, length2 = elem2.split(", ")

                outstr = f"{module_name2}, {class_name2}, {member_name}.{member_name2}, {member_type2}, {length2}"
                root_class_vs_list_module_class_member_name_type_len_resolved.append(outstr)

                if member_type2 not in list_basic_type:
                    print("2階層目でも基本型じゃない：", member_type2)


# ファイルへ書き出し
def write_list_to_file(filename, list_data):
    with open(filename, "w", encoding="utf-8") as f:
        for item in list_data:
            f.write(f"{item}\n")

#========== ========== ========== ========== ==========
# ここからmain
#========== ========== ========== ========== ==========
PATHNAME = "analized\\"
FILENAME_1 = "1.set_module_name.txt"
FILENAME_2 = "2.list_class_name.txt"
FILENAME_3 = "3.list_id_module_class.txt"
FILENAME_4 = "4.inst.txt"
FILENAME_5 = "5.メンバーの型一覧.txt"
FILENAME_6 = "6.list_module_class_member_name_type_len.txt"
FILENAME_7 = "7.list_module_class_member_name_type_len_flatten.txt"
FILENAME_8 = "8.list_module_class_member_name_type_len_resolved.txt"
FILENAME_9 = "9.root_module_class_member_name_type_len.txt"
FILENAME_A = "A.root_module_class_member_name_type_len_flatten.txt"
FILENAME_B = "B.root_module_class_member_name_type_len_resolved.txt"

# 上記モジュールに含まれるクラスを取得
build_list_id_module_class()
write_list_to_file(PATHNAME+FILENAME_1, sorted(set_module_name))
write_list_to_file(PATHNAME+FILENAME_2, sorted(list_class_name))
write_list_to_file(PATHNAME+FILENAME_3, sorted(list_id_module_class))

# inst を作って詳しく調べる
build_class_vs_inst()
f = open(PATHNAME+FILENAME_4,"w",encoding="utf8")
for classID,inst in class_vs_inst.items():
    print(f"☆{classID}", file=f)
    print(inst, file=f)
    print(file=f)
f.close()

# クラスごとにメンバー変数のリストを作る
for classID,inst in class_vs_inst.items():
    build_class_vs_members(inst)
write_list_to_file(PATHNAME+FILENAME_5, sorted(set_member_type))
f = open(PATHNAME+FILENAME_6,"w",encoding="utf8")
for classID,elem in class_vs_list_module_class_member_name_type_len.items():
    pprint(elem, stream=f)
f.close()

# クラスごとにメンバー変数のリストをflattenする
flatten_class_vs_members()
f = open(PATHNAME+FILENAME_7,"w",encoding="utf8")
for classID,elem in class_vs_list_module_class_member_name_type_len_flatten.items():
    print(f"☆{classID}", file=f)
    pprint(elem, stream=f)
    print(file=f)
f.close()

# クラスinクラスの完全解決（モジュール-クラス-メンバー型-長さ を出力）
full_resolve_class_vs_members()
f = open(PATHNAME+FILENAME_8,"w",encoding="utf8")
for classID,elem in class_vs_list_module_class_member_name_type_len_resolved.items():
    print(f"☆{classID}", file=f)
    pprint(elem, stream=f)
    print(file=f)
f.close()

# ルートモジュールもメンバー変数のリストを作る
inst_root = marvi_hk_data.MarviHkData()
build_root_class_vs_members(inst_root)
f = open(PATHNAME+FILENAME_9,"w",encoding="utf8")
for elem in root_class_vs_list_module_class_member_name_type_len:
    print(elem, file=f)
f.close()

# ルートモジュールをflattenする
flatten_root_class_vs_members()
f = open(PATHNAME+FILENAME_A,"w",encoding="utf8")
for elem in root_class_vs_list_module_class_member_name_type_len_flatten:
    print(elem, file=f)
f.close()

# ルートモジュールを完全解決する
full_resolve_root_class_vs_members()
f = open(PATHNAME+FILENAME_B,"w",encoding="utf8")
for elem in root_class_vs_list_module_class_member_name_type_len_resolved:
    print(elem, file=f)
f.close()

# 以下実験
# for member_name, member_value in vars(inst_root).items():
#     member_type = type(member_value)
#     if isinstance(member_value, list):
#         member_type = type(member_value[0])
#     member_type = f"{member_type.__module__}.{member_type.__name__}"
#     member_type = member_type.replace("core.","")
#     print(f"{member_name},{member_type},{type(member_type)}")
