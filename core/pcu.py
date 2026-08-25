# -*- coding: utf-8 -*-
from __future__ import annotations

class Ads7830Pop(object):
    """PCUのAds7830(通信機機器)の情報を保持するクラス。"""

    def __init__(self):
        super(Ads7830Pop, self).__init__()
        self.tx_a_power_ch0 = 0.0
        self.tx_a_power_ch1 = 0.0  # 未使用
        self.rx_a_power_ch2 = 0.0
        self.rx_b_power_ch3 = 0.0

        self.tx_a_volt_ch0 = 0.0
        self.tx_a_volt_ch1 = 0.0  # 未使用
        self.rx_a_volt_ch2 = 0.0
        self.rx_b_volt_ch3 = 0.0

    @staticmethod
    def __print_com_power(power_info, in_power):
        if isinstance(in_power, float):
            return "%s %f[dBm]" % (power_info, in_power)

        elif isinstance(in_power, str):
            return "%s %s[dBm]" % (power_info, in_power)

        else:
            return "-- -- [dBm]"

    def __str__(self):
        log = []
        log += [
            self.__print_com_power("Ch0 送信機Aパワー", self.tx_a_power_ch0)
        ]
        log += ["Ch0 送信機Aパワー %f [V]" % self.tx_a_volt_ch0]
        log += [
            self.__print_com_power("Ch1 送信機Aパワー", self.tx_a_power_ch1)
        ]
        log += ["Ch1 送信機Aパワー %f [V]" % self.tx_a_volt_ch1]
        log += [
            self.__print_com_power("Ch2 受信機Aパワー", self.rx_a_power_ch2)
        ]
        log += ["Ch2 受信機Aパワー %f [V]" % self.rx_a_volt_ch2]
        log += [
            self.__print_com_power("Ch3 受信機Bパワー", self.rx_b_power_ch3)
        ]
        log += ["Ch3 受信機Bパワー %f [V]" % self.rx_b_volt_ch3]
        return "\n".join(log)


class AdData(object):
    """PCUのAd Dataの情報を保持するクラス。"""

    def __init__(self):
        super(AdData, self).__init__()
        self.pcu_5v = 0.0
        self.other_pcu_v = 0.0
        self.i2c_v = 0.0

    def __str__(self):
        log = []
        log += ["PCU用+5V電源電圧 %d [V]" % self.pcu_5v]
        log += ["相手のPCUの電源電圧 %d [V]" % self.other_pcu_v]
        log += ["I2C電源電圧 %d [V]" % self.i2c_v]
        return "\n".join(log)


class I2cTmp(object):
    """PCUのI2Cの温度情報を保持するクラス。"""

    def __init__(self):
        super(I2cTmp, self).__init__()
        self.batt_control = 0.0
        self.com_power = 0.0
        self.obc = 0.0
        self.etc = 0.0

    def __str__(self):
        log = []
        log += ["バッテリ制御部 %f [degC]" % self.batt_control]
        log += ["通信機電源部 %f [degC]" % self.com_power]
        log += ["OBC周辺 %f [degC]" % self.obc]
        log += ["その他 %f [degC]" % self.etc]
        return "\n".join(log)


