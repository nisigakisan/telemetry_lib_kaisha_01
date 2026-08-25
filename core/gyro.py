# -*- coding: utf-8 -*-
class CeIru(object):
    """HKデータのIRU情報を保持するクラス。"""

    SAMPLING_PERIOD = 10  # Hz
    UNIT_SIZE = 44  # Byte
    HK_SIZE = SAMPLING_PERIOD * UNIT_SIZE

    def __init__(self):
        super(CeIru, self).__init__()
        self.systime = [""] * self.SAMPLING_PERIOD
        self.counter = [0] * self.SAMPLING_PERIOD
        self.gyro_status1 = [0] * self.SAMPLING_PERIOD
        self.gyro_status2 = [0] * self.SAMPLING_PERIOD
        self.iru_status = [0] * self.SAMPLING_PERIOD
        self.err_status = [0] * self.SAMPLING_PERIOD
        self.angular_increment_x = [0] * self.SAMPLING_PERIOD
        self.angular_increment_y = [0] * self.SAMPLING_PERIOD
        self.angular_increment_z1 = [0] * self.SAMPLING_PERIOD
        self.angular_increment_z2 = [0] * self.SAMPLING_PERIOD
        self.gyro_temp1 = [0] * self.SAMPLING_PERIOD
        self.gyro_temp2 = [0] * self.SAMPLING_PERIOD
        self.cpu_temp = [0] * self.SAMPLING_PERIOD
        self.cluster_temp = [0] * self.SAMPLING_PERIOD
        self.gyro1_rotation_vel = [0] * self.SAMPLING_PERIOD
        self.gyro2_rotation_vel = [0] * self.SAMPLING_PERIOD

        self.vx = [0] * self.SAMPLING_PERIOD
        self.vy = [0] * self.SAMPLING_PERIOD
        self.vz1 = [0] * self.SAMPLING_PERIOD
        self.vz2 = [0] * self.SAMPLING_PERIOD

        self.gyro_driver_status = [0] * self.SAMPLING_PERIOD

    def __str__(self):
        log = ["systime %s" % self.systime]
        log += ["counter %s" % self.counter]
        log += ["Gyro1状態 %s" % self.gyro_status1]
        log += ["Gyro2状態 %s" % self.gyro_status2]
        log += ["センサボックス状態 %s" % self.iru_status]
        log += ["エラーステータス %s" % self.err_status]
        log += ["X軸角度増分[deg] %s" % self.angular_increment_x]
        log += ["Y軸角度増分[deg] %s" % self.angular_increment_y]
        log += ["Z1軸角度増分[deg] %s" % self.angular_increment_z1]
        log += ["Z2軸角度増分[deg] %s" % self.angular_increment_z2]
        log += ["Gyro1温度[degC] %s" % self.gyro_temp1]
        log += ["Gyro2温度[degC] %s" % self.gyro_temp2]
        log += ["CPU温度[degC] %s" % self.cpu_temp]
        log += ["Cluster温度 %s" % self.cluster_temp]
        log += ["Gyro1回転速度[rpm] %s" % self.gyro1_rotation_vel]
        log += ["Gyro2回転速度[rpm] %s" % self.gyro2_rotation_vel]
        log += ["X軸角速度[arcsec/s] %s" % self.vx]
        log += ["Y軸角速度[arcsec/s] %s" % self.vy]
        log += ["Z1軸角速度[arcsec/s] %s" % self.vz1]
        log += ["Z2軸角速度[arcsec/s] %s" % self.vz2]
        log += ["ジャイロドライバステータス %s" % self.gyro_driver_status]
        return "\n".join(log)

    def get_dict(self, sampling_index: int) -> dict:
        iru_dict = {}
        iru_dict["ce_iru_systime"] = self.systime[sampling_index]
        iru_dict["ce_iru_count"] = self.counter[sampling_index]
        iru_dict["ce_iru_gyro_1_status"] = self.gyro_status1[sampling_index]
        iru_dict["ce_iru_gyro_2_status"] = self.gyro_status2[sampling_index]
        iru_dict["ce_iru_sensor_box_status"] = self.iru_status[sampling_index]
        iru_dict["ce_iru_error_status"] = self.err_status[sampling_index]
        iru_dict["ce_iru_theta_x_increment"] = self.angular_increment_x[
            sampling_index
        ]
        iru_dict["ce_iru_theta_y_increment"] = self.angular_increment_y[
            sampling_index
        ]
        iru_dict["ce_iru_theta_z_1_increment"] = self.angular_increment_z1[
            sampling_index
        ]
        iru_dict["ce_iru_theta_z_2_increment"] = self.angular_increment_z2[
            sampling_index
        ]
        iru_dict["ce_iru_gyro_1_temperature"] = self.gyro_temp1[sampling_index]
        iru_dict["ce_iru_gyro_2_temperature"] = self.gyro_temp2[sampling_index]
        iru_dict["ce_iru_cpu_temperature"] = self.cpu_temp[sampling_index]
        iru_dict["ce_iru_cluster_temperature"] = self.cluster_temp[
            sampling_index
        ]
        iru_dict["ce_iru_gyro_1_rpm"] = self.gyro1_rotation_vel[sampling_index]
        iru_dict["ce_iru_gyro_2_rpm"] = self.gyro2_rotation_vel[sampling_index]
        iru_dict["ce_iru_angular_velocity_arcsec_s_x"] = self.vx[
            sampling_index
        ]
        iru_dict["ce_iru_angular_velocity_arcsec_s_y"] = self.vy[
            sampling_index
        ]
        iru_dict["ce_iru_angular_velocity_arcsec_s_z_1"] = self.vz1[
            sampling_index
        ]
        iru_dict["ce_iru_angular_velocity_arcsec_s_z_2"] = self.vz2[
            sampling_index
        ]
        return iru_dict


