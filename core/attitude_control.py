# -*- coding: utf-8 -*-
class AttitudeControl(object):
    """HKデータのAttitudeControl情報を保持するクラス。"""

    HK_SIZE = 384  # byte

    def __init__(self):
        super(AttitudeControl, self).__init__()
        self.systime = "0:0:0.0"
        self.gas_vector = [0.0] * 3
        self.sas_vector = [0.0] * 3
        self.gyro_vector = [0.0] * 3
        self.stt_quaternion = [0.0] * 4
        self.gps_info = [0.0] * 3
        self.utc_time = ""
        self.dcm_inertia_to_body = [0.0] * 9
        self.target_vector = [0.0] * 6
        self.target_omega = [0.0] * 3
        self.output_torque = [0.0] * 3
        self.output_magnetic_moment = [0.0] * 3
        self.target_position = [0.0] * 3
        self.attitude_determine_system = 0
        self.attitude_determine_system_str = ""
        self.attitude_control_system = 0
        self.attitude_control_system_str = ""
        self.actuator = 0
        self.actuator_str = ""
        self.target_observation = 0
        self.target_observation_str = ""
        self.target_orbit = 0
        self.target_orbit_str = ""

    def __str__(self):
        log = ["Attitude Control SIZE {}[byte]".format(self.HK_SIZE)]
        log += ["systime %s" % self.systime]
        log += ["地磁気ベクトル(機体座標系) {}".format(self.gas_vector)]
        log += ["太陽方向ベクトル(機体座標系) {}".format(self.sas_vector)]
        log += [
            "角速度ベクトル(機体座標系)[deg/s] {}".format(self.gyro_vector)
        ]
        log += ["クォータニオン(機体座標系) {}".format(self.stt_quaternion)]
        log += ["""GPS情報 緯度{0[0]}[度]
                経度{0[1]}[度] 高度{0[2]}[m]""".format(self.gps_info)]
        log += [f"UTC時刻: {self.utc_time}"]
        log += ["""DCM(慣性座標系→機体座標系)
                [{0[0]} {0[1]} {0[2]}]
                [{0[3]} {0[4]} {0[5]}]
                [{0[6]} {0[7]} {0[8]}]""".format(self.dcm_inertia_to_body)]
        log += [
            "目標方向ベクトル(機体座標系) 観測方向 {}".format(
                self.target_vector[:3]
            )
        ]
        log += [
            "目標方向ベクトル(機体座標系) 進行(軌道)方向 {}".format(
                self.target_vector[3:]
            )
        ]
        log += ["""目標角速度ベクトル(機体座標系)
                X{0[0]} Y{0[1]} Z{0[2]}""".format(self.target_omega)]
        log += ["出力トルク {}".format(self.output_torque)]
        log += ["出力磁気モーメント {}".format(self.output_magnetic_moment)]
        log += ["""目標点 緯度{0[0]}[度] 経度{0[1]}[度]
                高度{0[2]}[m]""".format(self.target_position)]
        log += [
            "姿勢決定則 [{}][{}]".format(
                self.attitude_determine_system_str,
                self.attitude_determine_system,
            )
        ]
        log += [
            "姿勢制御則 [{}][{}]".format(
                self.attitude_control_system_str, self.attitude_control_system
            )
        ]
        log += ["出力機器 [{}][{}]".format(self.actuator_str, self.actuator)]
        log += [
            "観測目標方向 [{}][{}]".format(
                self.target_observation_str, self.target_observation
            )
        ]
        log += [
            "軌道(進行)方向 [{}][{}]".format(
                self.target_orbit_str, self.target_orbit
            )
        ]
        return "\n".join(log)

    @staticmethod
    def __create_xyz_elements_dict(elements: list, name: str) -> dict:
        xyz_elements_dict = {}
        for elm, xyz in zip(elements, ["x", "y", "z"]):
            xyz_elements_dict[f"{name}_{xyz}"] = elm
        return xyz_elements_dict

    def get_dict(self) -> dict:
        att_dict = {}
        att_dict["att_systime"] = self.systime
        att_dict.update(
            self.__create_xyz_elements_dict(
                self.gas_vector, "att_magnetic_vector_t"
            )
        )
        att_dict.update(
            self.__create_xyz_elements_dict(self.sas_vector, "att_sun_vector")
        )
        att_dict.update(
            self.__create_xyz_elements_dict(
                self.gyro_vector, "att_angular_velocity_rad_s"
            )
        )
        att_dict.update(
            create_indexed_elements_dict(
                self.stt_quaternion, "att_quaternion_i2b"
            )
        )
        att_dict["att_latitude"] = self.gps_info[0]
        att_dict["att_longitude"] = self.gps_info[1]
        att_dict["att_altitude"] = self.gps_info[2]
        att_dict["att_utc"] = self.utc_time
        att_dict.update(
            create_indexed_elements_dict(
                self.dcm_inertia_to_body, "att_dcm_i2b"
            )
        )
        att_dict["att_observation_vector_x"] = self.target_vector[0]
        att_dict["att_observation_vector_y"] = self.target_vector[1]
        att_dict["att_observation_vector_z"] = self.target_vector[2]
        att_dict["att_constraint_vector_x"] = self.target_vector[3]
        att_dict["att_constraint_vector_y"] = self.target_vector[4]
        att_dict["att_constraint_vector_z"] = self.target_vector[5]
        att_dict.update(
            self.__create_xyz_elements_dict(
                self.target_omega, "att_target_angular_velocity_rad_s"
            )
        )
        att_dict.update(
            self.__create_xyz_elements_dict(
                self.output_torque, "att_output_torque_nmm"
            )
        )
        att_dict.update(
            self.__create_xyz_elements_dict(
                self.output_magnetic_moment, "att_output_magnetic_moment_am2"
            )
        )
        att_dict["att_target_latitude"] = self.target_position[0]
        att_dict["att_target_longitude"] = self.target_position[1]
        att_dict["att_target_altitude"] = self.target_position[2]
        att_dict["att_determination_method"] = (
            self.attitude_determine_system_str
        )
        att_dict["att_control_method"] = self.attitude_control_system_str
        att_dict["att_output_component"] = self.actuator_str
        att_dict["att_observation_target"] = self.target_observation_str
        att_dict["att_constraint_target"] = self.target_orbit_str
        return att_dict