class I2c(object):
    """PCUのI2Cの情報を保持するクラス。"""

    def __init__(self, unit_type):
        super(I2c, self).__init__()
        self.unit_type = unit_type
        self.m_iru = 0.0  # MIRU
        self.ce_iru = 0.0  # CE IRU
        self.mic = 0.0  # ミッションPCU
        self.tx_a = 0.0  # 送信機A
        self.rx_a = 0.0  # 受信機A
        self.modem_a = 0.0  # モデムA
        self.stt1 = 0.0  # STT1
        self.stt2 = 0.0  # STT2
        self.stt3 = 0.0  # STT3
        self.stt4 = 0.0  # STT4
        self.obc_a = 0.0  # OBCA
        self.obc_b = 0.0  # OBCB
        self.tx_b = 0.0  # 送信機B
        self.rx_b = 0.0  # 受信機B
        self.modem_b = 0.0  # モデムB
        self.main = 0.0  # メイン
        self.gas = 0.0  # GAS
        self.gps1 = 0.0  # GPS1
        self.gps2 = 0.0  # GPS2

    def __str__(self):
        log = []
        unit_type = {"Voltage": "V", "Current": "mA"}
        unit_type = unit_type[self.unit_type]
        log += ["メイン %f [%s]" % (self.main, unit_type)]
        log += ["OBCA %f [%s]" % (self.obc_a, unit_type)]
        log += ["OBCB %f [%s]" % (self.obc_b, unit_type)]
        log += ["送信機A %f [%s]" % (self.tx_a, unit_type)]
        log += ["受信機A %f [%s]" % (self.rx_a, unit_type)]
        log += ["モデムA %f [%s]" % (self.modem_a, unit_type)]
        log += ["送信機B %f [%s]" % (self.tx_b, unit_type)]
        log += ["受信機B %f [%s]" % (self.rx_b, unit_type)]
        log += ["モデムB %f [%s]" % (self.modem_b, unit_type)]
        log += ["GAS %f [%s]" % (self.gas, unit_type)]
        log += ["MIRU %f [%s]" % (self.m_iru, unit_type)]
        log += ["CEIRU %f [%s]" % (self.ce_iru, unit_type)]
        log += ["STT1 %f [%s]" % (self.stt1, unit_type)]
        log += ["STT2 %f [%s]" % (self.stt2, unit_type)]
        log += ["STT3 %f [%s]" % (self.stt3, unit_type)]
        log += ["STT4 %f [%s]" % (self.stt4, unit_type)]
        log += ["GPS1 %f [%s]" % (self.gps1, unit_type)]
        log += ["GPS2 %f [%s]" % (self.gps2, unit_type)]
        log += ["MIC %f [%s]" % (self.mic, unit_type)]
        return "\n".join(log)


