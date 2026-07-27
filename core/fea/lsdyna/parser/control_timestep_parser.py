from core.fea.parser import Parser
from core.fea.lsdyna.keywords.control_timestep import ControlTimestep


class ControlTimestepParser(Parser):
    def __init__(self):
        super().__init__()

        self.version = {
            "12.0": self._12p0,
            "13.0": self._12p0,
        }

    def _12p0(self, line_raw):
        dtinit_raw = line_raw[0:10].strip()
        tssfac_raw = line_raw[10:20].strip()
        isdo_raw = line_raw[20:30].strip()
        tslimt_raw = line_raw[30:40].strip()
        dt2ms_raw = line_raw[40:50].strip()
        lctm_raw = line_raw[50:60].strip()
        erode_raw = line_raw[60:70].strip()
        ms1st_raw = line_raw[70:80].strip()

        if len(dtinit_raw) > 0:
            dtinit = self.dataframe.parameter[dtinit_raw[1:]].value if dtinit_raw.startswith("&") else float(dtinit_raw)
        else:
            dtinit = 0

        if len(tssfac_raw) > 0:
            tssfac = self.dataframe.parameter[tssfac_raw[1:]].value if tssfac_raw.startswith("&") else float(tssfac_raw)
        else:
            tssfac = 0

        if len(isdo_raw) > 0:
            isdo = self.dataframe.parameter[isdo_raw[1:]].value if isdo_raw.startswith("&") else int(isdo_raw)
        else:
            isdo = 0

        if len(tslimt_raw) > 0:
            tslimt = self.dataframe.parameter[tslimt_raw[1:]].value if tslimt_raw.startswith("&") else float(tslimt_raw)
        else:
            tslimt = 0

        if len(dt2ms_raw) > 0:
            dt2ms = self.dataframe.parameter[dt2ms_raw[1:]].value if dt2ms_raw.startswith("&") else float(dt2ms_raw)
        else:
            dt2ms = 0

        if len(lctm_raw) > 0:
            lctm = self.dataframe.parameter[lctm_raw[1:]].value if lctm_raw.startswith("&") else int(lctm_raw)
        else:
            lctm = 0

        if len(erode_raw) > 0:
            erode = self.dataframe.parameter[erode_raw[1:]].value if erode_raw.startswith("&") else int(erode_raw)
        else:
            erode = 0

        if len(ms1st_raw) > 0:
            ms1st = self.dataframe.parameter[ms1st_raw[1:]].value if ms1st_raw.startswith("&") else int(ms1st_raw)
        else:
            ms1st = 0

        uid = len(self.dataframe.control_timestep) + 1

        self.dataframe.control_timestep[uid] = ControlTimestep(uid=uid,
                                                               dtinit=dtinit,
                                                               tssfac=tssfac,
                                                               isdo=isdo,
                                                               tslimt=tslimt,
                                                               dt2ms=dt2ms,
                                                               lctm=lctm,
                                                               erode=erode,
                                                               ms1st=ms1st)

        return