# -*- coding: utf-8 -*-
class StarInfo(object):
    """STTのStarInfo情報を保持するクラス。"""

    def __init__(self, star_info_id):
        super(StarInfo, self).__init__()
        self.star_info_id = star_info_id + 1
        self.hipparcos_id = 0
        self.luminance = 0
        self.azimuth = 0
        self.elevation = 0

    def __str__(self):
        log = ["StarInfo%d" % self.star_info_id]
        log += ["hipparcos_id %d" % self.hipparcos_id]
        log += ["luminance %d" % self.luminance]
        log += ["azimuth %d" % self.azimuth]
        log += ["elevation %d" % self.elevation]
        return "\n".join(log)


class Stt(object):
    """HKデータのSTT情報を保持するクラス。"""

    HK_SIZE = 228  # byte

    def __init__(self, stt_id: int):
        super(Stt, self).__init__()
        self.stt_id = stt_id + 1
        self.systime = ""
        self.capture_id = 0
        self.estimation_status = ""
        self.attitude = [0] * 4
        self.attitude_time = ""
        self.board_temp = 0.0
        self.cmos_temp = 0.0
        self.fpga_detected_star_cnt = 0
        self.cpu_detected_star_cnt = 0
        self.detected_star_cnt = 0
        self.star_info = [StarInfo(info_id) for info_id in range(8)]
        self.attitude_error = 0.0
        self.focal_length = 0.0

    def __str__(self):
        log = ["STT%d SIZE %d[byte]" % (self.stt_id, self.HK_SIZE)]
        log += ["systime %s" % self.systime]
        log += ["capture_id %d" % self.capture_id]
        log += ["estimation_status %s" % self.estimation_status]
        log += ["attitude %s" % self.attitude]
        log += ["board_temp %f" % self.board_temp]
        log += ["cmos_temp %f" % self.cmos_temp]
        log += ["detected_star_cnt (FPGA) %d" % self.fpga_detected_star_cnt]
        log += ["detected_star_cnt (CPU) %d" % self.cpu_detected_star_cnt]
        log += ["detected_star_cnt %d" % self.detected_star_cnt]
        for info_id in range(8):
            log += [self.star_info[info_id].__str__()]
        log += ["attitude_error %f" % self.attitude_error]
        log += ["focal_length %f" % self.focal_length]
        return "\n".join(log)

    def get_dict(self) -> dict:
        stt_dict = {}
        stt_dict[f"stt{self.stt_id}_systime"] = self.systime
        stt_dict[f"stt{self.stt_id}_capture_id"] = self.capture_id
        stt_dict[f"stt{self.stt_id}_estimation_status"] = (
            self.estimation_status
        )
        stt_dict.update(
            create_indexed_elements_dict(
                self.attitude, f"stt{self.stt_id}_quaternion_s2i"
            )
        )
        stt_dict[f"stt{self.stt_id}_attitude_time"] = self.attitude_time
        stt_dict[f"stt{self.stt_id}_board_temp"] = self.board_temp
        stt_dict[f"stt{self.stt_id}_cmos_temp"] = self.cmos_temp
        stt_dict[f"stt{self.stt_id}_detected_star_count_fpga"] = (
            self.fpga_detected_star_cnt
        )
        stt_dict[f"stt{self.stt_id}_detected_star_count_cpu"] = (
            self.cpu_detected_star_cnt
        )
        stt_dict[f"stt{self.stt_id}_detected_star_count_stt"] = (
            self.detected_star_cnt
        )

        for index, star_info in enumerate(self.star_info, start=1):
            stt_dict[f"stt{self.stt_id}_hipparcos_id_{index}"] = (
                star_info.hipparcos_id
            )
            stt_dict[f"stt{self.stt_id}_luminance_{index}"] = (
                star_info.luminance
            )
            stt_dict[f"stt{self.stt_id}_tan_azimuth_{index}"] = (
                star_info.azimuth
            )
            stt_dict[f"stt{self.stt_id}_tan_elevation_{index}"] = (
                star_info.elevation
            )

        stt_dict[f"stt{self.stt_id}_attitude_error"] = self.attitude_error
        stt_dict[f"stt{self.stt_id}_focal_length"] = self.focal_length
        return stt_dict
