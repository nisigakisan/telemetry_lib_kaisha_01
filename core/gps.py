# -*- coding: utf-8 -*-
from enum import Enum, auto


class GpsIndex(Enum):
    GPS_NONE = -1
    GPS1 = 0
    GPS2 = 1
    UNKNOWN = auto()


class ReceiverStatus(object):
    """docstring for ReceiverStatus"""

    def __init__(self):
        super(ReceiverStatus, self).__init__()
        self.error_flag = None
        self.temp_status = None
        self.vol_supply_status = None
        self.primary_ant_power_status = None
        self.lna = None
        self.primary_ant_open_circuit_flag = None
        self.primary_ant_short_circuit_flag = None
        self.cpu_overload_flag = None
        self.comport_buff_overrun = None
        self.link_overrun_flag = None
        self.input_overrun_flag = None
        self.aux_transmit_overrun_flag = None
        self.agc_out_of_range = None
        self.jammer_detected = None
        self.ins_reset_flag = None
        self.imu_com_failure = None
        self.gps_almanac_flag = None
        self.pos_solution_flag = None
        self.pos_fixed_flag = None
        self.clock_steering_status = None
        self.clock_model_flag = None
        self.ext_oscillator_locked_flag = None
        self.software_resource = None
        self.version_bit = None
        self.tracking_mode = None
        self.digital_filtering_enabled = None
        self.aux3_status_event_flag = None
        self.aux2_status_event_flag = None
        self.aux1_status_event_flag = None

    def __str__(self):
        status = [
            "Error flag : %s" % self.error_flag,
            "Tempareture status : %s" % self.temp_status,
            "Voltage supply status : %s" % self.vol_supply_status,
            "Primary antenna power status : %s"
            % self.primary_ant_power_status,
            "LNA Failure : %s" % self.lna,
            "Primary antenna open circuit flag : %s"
            % self.primary_ant_open_circuit_flag,
            "Primary antenna short circuit flag : %s"
            % self.primary_ant_short_circuit_flag,
            "CPU overload flag : %s" % self.cpu_overload_flag,
            "COM port transmit buffer overrun : %s"
            % self.comport_buff_overrun,
            "Link overrun flag : %s" % self.link_overrun_flag,
            "Input overrun flag : %s" % self.input_overrun_flag,
            "Aux transmit overrun flag : %s" % self.aux_transmit_overrun_flag,
            "AGC out of range : %s" % self.agc_out_of_range,
            "Jammer Detected : %s" % self.jammer_detected,
            "INS reset flag : %s" % self.ins_reset_flag,
            "IMU communication failure : %s" % self.imu_com_failure,
            "GPS almanac flag/UTC known : %s" % self.gps_almanac_flag,
            "Position solution flag : %s" % self.pos_solution_flag,
            "Position fixed flag : %s" % self.pos_fixed_flag,
            "Clock steering status : %s" % self.clock_steering_status,
            "Clock model flag : %s" % self.clock_model_flag,
            "External oscillator locked flag : %s"
            % self.ext_oscillator_locked_flag,
            "Software resource : %s" % self.software_resource,
            "Version bit : %s" % self.version_bit,
            "Tracking mode : %s" % self.tracking_mode,
            "Digital Filtering Enabled : %s" % self.digital_filtering_enabled,
            "Auxiliary3 status event flag : %s" % self.aux3_status_event_flag,
            "Auxiliary2 status event flag : %s" % self.aux2_status_event_flag,
            "Auxiliary1 status event flag : %s" % self.aux1_status_event_flag,
        ]
        return "\n".join(status)