class Pcu(object):
    """HKデータのPCU情報を保持するクラス。"""

    HK_SIZE = 180  # Byte

    def __init__(self):
        super(Pcu, self).__init__()
        self.sys_time = ""
        self.log_size = 0
        self.pcu_id = ""
        self.pulse_status = [0] * 8
        self.pop = Ads7830Pop()
        self.power = AdData()
        self.tmp = I2cTmp()
        self.i2c_current = I2c("Current")
        self.i2c_voltage = I2c("Voltage")
        self.over_current_info = I2c("OverCurrentFlag")
        self.over_voltage_info = 0
        self.heater_pwm_value = [0] * 5 * 4
        self.rx_a_rec_status = ""
        self.rx_b_rec_status = ""
        self.time_stamp = "--:--:--:--"
        self.version = "0x00"
        self.build_time = "00:00:00"
        self.build_date = "01/01/00"
        self.heater_status = 0
        self.terminal_log = ""
        self.checksum = 0

    def __str__(self):
        log = ["PCU SIZE %d[byte]" % self.HK_SIZE]
        log += ["systime %s" % self.sys_time]
        log += ["PCU ログサイズ %d" % self.log_size]
        log += ["PCU ID %s" % self.pcu_id]
        log += ["パルス制御状況 %s" % self.pulse_status]
        log += [self.pop.__str__()]
        log += [self.power.__str__()]
        log += [self.tmp.__str__()]
        log += [self.i2c_current.__str__()]
        log += [self.i2c_voltage.__str__()]
        log += [f"DJMのヒータ駆動PWM値 {self.heater_pwm_value}"]
        log += ["PCU時刻 %s" % self.time_stamp]
        log += ["version %s" % self.version]
        log += ["ビルド時刻 %s" % self.build_time]
        log += ["ビルド日時 %s" % self.build_date]
        log += ["ターミナルログ %s" % self.terminal_log]
        log += ["チェックサム %d" % self.checksum]
        return "\n".join(log)

    @staticmethod
    def __convert_tx_rx_power_data_to_numeric(
        power: str | float,
    ) -> int | float:
        if isinstance(power, str):
            if power == "Under":
                return 0x7FFF
            elif power == "Over":
                return 0x7FFF
            else:
                return 0xFFFF  # Unknown
        return power

    def get_current_transmitter_system(self) -> str:
        i2c_voltage = self.i2c_voltage
        if check_power_on(i2c_voltage.tx_a):
            return "A"
        elif check_power_on(i2c_voltage.tx_b):
            return "B"
        else:
            return ""

    def get_dict(self) -> dict:
        pcu_dict = {}
        pcu_dict["pcu_systime"] = self.sys_time
        pcu_dict["pcu_log_size"] = self.log_size
        pcu_dict["pcu_id"] = self.pcu_id
        pcu_dict.update(
            create_indexed_elements_dict(
                self.pulse_status, "pcu_pulse_control_state"
            )
        )

        pop = self.pop
        pcu_dict["pcu_transmitter_a_power_ch0"] = (
            self.__convert_tx_rx_power_data_to_numeric(pop.tx_a_power_ch0)
        )
        pcu_dict["pcu_transmitter_a_power_ch1"] = (
            self.__convert_tx_rx_power_data_to_numeric(pop.tx_a_power_ch1)
        )
        pcu_dict["pcu_receiver_a_power_ch2"] = (
            self.__convert_tx_rx_power_data_to_numeric(pop.rx_a_power_ch2)
        )
        pcu_dict["pcu_receiver_b_power_ch3"] = (
            self.__convert_tx_rx_power_data_to_numeric(pop.rx_b_power_ch3)
        )
        pcu_dict["pcu_transmitter_a_voltage_ch0"] = pop.tx_a_volt_ch0
        pcu_dict["pcu_transmitter_a_voltage_ch1"] = pop.tx_a_volt_ch1
        pcu_dict["pcu_receiver_a_voltage_ch2"] = pop.rx_a_volt_ch2
        pcu_dict["pcu_receiver_b_voltage_ch3"] = pop.rx_b_volt_ch3

        power = self.power
        pcu_dict["pcu_5v"] = power.pcu_5v
        pcu_dict["pcu_other_pcu_v"] = power.other_pcu_v
        pcu_dict["pcu_i2c_v"] = power.i2c_v

        tmp = self.tmp
        pcu_dict["pcu_temperature_battery_controller"] = tmp.batt_control
        pcu_dict["pcu_temperature_com_controller"] = tmp.com_power
        pcu_dict["pcu_temperature_obc"] = tmp.obc
        pcu_dict["pcu_temperature_other"] = tmp.etc

        for i2c_data, vol_cur_str in [
            (self.i2c_current, "current"),
            (self.i2c_voltage, "voltage"),
            (self.over_current_info, "over_current_flag"),
        ]:
            pcu_dict[f"pcu_{vol_cur_str}_transmitter_a"] = i2c_data.tx_a
            pcu_dict[f"pcu_{vol_cur_str}_receiver_a"] = i2c_data.rx_a
            pcu_dict[f"pcu_{vol_cur_str}_modem_a"] = i2c_data.modem_a
            pcu_dict[f"pcu_{vol_cur_str}_obc_b"] = i2c_data.obc_b
            pcu_dict[f"pcu_{vol_cur_str}_obc_a"] = i2c_data.obc_a
            pcu_dict[f"pcu_{vol_cur_str}_transmitter_b"] = i2c_data.tx_b
            pcu_dict[f"pcu_{vol_cur_str}_receiver_b"] = i2c_data.rx_b
            pcu_dict[f"pcu_{vol_cur_str}_modem_b"] = i2c_data.modem_b
            pcu_dict[f"pcu_{vol_cur_str}_main"] = i2c_data.main
            pcu_dict[f"pcu_{vol_cur_str}_stt_1"] = i2c_data.stt1
            pcu_dict[f"pcu_{vol_cur_str}_stt_2"] = i2c_data.stt2
            pcu_dict[f"pcu_{vol_cur_str}_stt_3"] = i2c_data.stt3
            pcu_dict[f"pcu_{vol_cur_str}_stt_4"] = i2c_data.stt4
            pcu_dict[f"pcu_{vol_cur_str}_miru"] = i2c_data.m_iru
            pcu_dict[f"pcu_{vol_cur_str}_ceiru"] = i2c_data.ce_iru
            pcu_dict[f"pcu_{vol_cur_str}_gps1"] = i2c_data.gps1
            pcu_dict[f"pcu_{vol_cur_str}_gps2"] = i2c_data.gps2
            pcu_dict[f"pcu_{vol_cur_str}_gas"] = i2c_data.gas
            pcu_dict[f"pcu_{vol_cur_str}_mission_pcu"] = i2c_data.mic

        pcu_dict["pcu_over_voltage_flag"] = self.over_voltage_info

        heater_num = 2
        for djm_id in range(5):
            for heater_id in range(heater_num):
                pcu_dict[f"pcu_djm_heater_pwm_{djm_id}_{heater_id}"] = (
                    self.heater_pwm_value[djm_id * heater_num + heater_id]
                )

        pcu_dict["pcu_receiver_a_status"] = self.rx_a_rec_status
        pcu_dict["pcu_receiver_b_status"] = self.rx_b_rec_status
        pcu_dict["pcu_time"] = self.time_stamp
        pcu_dict["pcu_version"] = self.version
        pcu_dict["pcu_build_time"] = self.build_time
        pcu_dict["pcu_build_date"] = self.build_date
        return pcu_dict