class MIru(object):
    """HKデータのIRU情報を保持するクラス。"""

    SAMPLING_PERIOD = 10  # Hz
    UNIT_SIZE = 48  # Byte
    HK_SIZE = SAMPLING_PERIOD * UNIT_SIZE

    def __init__(self):
        super(MIru, self).__init__()
        self.systime = [""] * self.SAMPLING_PERIOD
        self.stx = [0] * self.SAMPLING_PERIOD
        self.frame_count = [0] * self.SAMPLING_PERIOD
        self.status = [0] * self.SAMPLING_PERIOD
        self.angular_velocity_a = [0.0] * self.SAMPLING_PERIOD
        self.angular_velocity_b = [0.0] * self.SAMPLING_PERIOD
        self.angular_velocity_c = [0.0] * self.SAMPLING_PERIOD
        self.angular_increment_a = [0.0] * self.SAMPLING_PERIOD
        self.angular_increment_b = [0.0] * self.SAMPLING_PERIOD
        self.angular_increment_c = [0.0] * self.SAMPLING_PERIOD
        self.gyro_temp_a = [0.0] * self.SAMPLING_PERIOD
        self.gyro_temp_b = [0.0] * self.SAMPLING_PERIOD
        self.gyro_temp_c = [0.0] * self.SAMPLING_PERIOD
        self.horizontal_parity = [0] * self.SAMPLING_PERIOD
        self.etb = [0] * self.SAMPLING_PERIOD
        self.is_active = [0] * self.SAMPLING_PERIOD
        self.gyro_driver_status = [0] * self.SAMPLING_PERIOD

    def __str__(self):
        log = ["systime %s" % self.systime]
        log += ["Stx %s" % self.stx]
        log += ["フレームカウント %s" % self.frame_count]
        log += ["ステータス %s" % self.status]
        log += ["ジャイロA 角速度[deg/s] %s" % self.angular_velocity_a]
        log += ["ジャイロB 角速度[deg/s] %s" % self.angular_velocity_b]
        log += ["ジャイロC 角速度[deg/s] %s" % self.angular_velocity_c]
        log += ["ジャイロA 積分[deg] %s" % self.angular_increment_a]
        log += ["ジャイロB 積分[deg] %s" % self.angular_increment_b]
        log += ["ジャイロC 積分[deg] %s" % self.angular_increment_c]
        log += ["ジャイロA 温度[degC] %s" % self.gyro_temp_a]
        log += ["ジャイロB 温度[degC] %s" % self.gyro_temp_b]
        log += ["ジャイロC 温度[degC] %s" % self.gyro_temp_c]
        log += ["水平パリティ %s" % self.horizontal_parity]
        log += ["Etb %s" % self.etb]
        log += ["ジャイロ有効フラグ %s" % self.is_active]
        log += ["ジャイロドライバステータス %s" % self.gyro_driver_status]
        return "\n".join(log)

    def get_dict(self, sampling_index: int) -> dict:
        iru_dict = {}
        return iru_dict
