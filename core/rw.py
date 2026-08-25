# -*- coding: utf-8 -*-
class Status(object):
    """RWのStatusを保持するクラス。"""

    def __init__(self):
        super(Status, self).__init__()
        self.servo_status = ""
        self.torque_direction = ""
        self.motor_direction = ""

    def __str__(self):
        servo_status = "Servo Status %s" % self.servo_status
        torque_direction = "Torque Direction %s" % self.torque_direction
        motor_direction = "Motor Direction %s" % self.motor_direction
        return "\n".join([servo_status, torque_direction, motor_direction])


class ErrorInfo(object):
    """RWのErrorを保持するクラス"""

    def __init__(self):
        super(ErrorInfo, self).__init__()
        self.over_voltage = ""
        self.sensor_error = ""
        self.over_current = ""
        self.over_velocity = ""
        self.storage_error = ""
        self.over_tmp = ""

    def __str__(self):
        over_voltage = "Over Voltage %s" % self.over_voltage
        sensor_error = "Sensor Error %s" % self.sensor_error
        over_current = "Over Current %s" % self.over_current
        over_velocity = "Over Velocity %s" % self.over_velocity
        storage_error = "Storage Error %s" % self.storage_error
        over_tmp = "Over Temp %s" % self.over_tmp
        return "\n".join(
            [
                over_voltage,
                sensor_error,
                over_current,
                over_velocity,
                storage_error,
                over_tmp,
            ]
        )


class Rw(object):
    """HKデータのRW情報を保持するクラス。"""

    SAMPLING_PERIOD = 10  # Hz
    UNIT_SIZE = 24  # Byte
    HK_SIZE = SAMPLING_PERIOD * UNIT_SIZE

    def __init__(self, rw_id):
        super(Rw, self).__init__()
        self.rw_id = rw_id + 1
        self.systime = ["" for _ in range(self.SAMPLING_PERIOD)]
        self.omega_dot = [0 for _ in range(self.SAMPLING_PERIOD)]
        self.omega = [0 for _ in range(self.SAMPLING_PERIOD)]
        self.status = [Status() for _ in range(self.SAMPLING_PERIOD)]
        self.dummy = [0 for _ in range(self.SAMPLING_PERIOD)]
        self.error = [ErrorInfo() for _ in range(self.SAMPLING_PERIOD)]
        self.velocity = [0.0 for _ in range(self.SAMPLING_PERIOD)]
        self.current = [0.0 for _ in range(self.SAMPLING_PERIOD)]
        self.board_tmp = [0.0 for _ in range(self.SAMPLING_PERIOD)]
        self.motor_tmp = [0.0 for _ in range(self.SAMPLING_PERIOD)]

    def __str__(self):
        log = ["RW%d SIZE %d[byte]" % (self.rw_id, self.HK_SIZE)]
        log += ["systime %s" % self.systime]
        log += ["加速度指令 %s" % self.omega_dot]
        log += ["速度指令 %s" % self.omega]
        for status in self.status:
            log += ["status %s" % status.__str__()]
        log += ["dummy %s" % self.dummy]
        for error in self.error:
            log += ["error %s" % error.__str__()]
        log += ["速度モニタ %s" % self.velocity]
        log += ["電流モニタ %s" % self.current]
        log += ["基板温度 %s" % self.board_tmp]
        log += ["モータ軸受け温度 %s" % self.motor_tmp]
        log += ["サンプリング周期 %d[Hz]" % self.SAMPLING_PERIOD]
        log += ["1サンプリングSIZE %d[byte/Hz]" % self.UNIT_SIZE]
        return "\n".join(log)

    def get_dict(self, sampling_index: int) -> dict:
        rw_dict = {}
        rw_dict[f"rw_{self.rw_id}_systime"] = self.systime[sampling_index]
        rw_dict[
            f"rw_{self.rw_id}_angular_acceleration_command_value_rpm_s"
        ] = self.omega_dot[sampling_index]
        rw_dict[
            f"rw_{self.rw_id}_angular_velocity_command_value_rpm"
        ] = self.omega[sampling_index]
        status = self.status[sampling_index]
        rw_dict[f"rw_{self.rw_id}_motor_status"] = status.servo_status
        rw_dict[f"rw_{self.rw_id}_torque_direction"] = status.torque_direction
        rw_dict[f"rw_{self.rw_id}_motor_direction"] = status.motor_direction
        rw_dict[f"rw_{self.rw_id}_dummy"] = self.dummy[sampling_index]
        error = self.error[sampling_index]
        rw_dict[f"rw_{self.rw_id}_over_voltage_status"] = error.over_voltage
        rw_dict[f"rw_{self.rw_id}_sensor_status"] = error.sensor_error
        rw_dict[f"rw_{self.rw_id}_over_current_status"] = error.over_current
        rw_dict[
            f"rw_{self.rw_id}_angular_velocity_status"
        ] = error.over_velocity
        rw_dict[f"rw_{self.rw_id}_storage_status"] = error.storage_error
        rw_dict[f"rw_{self.rw_id}_over_temperature_status"] = error.over_tmp
        rw_dict[f"rw_{self.rw_id}_angular_velocity_rpm"] = self.velocity[
            sampling_index
        ]
        rw_dict[f"rw_{self.rw_id}_current"] = self.current[sampling_index]
        rw_dict[f"rw_{self.rw_id}_board_temperature"] = self.board_tmp[
            sampling_index
        ]
        rw_dict[f"rw_{self.rw_id}_motor_temperature"] = self.motor_tmp[
            sampling_index
        ]
        return rw_dict
