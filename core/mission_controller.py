# -*- coding: utf-8 -*-
class MissionController(object):
    """HKデータのMissionController情報を保持するクラス。"""

    HK_SIZE = 8  # byte

    def __init__(self):
        super(MissionController, self).__init__()
        self.systime = ""
        self.mission_status = ""
        self.hscm_status = ""
        self.wcam_status = ""

    def __str__(self):
        log = ["Mission Controller SIZE %d[byte]" % self.HK_SIZE]
        log += ["systime %s" % self.systime]
        log += ["ミッション系接続状態 %s" % self.mission_status]
        log += ["HSCM状態 %s" % self.hscm_status]
        log += ["PowerShot状態 %s" % self.wcam_status]
        return "\n".join(log)

    def get_dict(self) -> dict:
        mission_dict = {}
        mission_dict["mission_controller_systime"] = self.systime
        mission_dict["mission_controller_status"] = self.mission_status
        mission_dict["mission_controller_hscm_state"] = self.hscm_status
        mission_dict["mission_controller_ps_state"] = self.wcam_status
        return mission_dict
