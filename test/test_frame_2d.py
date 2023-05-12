import numpy as np
import pytest


@pytest.mark.physical_camera
def test_image_context_manager(physical_camera_frame_2d):
    import zivid

    with physical_camera_frame_2d.image_rgba() as image_rgba:
        assert image_rgba is not None
        assert isinstance(image_rgba, zivid.Image)

    with physical_camera_frame_2d.image_bgra() as image_bgra:
        assert image_bgra is not None
        assert isinstance(image_bgra, zivid.Image)


@pytest.mark.physical_camera
def test_image(physical_camera_frame_2d):
    import zivid

    image_rgba = physical_camera_frame_2d.image_rgba()
    assert image_rgba is not None
    assert isinstance(image_rgba, zivid.Image)

    image_bgra = physical_camera_frame_2d.image_bgra()
    assert image_bgra is not None
    assert isinstance(image_bgra, zivid.Image)


@pytest.mark.physical_camera
def test_image_rgba_bgra_correspondence(physical_camera_frame_2d):
    rgba = physical_camera_frame_2d.image_rgba().copy_data()
    bgra = physical_camera_frame_2d.image_bgra().copy_data()

    np.testing.assert_array_equal(bgra[:, :, 0], rgba[:, :, 2])
    np.testing.assert_array_equal(bgra[:, :, 1], rgba[:, :, 1])
    np.testing.assert_array_equal(bgra[:, :, 2], rgba[:, :, 0])
    np.testing.assert_array_equal(bgra[:, :, 3], rgba[:, :, 3])


@pytest.mark.physical_camera
def test_state(physical_camera_frame_2d):
    import zivid

    state = physical_camera_frame_2d.state
    assert state is not None
    assert isinstance(state, zivid.CameraState)


@pytest.mark.physical_camera
def test_info(physical_camera_frame_2d):
    import zivid

    info = physical_camera_frame_2d.info
    assert info is not None
    assert isinstance(info, zivid.FrameInfo)


@pytest.mark.physical_camera
def test_camera_info(physical_camera_frame_2d):
    from zivid.camera_info import CameraInfo

    camera_info = physical_camera_frame_2d.camera_info
    assert camera_info
    assert isinstance(camera_info, CameraInfo)


@pytest.mark.physical_camera
def test_settings(physical_camera_frame_2d):
    import zivid

    settings_2d = physical_camera_frame_2d.settings
    assert settings_2d is not None
    assert isinstance(settings_2d, zivid.Settings2D)


@pytest.mark.physical_camera
def test_release(physical_camera_frame_2d):
    physical_camera_frame_2d.image_rgba()
    physical_camera_frame_2d.release()
    with pytest.raises(RuntimeError):
        physical_camera_frame_2d.image_rgba()


@pytest.mark.physical_camera
def test_context_manager(physical_camera):
    import zivid

    settings_2d = zivid.Settings2D(acquisitions=[zivid.Settings2D.Acquisition()])
    with physical_camera.capture(settings_2d) as frame_2d:
        frame_2d.image_rgba()
    with pytest.raises(RuntimeError):
        frame_2d.image_rgba()

    with physical_camera.capture(settings_2d) as frame_2d:
        frame_2d.image_bgra()
    with pytest.raises(RuntimeError):
        frame_2d.image_bgra()
