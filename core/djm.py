# -*- coding: utf-8 -*-
class I2c(object):
    """DJMのI2Cの情報を保持するクラス。"""

    def __init__(self, unit_type):
        super(I2c, self).__init__()
        self.unit_type = unit_type
        self.cpu_i2c_origin = 0.0  # +5V(CPUとその周辺、I2Cの3.3Vの元)
        self.djm_15 = 0.0  # DJM電源15V
        self.temp_sensor = 0.0  # 温度センサ電源
        self.mtq = 0.0  # MTQ用電源
        self.sas1 = 0.0  # 太陽センサ1の電源
        self.sas2 = 0.0  # 太陽センサ2の電源
        self.djm_i2c = 0.0  # I2C 3.3V電源
        self.heater1 = 0.0  # ヒータ1電源(+15V無制御)
        self.heater2 = 0.0  # ヒータ2電源(+15V無制御)
        self.heater3 = 0.0  # ヒータ3電源(+15V無制御)
        self.heater4 = 0.0  # ヒータ4電源(+15V無制御)
        self.hdrm1 = 0.0  # HDRM1電源
        self.hdrm2 = 0.0  # HDRM2電源

    def __str__(self):
        unit_type = {"Voltage": 'V', "Current": 'mA', "OverCurrentFlag": 'flag'}
        unit_type = unit_type[self.unit_type]
        log = []
        log += [
            "+5V(CPUとその周辺、I2Cの3.3Vの元) %f[%s]"
            % (self.cpu_i2c_origin, unit_type)
        ]
        log += ["[DJM電源15V %f[%s]" % (self.djm_15, unit_type)]
        log += ["[温度センサ電源 %f[%s]" % (self.temp_sensor, unit_type)]
        log += ["[太陽センサ1の電源 %f[%s]" % (self.sas1, unit_type)]
        log += ["[太陽センサ2の電源 %f[%s]" % (self.sas2, unit_type)]
        log += ["[MTQ用電源 %f[%s]" % (self.mtq, unit_type)]
        log += ["[I2C 3.3V電源 %f[%s]" % (self.djm_i2c, unit_type)]
        log += ["[ヒータ1電源(+15V無制御) %f[%s]" % (self.heater1, unit_type)]
        log += ["[ヒータ2電源(+15V無制御) %f[%s]" % (self.heater2, unit_type)]
        log += ["[ヒータ3電源(+15V無制御) %f[%s]" % (self.heater3, unit_type)]
        log += ["[ヒータ4電源(+15V無制御) %f[%s]" % (self.heater4, unit_type)]
        log += ["[HDRM1電源 %f[%s]" % (self.hdrm1, unit_type)]
        log += ["[HDRM2電源 %f[%s]" % (self.hdrm2, unit_type)]
        return "\n".join(log)

    @staticmethod
    def get_mtq_axis(djm_id: int) -> str:
        mtq_axis_dict = {1: "nc", 2: "nc", 3: "y", 4: "z", 5: "x"}
        return mtq_axis_dict.get(djm_id, "unknown")

    @staticmethod
    def get_heater_name(djm_id: int, heater_id: int) -> str:
        heater_name_dict = {
            (1, 1): "htr",
            (1, 2): "nc",
            (1, 3): "nc",
            (1, 4): "nc",
            (2, 1): "sub_mirror_2",
            (2, 2): "bench_1",
            (2, 3): "nc",
            (2, 4): "peltier",
            (3, 1): "bench_hub",
            (3, 2): "bench_3",
            (3, 3): "nc",
            (3, 4): "nc",
            (4, 1): "sub_mirror_1",
            (4, 2): "nc",
            (4, 3): "nc",
            (4, 4): "nc",
            (5, 1): "nc",
            (5, 2): "bench_2",
            (5, 3): "nc",
            (5, 4): "nc",
        }
        return heater_name_dict.get((djm_id, heater_id), "unknown")


class Sas(object):
    """DJMの太陽センサ情報を保持するクラス。"""

    def __init__(self):
        super(Sas, self).__init__()
        self.x_angle = 0.0
        self.y_angle = 0.0
        self.tmp = 0.0
        self.gain = 0
        self.x_peak = 0
        self.y_peak = 0
        self.sensor_gain_mode = ""
        self.error_chk = ""
        self.timestamp = ""

    def __str__(self):
        log = ["【太陽センサー】"]
        if isinstance(self.x_angle, float):
            log += ["X軸 %f[deg]" % self.x_angle]
        elif isinstance(self.x_angle, str):
            log += ["X軸 %s[deg]" % self.x_angle]

        if isinstance(self.y_angle, float):
            log += ["Y軸 %f[deg]" % self.y_angle]
        elif isinstance(self.y_angle, str):
            log += ["Y軸 %s[deg]" % self.y_angle]

        log += ["温度 %f[degC]" % self.tmp]
        log += ["ゲイン %f[msec]" % self.gain]
        log += ["X軸ピーク輝度値 %d" % self.x_peak]
        log += ["Y軸ピーク輝度値 %d" % self.y_peak]
        log += ["センサゲインモード %s" % self.sensor_gain_mode]
        log += ["エラーチェック %s" % self.error_chk]
        log += ["データ取得時刻 %s" % (self.timestamp)]
        return "\n".join(log)


