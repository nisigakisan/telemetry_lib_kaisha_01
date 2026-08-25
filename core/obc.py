# -*- coding: utf-8 -*-
class Obc(object):
    """HKデータのOBC情報を保持するクラス"""

    HK_SIZE = 126  # Byte
    MAX_BATTERY_CAPACITY_mAh = 5200

    def __init__(self):
        super(Obc, self).__init__()
        self.systime = ""
        self.sap_i = 0
        self.sap_v = 0
        self.chrg_i = 0
        self.chrg_v = 0
        self.disc_i = 0
        self.disc_v = 0
        self.battery_power = 0
        self.cell_balance_thresh = 0
        self.pwm_period = 0.0
        self.pwm_duty = 0.0
        self.cell_balance_port_a = [""] * 5
        self.cell_balance_port_b = [""] * 5
        self.cell_balance_time = [[0] * 5, [0] * 5]
        self.battchg_auto_mode = ""
        self.battchg_on = ""
        self.cell_balance_mode = ""
        self.in_port_status = 0
        self.obc_fw_update_status = ""
        self.pcu_djm_fw_update_status = "-"
        self.upload_file_name = ""
        self.upload_file_error_count = 0
        self.upload_file_lost_total_size = 0
        self.upload_file_lost_offset = 0
        self.upload_file_lost_size = 0
        self.upload_file_state = ""
        self.build_date = ""
        self.revision = ""
        self.keep_alive_count = 0
        self.cpu_mode = ""
        self.rx_modem_id = ""
        self.run_app = ""
        self.reg_wrcsr = ""
        self.boot_count = 0

    def __str__(self):
        log = ["OBC SIZE %d[byte]" % self.HK_SIZE]
        log += ["systime %s" % self.systime]
        log += ["sap current %f" % self.sap_i]
        log += ["Bat charge current %f" % self.chrg_i]
        log += ["Bat discharge current %f" % self.disc_i]
        log += ["sap voltage %f" % self.sap_v]
        log += ["Bat charge voltage %f" % self.chrg_v]
        log += ["Bat discharge voltage %f" % self.disc_v]
        log += ["電池容量 %d[mAh]" % self.battery_power]
        log += ["CELLバランス回路駆動閾値 %d[mV]" % self.cell_balance_thresh]
        log += ["PWM周期 %f[uSec]" % self.pwm_period]
        log += ["CELLバランス回路駆動状態A %s" % self.cell_balance_port_a]
        log += ["CELLバランス回路駆動状態B %s" % self.cell_balance_port_b]
        log += ["バッテリー充電モード %s" % self.battchg_auto_mode]
        log += ["PWM割合 %d" % self.pwm_duty]
        log += ["充電ON/OFFフラグ %s" % self.battchg_on]
        log += ["Obc Fw Update Status %s" % self.obc_fw_update_status]
        log += ["Pcu Djm Fw Update Status %s" % self.pcu_djm_fw_update_status]
        log += ["In Port Status %s" % self.in_port_status]
        log += ["Upload file name %s" % self.upload_file_name]
        log += ["Upload file error count %d" % self.upload_file_error_count]
        log += ["Upload file lost offset %d" % self.upload_file_lost_offset]
        log += ["Upload file lost size %d" % self.upload_file_lost_size]
        log += ["Upload file state %s" % self.upload_file_state]
        log += ["Build date %s" % self.build_date]
        log += ["Revision %s" % self.revision]
        log += ["KeepAlive受信カウンタ %d" % self.keep_alive_count]
        log += ["Cpu mode %s" % self.cpu_mode]
        log += ["Rx Modem ID %s" % self.rx_modem_id]
        log += ["Run %s" % self.run_app]
        log += ["Reg WRCSR %s" % self.reg_wrcsr]
        log += ["Boot Count %d" % self.boot_count]
        return "\n".join(log)

    def get_dict(self) -> dict:
        obc_dict = {}
        obc_dict["obc_systime"] = self.systime
        obc_dict["obc_current_sap"] = self.sap_i
        obc_dict["obc_current_charge"] = self.chrg_i
        obc_dict["obc_current_discharge"] = self.disc_i
        obc_dict["obc_voltage_sap"] = self.sap_v
        obc_dict["obc_voltage_charge"] = self.chrg_v
        obc_dict["obc_voltage_discharge"] = self.disc_v
        obc_dict["obc_battery_capacity"] = self.battery_power
        obc_dict["obc_cell_threshold"] = self.cell_balance_thresh
        obc_dict["obc_pwm_period"] = self.pwm_period
        obc_dict["obc_pwm_duty"] = self.pwm_duty
        obc_dict["obc_cell_status_a"] = self.cell_balance_port_a
        obc_dict["obc_cell_status_b"] = self.cell_balance_port_b
        obc_dict["obc_battery_charge_auto_mode"] = self.battchg_auto_mode
        obc_dict["obc_charge_flag"] = self.battchg_on
        obc_dict["obc_cell_method"] = self.cell_balance_mode
        obc_dict["obc_in_port_status"] = self.in_port_status
        obc_dict["obc_fw_update_status"] = self.obc_fw_update_status
        obc_dict["obc_pcu_djm_fw_update_status"] = (
            self.pcu_djm_fw_update_status
        )
        obc_dict["obc_upload_file_name"] = self.upload_file_name
        obc_dict["obc_upload_file_error_count"] = self.upload_file_error_count
        obc_dict["obc_upload_file_lost_total_size"] = (
            self.upload_file_lost_total_size
        )
        obc_dict["obc_upload_file_lost_offset"] = self.upload_file_lost_offset
        obc_dict["obc_upload_file_lost_size"] = self.upload_file_lost_size
        obc_dict["obc_upload_file_state"] = self.upload_file_state
        obc_dict["obc_build_date"] = self.build_date
        obc_dict["obc_revision"] = self.revision
        obc_dict["obc_keep_alive"] = self.keep_alive_count
        obc_dict["obc_cpu_mode"] = self.cpu_mode
        obc_dict["obc_boot_count"] = self.boot_count
        return obc_dict

    @property
    def battery_capacity_percent(self) -> float:
        return self.battery_power / self.MAX_BATTERY_CAPACITY_mAh * 100
