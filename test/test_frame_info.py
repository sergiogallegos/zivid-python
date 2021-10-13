from datetime import datetime
import zivid


def test_time_stamp(frame_info):
    time_stamp = frame_info.time_stamp
    assert time_stamp
    assert isinstance(time_stamp, datetime)


def test_software_version(frame_info):
    software_version = frame_info.software_version
    assert software_version
    assert isinstance(software_version, zivid.frame_info.FrameInfo.SoftwareVersion)
    assert software_version.core
    assert isinstance(software_version.core, str)


def test_set_time_stamp(frame_info):
    assert isinstance(frame_info.time_stamp, datetime)
    assert isinstance(str(frame_info.time_stamp), str)
    new_time_stamp = datetime(1992, 2, 7)
    frame_info.time_stamp = new_time_stamp
    assert isinstance(str(frame_info.time_stamp), str)
    assert isinstance(frame_info.time_stamp, datetime)
    assert frame_info.time_stamp == new_time_stamp