class Djm(object):
    """HKデータのDJM情報を保持するクラス。"""

    HK_SIZE = 160  # Byte

    def __init__(self, djm_id: int):
        super(Djm, self).__init__()
        self.djm_id = djm_id
        self.systime = ""
        self.log_size = 0
        self.hk_djm_id = 0
        self.string_v = [0.0] * 8
        self.pulse_status = [0] * 4
        self.sap_panel_v = 0.0
        self.sap_panel_i = 0.0
        self.i2c_sas_power = 0.0
        self.tmp = 0.0
        self.ads1115_temp = [0.0] * 10
        self.i2c_current = I2c("Current")
        self.i2c_voltage = I2c("Voltage")
        self.over_current_info = I2c("OverCurrentFlag")
        self.sas1 = Sas()
        self.sas2 = Sas()
        self.time_stamp = ""
        self.djm_version = "0x00"
        self.build_time = "00:00:00"
        self.build_date = "1900/01/01"
        self.terminal_log = ""
        self.checksum = 0

    def __str__(self):
        log = ["DJM %d SIZE %d[byte]" % (self.djm_id, self.HK_SIZE)]
        log += ["systime %s" % self.systime]
        log += ["DJMログサイズ %d" % (self.log_size)]
        log += ["DJM基板ID %d" % (self.hk_djm_id)]
        log += ["ストリング電圧1~8 %s" % (self.string_v)]
        log += ["パルスの出力状況 %s" % (self.pulse_status)]
        log += ["太陽電池パネル面電圧 %f" % (self.sap_panel_v)]
        log += ["太陽電池パネル面電流 %f" % (self.sap_panel_i)]
        log += ["I2C監視用2.5V %f" % (self.i2c_sas_power)]
        log += ["DJM基板温度 %f" % self.tmp]
        log += [self.i2c_current.__str__()]
        log += [self.i2c_voltage.__str__()]
        log += [self.sas1.__str__()]
        log += [self.sas2.__str__()]
        log += ["DJM時刻 %s" % (self.time_stamp)]
        log += ["Version %s" % (self.djm_version)]
        log += ["ビルド時刻 %s" % (self.build_time)]
        log += ["ビルド日時 %s" % (self.build_date)]
        log += ["ターミナルログ %s" % (self.terminal_log)]
        log += ["チェックサム %d" % (self.checksum)]
        return "\n".join(log)

    @property
    def mounting_face(self) -> str:
        mounting_face_dict = {1: "py", 2: "mz", 3: "mx", 4: "px", 5: "my"}
        return mounting_face_dict.get(self.djm_id, "unknown")

    def get_dict(self) -> dict:
        djm_dict = {}
        djm_dict[f"djm_{self.djm_id}_systime"] = self.systime
        djm_dict[f"djm_{self.djm_id}_log_size"] = self.log_size
        djm_dict[f"djm_{self.djm_id}_board_id"] = self.hk_djm_id
        djm_dict.update(
            create_indexed_elements_dict(
                self.string_v, f"djm_{self.djm_id}_string_voltage"
            )
        )
        djm_dict.update(
            create_indexed_elements_dict(
                self.pulse_status, f"djm_{self.djm_id}_output_pulse"
            )
        )
        djm_dict[f"djm_{self.djm_id}_sap_panel_voltage"] = self.sap_panel_v
        djm_dict[f"djm_{self.djm_id}_sap_panel_current"] = self.sap_panel_i
        djm_dict[f"djm_{self.djm_id}_voltage_i2c"] = self.i2c_sas_power
        djm_dict[f"djm_{self.djm_id}_temperature_board"] = self.tmp

        i2c_current = self.i2c_current
        i2c_voltage = self.i2c_voltage
        over_current_info = self.over_current_info
        heater1_name = i2c_current.get_heater_name(self.djm_id, 1)
        heater2_name = i2c_current.get_heater_name(self.djm_id, 2)
        heater3_name = i2c_current.get_heater_name(self.djm_id, 3)
        heater4_name = i2c_current.get_heater_name(self.djm_id, 4)
        mtq_axis = i2c_current.get_mtq_axis(self.djm_id)
        for i2c_data, unit in zip(
            [i2c_current, i2c_voltage, over_current_info],
            ["current", "voltage", "over_current_flag"],
        ):
            djm_dict[f"djm_{self.djm_id}_{unit}_5v"] = i2c_data.cpu_i2c_origin
            djm_dict[f"djm_{self.djm_id}_{unit}_power_supply_15v"] = (
                i2c_data.djm_15
            )
            djm_dict[f"djm_{self.djm_id}_{unit}_temperature_sensor"] = (
                i2c_data.temp_sensor
            )
            djm_dict[
                f"djm_{self.djm_id}_{unit}_sas_1_{self.mounting_face}"
            ] = i2c_data.sas1
            djm_dict[
                f"djm_{self.djm_id}_{unit}_sas_2_{self.mounting_face}"
            ] = i2c_data.sas2
            djm_dict[f"djm_{self.djm_id}_{unit}_mtq_{mtq_axis}"] = i2c_data.mtq
            djm_dict[f"djm_{self.djm_id}_{unit}_i2c_3_3v"] = i2c_data.djm_i2c
            djm_dict[f"djm_{self.djm_id}_{unit}_heater_1_{heater1_name}"] = (
                i2c_data.heater1
            )
            djm_dict[f"djm_{self.djm_id}_{unit}_heater_2_{heater2_name}"] = (
                i2c_data.heater2
            )
            djm_dict[f"djm_{self.djm_id}_{unit}_heater_3_{heater3_name}"] = (
                i2c_data.heater3
            )
            djm_dict[f"djm_{self.djm_id}_{unit}_heater_4_{heater4_name}"] = (
                i2c_data.heater4
            )
            djm_dict[f"djm_{self.djm_id}_{unit}_hdrm_1"] = i2c_data.hdrm1
            djm_dict[f"djm_{self.djm_id}_{unit}_hdrm_2"] = i2c_data.hdrm2

        djm_dict[f"djm_{self.djm_id}_sas_1_{self.mounting_face}_angle_x"] = (
            convert_sas_angle_data_to_numeric(self.sas1.x_angle)
        )
        djm_dict[f"djm_{self.djm_id}_sas_1_{self.mounting_face}_angle_y"] = (
            convert_sas_angle_data_to_numeric(self.sas1.y_angle)
        )
        djm_dict[
            f"djm_{self.djm_id}_sas_1_{self.mounting_face}_temperature"
        ] = self.sas1.tmp
        djm_dict[f"djm_{self.djm_id}_sas_1_{self.mounting_face}_gain"] = (
            self.sas1.gain
        )
        djm_dict[f"djm_{self.djm_id}_sas_1_{self.mounting_face}_peak_x"] = (
            self.sas1.x_peak
        )
        djm_dict[f"djm_{self.djm_id}_sas_1_{self.mounting_face}_peak_y"] = (
            self.sas1.y_peak
        )
        djm_dict[
            f"djm_{self.djm_id}_sas_1_{self.mounting_face}_sensor_gain"
        ] = self.sas1.sensor_gain_mode
        djm_dict[
            f"djm_{self.djm_id}_sas_1_{self.mounting_face}_error_check"
        ] = self.sas1.error_chk
        djm_dict[f"djm_{self.djm_id}_sas_1_{self.mounting_face}_timestamp"] = (
            self.sas1.timestamp
        )

        djm_dict[f"djm_{self.djm_id}_sas_2_{self.mounting_face}_angle_x"] = (
            convert_sas_angle_data_to_numeric(self.sas1.x_angle)
        )
        djm_dict[f"djm_{self.djm_id}_sas_2_{self.mounting_face}_angle_y"] = (
            convert_sas_angle_data_to_numeric(self.sas2.y_angle)
        )
        djm_dict[
            f"djm_{self.djm_id}_sas_2_{self.mounting_face}_temperature"
        ] = self.sas2.tmp
        djm_dict[f"djm_{self.djm_id}_sas_2_{self.mounting_face}_gain"] = (
            self.sas2.gain
        )
        djm_dict[f"djm_{self.djm_id}_sas_2_{self.mounting_face}_peak_x"] = (
            self.sas2.x_peak
        )
        djm_dict[f"djm_{self.djm_id}_sas_2_{self.mounting_face}_peak_y"] = (
            self.sas2.y_peak
        )
        djm_dict[
            f"djm_{self.djm_id}_sas_2_{self.mounting_face}_sensor_gain"
        ] = self.sas2.sensor_gain_mode
        djm_dict[
            f"djm_{self.djm_id}_sas_2_{self.mounting_face}_error_check"
        ] = self.sas2.error_chk
        djm_dict[f"djm_{self.djm_id}_sas_2_{self.mounting_face}_timestamp"] = (
            self.sas2.timestamp
        )

        djm_dict[f"djm_{self.djm_id}_time"] = self.time_stamp
        djm_dict[f"djm_{self.djm_id}_version"] = self.djm_version
        djm_dict[f"djm_{self.djm_id}_build_time"] = self.build_time
        djm_dict[f"djm_{self.djm_id}_build_date"] = self.build_date
        return djm_dict