class Gps(object):
    """HKデータのGPS情報を保持するクラス."""

    HK_SIZE = 136  # byte

    def __init__(self):
        super(Gps, self).__init__()
        self.systime = ""
        self.lat_deg = 0
        self.long_deg = 0
        self.altitude = 0
        self.x_pos_vec = 0
        self.y_pos_vec = 0
        self.z_pos_vec = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.z_velocity = 0
        self.utc = 0
        self.dummy1 = 0
        self.num_of_satellites_tracked = 0
        self.num_of_sat_used_in_solution = 0
        self.num_of_sat_vehicles_used_in_solution = 0
        self.gps_glonass_sig_mask = 0
        self.receiver_status = 0
        self.solution_status = 0
        self.position_type = 0
        self.velocity_type = 0
        self.time_clock_status = 0
        self.bestpos_gps_week = 0
        self.bestpos_gps_ms = 0
        self.dummy2 = 0
        self.bestxyz_gps_ms = 0
        self.time_gps_ms = 0
        self.receiverStatusCls = ReceiverStatus()
        self.gps_index = GpsIndex.GPS_NONE

    def __str__(self):
        log = ["GPS SIZE %d[byte]" % self.HK_SIZE]
        log += ["systime %s" % self.systime]
        log += ["lat_deg %s" % self.lat_deg]
        log += ["long_deg %s" % self.long_deg]
        log += ["altitude %s" % self.altitude]
        log += ["x_pos_vec %s" % self.x_pos_vec]
        log += ["y_pos_vec %s" % self.y_pos_vec]
        log += ["z_pos_vec %s" % self.z_pos_vec]
        log += ["x_velocity %s" % self.x_velocity]
        log += ["y_velocity %s" % self.y_velocity]
        log += ["z_velocity %s" % self.z_velocity]
        log += ["utc %s" % self.utc]
        log += ["satellites_tracked %d" % self.num_of_satellites_tracked]
        log += ["sat_used_in_solution %d" % self.num_of_sat_used_in_solution]
        log += [
            "sat_vehicles_used_in_solution %s"
            % self.num_of_sat_vehicles_used_in_solution
        ]
        log += ["gps_glonass_sig_mask %s" % self.gps_glonass_sig_mask]
        log += ["solution_status %s" % self.solution_status]
        log += ["position_type %s" % self.position_type]
        log += ["velocity_type %s" % self.velocity_type]
        log += ["time_clock_status %s" % self.time_clock_status]
        log += ["bestpos_gps_week %s" % self.bestpos_gps_week]
        log += ["bestpos_gps_ms %s" % self.bestpos_gps_ms]
        log += ["bestxyz_gps_ms %s" % self.bestxyz_gps_ms]
        log += ["time_gps_ms %s" % self.time_gps_ms]
        log += ["dummy1 %d" % self.dummy1]
        log += ["dummy2 %d" % self.dummy2]
        log += [str(self.receiverStatusCls)]
        log += [f"gps_index {self.gps_index.value}"]
        return "\n".join(log)

    def get_dict(self) -> dict:
        gps_dict = {}
        gps_dict["gps_systime"] = self.systime
        gps_dict["gps_latitude"] = self.lat_deg
        gps_dict["gps_longitude"] = self.long_deg
        gps_dict["gps_altitude"] = self.altitude
        gps_dict["gps_ecef_position_x"] = self.x_pos_vec
        gps_dict["gps_ecef_position_y"] = self.y_pos_vec
        gps_dict["gps_ecef_position_z"] = self.z_pos_vec
        gps_dict["gps_ecef_velocity_x"] = self.x_velocity
        gps_dict["gps_ecef_velocity_y"] = self.y_velocity
        gps_dict["gps_ecef_velocity_z"] = self.z_velocity
        gps_dict["gps_utc"] = self.utc
        gps_dict["gps_satellites_tracked"] = self.num_of_satellites_tracked
        gps_dict["gps_sat_used_in_solution"] = self.num_of_sat_used_in_solution
        gps_dict["gps_sat_vehicles_used_in_solution"] = (
            self.num_of_sat_vehicles_used_in_solution
        )
        gps_dict["gps_gps_glonass_sig_mask"] = self.gps_glonass_sig_mask
        gps_dict["gps_receiver_status"] = self.receiver_status
        gps_dict["gps_solution_status"] = self.solution_status
        gps_dict["gps_position_type"] = self.position_type
        gps_dict["gps_velocity_type"] = self.velocity_type
        gps_dict["gps_time_clock_status"] = self.time_clock_status
        gps_dict["gps_bestpos_gps_week"] = self.bestpos_gps_week
        gps_dict["gps_bestpos_gps_ms"] = self.bestpos_gps_ms
        gps_dict["gps_bestxyz_gps_ms"] = self.bestxyz_gps_ms
        gps_dict["gps_time_gps_ms"] = self.time_gps_ms

        receiver_status = self.receiverStatusCls
        gps_dict["gps_error_flag"] = receiver_status.error_flag
        gps_dict["gps_temperature_status"] = receiver_status.temp_status
        gps_dict["gps_vol_supply_status"] = receiver_status.vol_supply_status
        gps_dict["gps_primary_ant_power_status"] = (
            receiver_status.primary_ant_power_status
        )
        gps_dict["gps_lna"] = receiver_status.lna
        gps_dict["gps_primary_ant_open_circuit_flag"] = (
            receiver_status.primary_ant_open_circuit_flag
        )
        gps_dict["gps_primary_ant_short_circuit_flag"] = (
            receiver_status.primary_ant_short_circuit_flag
        )
        gps_dict["gps_cpu_overload_flag"] = receiver_status.cpu_overload_flag
        gps_dict["gps_comport_buff_overrun"] = (
            receiver_status.comport_buff_overrun
        )
        gps_dict["gps_link_overrun_flag"] = receiver_status.link_overrun_flag
        gps_dict["gps_input_overrun_flag"] = receiver_status.input_overrun_flag
        gps_dict["gps_aux_transmit_overrun_flag"] = (
            receiver_status.aux_transmit_overrun_flag
        )
        gps_dict["gps_agc_out_of_range"] = receiver_status.agc_out_of_range
        gps_dict["gps_jammer_detected"] = receiver_status.jammer_detected
        gps_dict["gps_ins_reset_flag"] = receiver_status.ins_reset_flag
        gps_dict["gps_imu_com_failure"] = receiver_status.imu_com_failure
        gps_dict["gps_gps_almanac_flag"] = receiver_status.gps_almanac_flag
        gps_dict["gps_pos_solution_flag"] = receiver_status.pos_solution_flag
        gps_dict["gps_pos_fixed_flag"] = receiver_status.pos_fixed_flag
        gps_dict["gps_clock_steering_status"] = (
            receiver_status.clock_steering_status
        )
        gps_dict["gps_clock_model_flag"] = receiver_status.clock_model_flag
        gps_dict["gps_ext_oscillator_locked_flag"] = (
            receiver_status.ext_oscillator_locked_flag
        )
        gps_dict["gps_software_resource"] = receiver_status.software_resource
        gps_dict["gps_version_bit"] = receiver_status.version_bit
        gps_dict["gps_tracking_mode"] = receiver_status.tracking_mode
        gps_dict["gps_digital_filtering_enabled"] = (
            receiver_status.digital_filtering_enabled
        )
        gps_dict["gps_aux3_status_event_flag"] = (
            receiver_status.aux3_status_event_flag
        )
        gps_dict["gps_aux2_status_event_flag"] = (
            receiver_status.aux2_status_event_flag
        )
        gps_dict["gps_aux1_status_event_flag"] = (
            receiver_status.aux1_status_event_flag
        )
        gps_dict["gps_index"] = self.gps_index.value
        return gps_dict
